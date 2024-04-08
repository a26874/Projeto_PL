import sys

def main():
    if len(sys.argv) < 3:
        print("Uso: python expAFND.py ARQUIVO_JSON [--output NOME_JSON]")
        return
    
    with open(str(sys.argv[1]), "r", encoding="utf-8") as ficheiro:
        af = json.load(ficheiro)
    caracteres = list(af)
    
if __name__ == '__main__':
    main()
