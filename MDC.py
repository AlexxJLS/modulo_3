"""
maximo divisor comum entre 2 números
"""
def mcd(n1,n2):
    if n1<n2:
        menor = n1
    else: 
        menor = n2

    for i in range(menor,0,-1):
        if n1 % i == 0 and n2 % i == 0:
            print(f"O MCD é {i}")
            return

def main():
    numero1 = int(input("Insira o primeiro número:"))
    numero2 = int(input("Insira o segundo número:"))
    mcd(numero1,numero2)

if __name__ == "__main__":
    main()

