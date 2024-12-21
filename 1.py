def calcular_mdc(a,b):
    while b !=0:
        resto= a % b
        a = b
        b = resto
    return abs(a)
def simplificar_fracao(fracao):
    try: 
        if '/' in fracao:
            numerador, denominador = map(int, fracao.split('/'))
            if denominador ==0:
                return "ERR"   
            mdc=calcular_mdc(numerador,denominador)
            numerador//=mdc
            denominador//=mdc
            if denominador==1:
                return str(numerador)
            if abs(numerador)> abs(denominador):
                parte_inteira = numerador//numerador
                numerador_restante= abs(numerador%denominador)
                if numerador_restante==0:
                    return str(parte_inteira)
                else:
                    return f"{parte_inteira} {numerador_restante}/{abs(denominador)}"
            else:
                return f"{numerador}/{denominador}"
        else:
            return str(int(fracao))
    except ValueError:
        return "ERR"    
    except ZeroDivisionError:
        return "ERR"
def processar_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                fracao = linha.strip()
                if fracao:
                    resultado=simplificar_fracao(fracao)
                    print(f"entrada: {fracao} -> Saida: {resultado}")
    except FileNotFoundError:
        print(f"Erro, arquivo nao encontrado")
    except Exception as e:
        print(f"erro inesperado: {e}")
nome_arquivo='frac.txt'
processar_arquivo(nome_arquivo)
