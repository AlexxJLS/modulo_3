def tabuada(numero):
    for i in range(1,11):
        total = i * numero
        print(i,"x",numero,"=",total)

def main():
    n_pedido = int(input("Insira o número:"))
    tabuada(n_pedido)    

if __name__ == "__main__":
    main()
