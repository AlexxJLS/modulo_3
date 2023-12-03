
def soma(n1,n2):
    Resultado = n1 + n2
    print(Resultado)

def subtração(n1,n2):
    Resultado = n1 - n2
    print(Resultado)

def multiplicação(n1,n2):
    Resultado = n1 * n2
    print(Resultado)

def divisão(n1,n2):
    Resultado = n1 / n2
    print(Resultado)

def menu():
    print(" 1.Somar \n 2.Subtrair \n 3.Multiplicar \n 4.Dividir")
    op = input("Escolha uma opção:")
    x = float(input("1º valor:"))
    y = float(input("2º Valor:"))
    if op == "1":
        soma(x,y)
    elif op == "2":
        subtração(x,y)
    elif op == "3":
        multiplicação(x,y)
    else:
        divisão(x,y)

def main():
    menu()
if __name__ == "__main__":
    main()