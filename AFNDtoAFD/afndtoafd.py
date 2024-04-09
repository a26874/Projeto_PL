import json
from collections import deque
import sys

# Função para calcular o fecho epsilon de um conjunto de estados
def fecho_epsilon(estados, transicoes):
    fecho_epsilon_set = set(estados)
    fila = deque(estados)
    while fila:
        estado = fila.popleft()
        if 'ε' in transicoes[estado]:
            estados_epsilon = transicoes[estado]['ε']
            for estado_epsilon in estados_epsilon:
                if estado_epsilon not in fecho_epsilon_set:
                    fecho_epsilon_set.add(estado_epsilon)
                    fila.append(estado_epsilon)
    return list(fecho_epsilon_set)

# Função para mover-se de um conjunto de estados dado um símbolo de entrada
def mover(estados, simbolo, transicoes):
    estados_movidos = set()
    for estado in estados:
        if simbolo in transicoes[estado]:
            estados_movidos.update(transicoes[estado][simbolo])
    return list(estados_movidos)

# Função principal para converter um AFND para um AFD
def converter_afnd_para_afd(afnd):
    # Carregar AFND do JSON
    with open(AFND, 'r') as f:
        afnd_data = json.load(f)

    # Inicialização do AFD
    alfabeto = afnd_data['alphabet']
    estado_inicial = afnd_data['initial_state']
    estados_afnd = afnd_data['states']
    transicoes_afnd = afnd_data['transitions']
    estados_finais_afnd = afnd_data['final_states']
    estados_afd = []
    transicoes_afd = {}
    estado_inicial_afd = fecho_epsilon([estado_inicial], transicoes_afnd)

    # Algoritmo de conversão
    estados_nao_processados = [estado_inicial_afd]
    while estados_nao_processados:
        estados_atuais = estados_nao_processados.pop()
        estados_afd.append(estados_atuais)
        for simbolo in alfabeto:
            estados_movidos = mover(estados_atuais, simbolo, transicoes_afnd)
            fecho_epsilon_estados = fecho_epsilon(estados_movidos, transicoes_afnd)
            if fecho_epsilon_estados:
                if fecho_epsilon_estados not in estados_afd and fecho_epsilon_estados not in estados_nao_processados:
                    estados_nao_processados.append(fecho_epsilon_estados)
                transicoes_afd.setdefault(tuple(estados_atuais), {})[simbolo] = fecho_epsilon_estados

    # Mapear estados do AFD para índices
    mapa_estados_afd = {tuple(estado): i for i, estado in enumerate(estados_afd)}

    # Construir AFD em formato JSON
    afd_json = {
        "alfabeto": alfabeto,
        "estados": [str(i) for i in range(len(estados_afd))],
        "estado_inicial": str(mapa_estados_afd[tuple(estado_inicial_afd)]),
        "transicoes": {
            str(mapa_estados_afd[estado]): {simbolo: str(mapa_estados_afd[tuple(estado_alvo)]) for simbolo, estado_alvo in transicoes.items()}
            for estado, transicoes in transicoes_afd.items()
        }
    }

    return afd_json

# Função principal do programa
def principal():
    if len(sys.argv) < 3:
        print("Uso: python afnd_main.py afnd.json -saida AFD.json")
        return

    arquivo_afnd = sys.argv[1]
    arquivo_saida = sys.argv[3]
    afd_json = converter_afnd_para_afd(arquivo_afnd)
 
    # Escrever o JSON do AFD no arquivo de saída "AFD.json"
    with open("AFD.json", 'w') as f:
        json.dump(afd_json, f, indent=4)

if __name__ == "__main__":
    principal()
