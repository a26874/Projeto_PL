import json
from collections import deque
import sys
import os

def fecho_epsilon(estados, transicoes):
    """Calcula o fecho epsilon de um conjunto de estados num autômato.

    Args:
        estados (list): Uma lista de estados do autômato.
        transicoes (dict): Um dicionário que representa as transições do autômato.
            As chaves são os estados e os valores são outro dicionário que mapeia
            símbolos de transição para listas de estados alcançáveis.

    Returns:
        list: Uma lista com  todos os estados possiveis de alcançar a partir dos estados
        de entrada, considerando as transições epsilon.
    """
    fecho_epsilon_set = set(estados)
    fila = deque(estados)
    while fila:
        estado = fila.popleft()

        if '€' in transicoes[estado]:
            estados_epsilon = transicoes[estado]['€']
            for estado_epsilon in estados_epsilon:
                if estado_epsilon not in fecho_epsilon_set:
                    fecho_epsilon_set.add(estado_epsilon)
                    fila.append(estado_epsilon)

    return list(fecho_epsilon_set)



def unir_estados(estado1, estado2):
    """Une dois estados num  único estado.

    Args:
        estado1 (iterable): O primeiro estado a ser unido.
        estado2 (iterable): O segundo estado a ser unido.

    Returns:
        tuple: Um novo estado resultante da união dos dois estados de entrada.
    """
    return tuple(sorted(set(estado1) | set(estado2)))



def mover(estados, simbolo, transicoes):
    """Realiza a operação de mover em um conjunto de estados através de um símbolo de entrada.

    Args:
        estados (list): Lista de estados a serem movidos.
        simbolo (str): Símbolo de entrada para a transição.
        transicoes (dict): Dicionário que mapeia estados para transições.

    Returns:
        list: Uma lista com  os estados possiveis de alcancar a partir dos estados de entrada
        através do símbolo de entrada fornecido.
    """
    estados_movidos = set()
    for estado in estados:
        if simbolo in transicoes[estado]:
            estados_movidos.update(transicoes[estado][simbolo])
    return list(estados_movidos)


# Função principal para converter um AFND para um AFD
def converter_afnd_para_afd(afnd):
    """Converte um autômato finito não determinístico (AFND) em um autômato finito determinístico (AFD).

    Args:
        afnd (str): O caminho do arquivo JSON que contém a descrição do AFND.

    Returns:
        dict: Um dicionário que representa o autômato finito determinístico (AFD) resultante da conversão.
    """
    # Carregar AFND do JSON
    with open(afnd, 'r', encoding='utf-8') as f:
        afnd_data = json.load(f)

    # Inicialização do AFD
    alfabeto = afnd_data['V']
    estado_inicial = afnd_data['q0']
    estados_afnd = afnd_data['Q']
    transicoes_afnd = afnd_data['delta']
    estados_finais_afnd = afnd_data['F']
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
        "V": alfabeto,
        "Q": [str(i) for i in range(len(estados_afd))],
        "q0": str(mapa_estados_afd[tuple(estado_inicial_afd)]),
        "delta": {
            str(mapa_estados_afd[estado]): {simbolo: str(mapa_estados_afd[tuple(estado_alvo)]) for simbolo, estado_alvo in transicoes.items()}
            for estado, transicoes in transicoes_afd.items()
        },
        "F": [str(mapa_estados_afd[tuple(estado)]) for estado in estados_afd if any(ef in estado for ef in estados_finais_afnd)]
    }

    return afd_json


# Função principal do programa
# Função principal do programa
def principal():
    if len(sys.argv) < 2:
        print("Uso: python afnd_main.py afnd.json [nome_ficheiro]")
        return
    infile = sys.argv[1]
    directory = ".\json_novos"
    if not os.path.exists(directory):
        os.makedirs(directory)
    if len(sys.argv) == 3: outfile = f".\json_novos\{sys.argv[2]}.json" 
    else: outfile = f".\json_novos\AFD.json"
    afd_json = converter_afnd_para_afd(infile)
 
    # Escrever o JSON do AFD no ficheiro de saída especificado
    with open(outfile, 'w', encoding='utf-8') as f:
        json.dump(afd_json, f, indent=4)

if __name__ == "__main__":
    principal()
