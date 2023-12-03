"""
Mesma coisa que o ex da tabuada mas com uma variavel global
"""

n_pedido = int(input("Insira o número:"))

def tabuada():
    global n_pedido
    for i in range(1,11):
        total = i * n_pedido
        print(i,"x",n_pedido,"=",total)
    n_pedido = 0

def main():
    
    tabuada()    

if __name__ == "__main__":
    main()
