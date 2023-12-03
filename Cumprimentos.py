def cumprimentar():
    print("Bom dia")

def cumprimentar_v2():
    nome = input("Qual é o seu nome?:")
    print(f"Bom dia {nome}")


def cumprimentar_v3(nome):
    print(f"Bom dia {nome}")
    nome = ""

def main():
    nome = input("Qual é o seu nome?:")
    cumprimentar_v3(nome)
    print(nome)


if __name__ == "__main__":
    main()
