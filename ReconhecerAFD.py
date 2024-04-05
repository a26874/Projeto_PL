import json
import sys


def main():

    def reconhecerPalavra(palavra: str, lista_caminho: list):
        """_summary_
        
        Função que recebe uma palavra e tenta reconhecê-la, se nao reconhecer, retorna o False, senao, retorna True.
        A função envia tambem o caminho realizado pela função.
        
        Args:
            palavra (str): palavra recebida do user
            lista_caminho (list): caminho realizado na analise da palavra

        Returns:
            bool: False or True, dependendo se reconhece ou nao a palavra
            lista_caminho: caminho realizado até a ultima instrução do reconhecimento
        """
        estado_atual: str = q0
        tam: int = len(palavra)
        i: int = 0
        aux_caminho = []
        aux_caminho.append(palavra)
        # Enquanto o tamanho da palavra for maior que i, é feito a determinação se ela é reconhecida ou não. Caso o estado_atual seja
        # atualizado para erro (quando não é encontrado nenhum caminho por esse estado e pelo simbolo) esse mesmo é atuzliado para erro.
        while (i < tam) and (estado_atual != "erro"):
            simbolo_atual = palavra[i]
            if (simbolo_atual in delta[estado_atual]):
                # Caso o simbolo esteja no delta daquele estado, é adicionado a uma lista de caminhos auxiliar e passado ao estado seguinte.
                aux_caminho.extend([estado_atual, simbolo_atual])
                estado_atual = delta[estado_atual][simbolo_atual]
            else:
                estado_atual = "erro"
            i = i+1
        # Caso esteja no ultimo simbolo e o estado atual pertenca aos estados finais, adiciona o camihno a lista de caminhos e retorna true
        lista_caminho.append(aux_caminho)
        if estado_atual in F:
            return True, lista_caminho
        else:
            return False, lista_caminho


    if len(sys.argv) < 3:
        print("Uso: python ReconhecerAFD.py ARQUIVO_JSON [-graphviz] [-rec VALOR_REC]")
        return

    with open(str(sys.argv[1]), "r", encoding="utf-8") as ficheiro:
        af = json.load(ficheiro)

    # Converter listas para sets
    V = set(af["V"])
    Q = set(af["Q"])
    delta = af["delta"]
    q0 = af["q1"]
    F = set(af["F"])
    lista_caminho = []

    if '-graphviz' in sys.argv:
        with open("./digraph/digraph.dot", "w", encoding="utf-8") as ficheiro:
            ficheiro.write("digraph{\n")
            for estado in F:
                ficheiro.write(f"	node [shape = doublecircle]; {estado};\n")
            ficheiro.write("	node [shape = point]; initial;\n")
            ficheiro.write("	node [shape = circle];\n")
            ficheiro.write(f"	initial->{q0}\n")
            for key,value in delta.items():
                i = 0
                string = ""
                for keyv,valuev in value.items():
                    if i == 0:
                        string += f'	{key}->{valuev}[label="{keyv}"]; '
                    elif i == len(value) - 1:
                        string += f'{key}->{valuev}[label="{keyv}"];\n'
                    else:
                        string += f'{key}->{valuev}[label="{keyv}"]; '
                    i += 1
                ficheiro.write(string)
            ficheiro.write("}")
            
    if '-rec' in sys.argv:
        bool = False
        resultado = False
        for i in sys.argv[2:]:
            if (i == '-rec'):
                bool = True
                continue
            if (bool):
                resultado, lista_caminho = reconhecerPalavra(i, lista_caminho)
                for caminho in lista_caminho:
                    if len(caminho) <= 1:
                        print(
                            f"'Palavra:{caminho[0]}, caminho: Não tem caminho")
                    else:
                        stringCaminho = ' -> '.join(caminho[1:])
                        print(
                            f"'Palavra:{caminho[0]}, caminho: {stringCaminho}")
                lista_caminho.clear()


if __name__ == '__main__':
    main()
