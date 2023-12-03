nome = "Joaquim"
def cumprimentar_v3():
    print(f"Bom dia {nome}")

resultado = 0
x = 0
y = 0

def soma():
    global resultado,x,y
    resultado = x + y
    x = 0

def main():
    global x,y
    x = 10
    y = 5
    soma()
    print(resultado)

if __name__ == "__main__":
    main()