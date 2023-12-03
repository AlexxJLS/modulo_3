
def soma(n1,n2):
    Resultado = n1 + n2
    return Resultado

def subtração(n1,n2):
    Resultado = n1 - n2
    return Resultado

def multiplicação(n1,n2):
    Resultado = n1 * n2
    return Resultado

def divisão(n1,n2):
    Resultado = n1 / n2
    return Resultado

def menu():
    while True:
        print(" 1.Somar \n 2.Subtrair \n 3.Multiplicar \n 4.Dividir \n 5.sair")
        op = input("Escolha uma opção:")
        if op == "5":
            break
        x = float(input("1º valor:"))
        y = float(input("2º Valor:"))
        if op == "1":
            r = soma(x,y)
        elif op == "2":
            r = subtração(x,y)
        elif op == "3":
            r = multiplicação(x,y)
        else:
            r = divisão(x,y)
        print(r)

def main():
    menu()
if __name__ == "__main__":
    main()