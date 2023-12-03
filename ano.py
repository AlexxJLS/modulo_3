def anobissexto():
    ano = int(input("Ano que pretende introduzir:"))

    if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
        return True
    else:
        return False
    

def main():
    if anobissexto() == True:
        print("Bissexto")
    else:
        print("Não é bissexto")


if __name__ == "__main__":
    main()