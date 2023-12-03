"""
ver se o numero é primo ou não, usando funções
"""
def primo(numero):
    nd = 0 
    for i in range(2,numero):
        resto = numero % i
        if resto == 0:
            print("Não é primo")
            return
    print("É primo")


def main():
    n_pedido = int(input("Insira o número:"))
    primo(n_pedido)

if __name__ == "__main__":
    main()