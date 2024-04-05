import json
from collections import deque

# Função para calcular o fecho epsilon de um conjunto de estados
def epsilon_closure(states, transitions):
    # Inicializa o conjunto de fecho epsilon com os estados fornecidos
    fecho_epsilon = set(states)
    # Inicializa uma fila para realizar a busca em largura nos estados
    fila = deque(states)
    
    # Realiza a busca em largura nos estados alcançáveis via transições epsilon
    while fila:
        # Obtém o próximo estado da fila
        estado = fila.popleft()
        
        # Verifica se há transições epsilon a partir do estado atual
        if 'ε' in transitions[estado]:
            # Obtém os estados alcançáveis via transições epsilon
            estados_epsilon = transitions[estado]['ε']
            # Itera sobre cada estado alcançável
            for estado_epsilon in estados_epsilon:
                # Se o estado não estiver no fecho epsilon, adiciona ao conjunto e à fila
                if estado_epsilon not in fecho_epsilon:
                    fecho_epsilon.add(estado_epsilon)
                    fila.append(estado_epsilon)
    
    # Retorna o fecho epsilon como uma lista de estados
    return list(fecho_epsilon)

# Função para mover-se de um conjunto de estados dado um símbolo de entrada
def move(states, symbol, transitions):
    # Inicializa um conjunto para armazenar os estados alcançáveis pelo símbolo
    estados_alcancar = set()   
    # Itera sobre cada estado no conjunto de estados fornecido
    for estado in states:
        # Verifica se há uma transição para o símbolo dado a partir do estado atual
        if symbol in transitions[estado]:
            # Adiciona os estados alcançáveis pela transição ao conjunto de estados movidos
            estados_alcancar.update(transitions[estado][symbol])
    
    # Retorna os estados alcançáveis pelo símbolo como uma lista
    return list(estados_alcancar)


# Função principal para converter um AFND para um AFD
def converter_afnd_para_afd(afnd):
    # Carregar AFND do JSON
    with open(afnd, 'r') as f:
        dados_afnd = json.load(f)

    # Inicialização do AFD
    alfabeto = dados_afnd['alphabet']
    estado_inicial = dados_afnd['initial_state']
    estados_afnd = dados_afnd['states']
    transicoes_afnd = dados_afnd['transitions']
    estados_afd = []
    transicoes_afd = {}
    estado_inicial_afd = epsilon_closure([estado_inicial], transicoes_afnd)

    # Algoritmo de conversão
    estados_nao_processados = [estado_inicial_afd]
    while estados_nao_processados:
        estados_atuais = estados_nao_processados.pop()
        estados_afd.append(estados_atuais)
        for simbolo in alfabeto:
            estados_movidos = move(estados_atuais, simbolo, transicoes_afnd)
            fecho_epsilon_estados = epsilon_closure(estados_movidos, transicoes_afnd)
            if fecho_epsilon_estados:
                if fecho_epsilon_estados not in estados_afd and fecho_epsilon_estados not in estados_nao_processados:
                    estados_nao_processados.append(fecho_epsilon_estados)
                transicoes_afd.setdefault(tuple(estados_atuais), {})[simbolo] = fecho_epsilon_estados
    # Mapear estados do AFD para índices
    afd_state_map = {tuple(state): i for i, state in enumerate(afd_states)}

    # Construir AFD em formato JSON
    afd_json = {
        "alphabet": alphabet,
        "states": [str(i) for i in range(len(afd_states))],  # Mapeia os estados do AFD para índices numéricos
        "initial_state": str(afd_state_map[tuple(afd_initial_state)]),  # Obtém o estado inicial do AFD mapeado
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
