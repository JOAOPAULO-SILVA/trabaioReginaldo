base_entrada, base_saida, numero_entrada = map(str,input("Digite a base de entrada a base de saida e o numer à ser convertido: ").split(" "))
base_saida = int(base_saida)
dicionario = {
    "0" : 0,
    "1" : 1,
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9,
    "A" : 10,
    "B" : 11,
    "C" : 12,
    "D" : 13,
    "E" : 14,
    "F" : 15,
    "G" : 16,
    "H" : 17,
    "I" : 18,
    "J" : 19,
    "K" : 20,
    "L" : 21,
    "M" : 22,
    "N" : 23,
    "O" : 24,
    "P" : 25,
    "Q" : 26,
    "R" : 27,
    "S" : 28,
    "T" : 29,
    "U" : 30,
    "V" : 31,
    "W" : 32,
    "X" : 33,
    "Y" : 34,
    "Z" : 35,
    "a" : 36,
    "b" : 37,
    "c" : 38,
    "d" : 39,
    "e" : 40,
    "f" : 41,
    "g" : 42,
    "h" : 43,
    "i" : 44,
    "j" : 45,
    "k" : 46,
    "l" : 47,
    "m" : 48,
    "n" : 49,
    "o" : 50,
    "p" : 51,
    "q" : 52,
    "r" : 53,
    "s" : 54,
    "t" : 55,
    "u" : 56,
    "v" : 57,
    "w" : 58,
    "x" : 59,
    "y" : 60,
    "z" : 61,
}
def converttobase10(base_entrada,numero_entrada):
    indice = len(numero_entrada)-1
    base = int(base_entrada)
    base10=0
    for n in numero_entrada:
        valor = dicionario[n]
        base10 += valor * base**indice
        indice-=1
    return base10

def ValueInDict(valor_desejado):
    for k, v in dicionario.items():
        if valor_desejado == v:
            return k

def base10tobaseX(numBase_10, base_saida):
    dividendo = numBase_10
    numeroFinal  = ""
    while dividendo >= base_saida:
        resto = dividendo % base_saida
        numeroFinal = ValueInDict(resto) + numeroFinal
        dividendo = dividendo // base_saida
    numeroFinal = str(dividendo) + numeroFinal
    return numeroFinal

numero_com_base10 = converttobase10(base_entrada,numero_entrada)
resultado = base10tobaseX(numero_com_base10, base_saida)
print(resultado)