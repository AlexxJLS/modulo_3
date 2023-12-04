"""
verificar se uma palavra é uma capicua/palíndromo
"""
def capicua(palavra):
    palavra = palavra.lower()
    palavra2 = ""
    for i in range(len(palavra)-1,-1,-1):
        palavra2 = palavra2 + palavra[i]
    
    print("Palavra ao contrário:",palavra2)

    if palavra == palavra2:
        print("É uma capicua")
    else:
        print("Não é uma capicua")

def main():
    palavra_utilizador = input("Insira a palavra:")
    capicua(palavra_utilizador)

if __name__ == "__main__":
    main()
