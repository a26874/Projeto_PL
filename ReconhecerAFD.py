import json

with open("json/AFD.json", "r", encoding="utf-8") as ficheiro:
    af = json.load(ficheiro)

#Converter listas para sets
V= set(af["V"])
Q = set(af["Q"])
delta = af["delta"]
q0 = af["q1"]
F = set(af["F"])
listaCaminho = []
auxCaminho = []

#Reconhece a palavra
def reconhecerPalavra(palavra:str) -> bool:
    estado_atual: str = q0
    tam: int = len(palavra)
    i: int = 0
    auxCaminho=[]
    auxCaminho.append(palavra)
    #Enquanto o tamanho da palavra for maior que i, é feito a determinação se ela é reconhecida ou não. Caso o estado_atual seja
    #atualizado para erro (quando não é encontrado nenhum caminho por esse estado e pelo simbolo) esse mesmo é atuzliado para erro.
    while(i < tam) and (estado_atual != "erro"):
        simbolo_atual = palavra[i]
        if (simbolo_atual in delta[estado_atual]):
            #Caso o simbolo esteja no delta daquele estado, é adicionado a uma lista de caminhos auxiliar e passado ao estado seguinte.
            auxCaminho.extend([estado_atual,simbolo_atual])
            estado_atual = delta[estado_atual][simbolo_atual]
        else:
            estado_atual = "erro"
        i = i+1
    #Caso esteja no ultimo simbolo e o estado atual pertenca aos estados finais, adiciona o camihno a lista de caminhos e retorna true
    if estado_atual in F:
        listaCaminho.append(auxCaminho)
        return True
    else:
        return False
for exemplo in ["+123","-123", "+2424","+244.22","-42112.22","284829","a244","948329875249539"]:
	print(f"'{exemplo}'\t{reconhecerPalavra(exemplo)}")

for caminho in listaCaminho:
    if len(caminho) <=1:
        print(f"'Palavra:{caminho[0]}, caminho: Não tem caminho")
    else:
        stringCaminho = ' -> '.join(caminho[1:])
        print(f"'Palavra:{caminho[0]}, caminho: {stringCaminho}")