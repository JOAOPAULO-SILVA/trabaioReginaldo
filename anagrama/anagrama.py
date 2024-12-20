import sys
import re
from collections import Counter

def carregar_palavras(arquivo):
    try:
        with open(arquivo, 'r') as f:
            palavras = {linha.strip().upper() for linha in f}
        return palavras
    except FileNotFoundError:
        print("Erro: O arquivo 'words.txt' não foi encontrado.")
        sys.exit(1)

def validar_expressao(expressao):
    if not re.match(r'^[A-Z\s]*$', expressao):
        print("Erro: A expressão contém caracteres inválidos. Use apenas letras de A a Z e espaços.")
        sys.exit(1)


def gerar_anagramas(expressao, palavras_validas):

    letras = Counter(expressao.replace(" ", ""))
    resultados = set()

    # Função recursiva para encontrar combinações de anagramas
    def buscar_anagramas(letras_restantes, caminho):
        if not letras_restantes:
            resultados.add(" ".join(sorted(caminho)))
            return

        for palavra in palavras_validas:
            contador_palavra = Counter(palavra)
            if all(letras_restantes[letra] >= contador_palavra[letra] for letra in contador_palavra):
                buscar_anagramas(letras_restantes - contador_palavra, caminho + [palavra])

    buscar_anagramas(letras, [])
    return resultados

def main():
    if len(sys.argv) != 2:
      print("Uso: python anagrama.py '<expressão>'")
      sys.exit(1)
      
    expressao = sys.argv[1].upper()
    validar_expressao(expressao)

    palavras_validas = carregar_palavras("words.txt")

    anagramas = gerar_anagramas(expressao, palavras_validas)

    for anagrama in sorted(anagramas):
        print(anagrama)

if __name__ == "__main__":
    main()