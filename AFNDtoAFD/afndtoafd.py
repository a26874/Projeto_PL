import json
from collections import deque

# Função para calcular o fecho epsilon de um conjunto de estados
def epsilon_closure(states, transitions):
    epsilon_closure_set = set(states)
    queue = deque(states)
    while queue:
        state = queue.popleft()
        if 'ε' in transitions[state]:
            epsilon_states = transitions[state]['ε']
            for epsilon_state in epsilon_states:
                if epsilon_state not in epsilon_closure_set:
                    epsilon_closure_set.add(epsilon_state)
                    queue.append(epsilon_state)
    return list(epsilon_closure_set)

# Função para mover-se de um conjunto de estados dado um símbolo de entrada
def move(states, symbol, transitions):
    moved_states = set()
    for state in states:
        if symbol in transitions[state]:
            moved_states.update(transitions[state][symbol])
    return list(moved_states)

# Função principal para converter um AFND para um AFD
def convert_afnd_to_afd(afnd):
    # Carregar AFND do JSON
    with open(afnd, 'r') as f:
        afnd_data = json.load(f)

    # Inicialização do AFD
    alphabet = afnd_data['alphabet']
    initial_state = afnd_data['initial_state']
    afnd_states = afnd_data['states']
    afnd_transitions = afnd_data['transitions']
    afd_states = []
    afd_transitions = {}
    afd_initial_state = epsilon_closure([initial_state], afnd_transitions)

    # Algoritmo de conversão
    unprocessed_states = [afd_initial_state]
    while unprocessed_states:
        current_states = unprocessed_states.pop()
        afd_states.append(current_states)
        for symbol in alphabet:
            moved_states = move(current_states, symbol, afnd_transitions)
            epsilon_closure_states = epsilon_closure(moved_states, afnd_transitions)
            if epsilon_closure_states:
                if epsilon_closure_states not in afd_states and epsilon_closure_states not in unprocessed_states:
                    unprocessed_states.append(epsilon_closure_states)
                afd_transitions.setdefault(tuple(current_states), {})[symbol] = epsilon_closure_states

    # Mapear estados do AFD para índices
    afd_state_map = {tuple(state): i for i, state in enumerate(afd_states)}

    # Construir AFD em formato JSON
    afd_json = {
        "alphabet": alphabet,
        "states": [str(i) for i in range(len(afd_states))],
        "initial_state": str(afd_state_map[tuple(afd_initial_state)]),
        "transitions": {
            str(afd_state_map[state]): {symbol: str(afd_state_map[tuple(target_state)]) for symbol, target_state in transitions.items()}
            for state, transitions in afd_transitions.items()
        }
    }

    return afd_json

# Função principal do programa
def main():
    import sys
    if len(sys.argv) < 3:
        print("Usage: python afnd_main.py afnd.json -output afd.json")
        return

    afnd_file = sys.argv[1]
    output_file = sys.argv[3]
    afd_json = convert_afnd_to_afd(afnd_file)
 
# Escrever o JSON do AFD no ficheiro de saída
    with open(output_file, 'w') as f:
        json.dump(afd_json, f, indent=4)



if __name__ == "__main__":
    main()
