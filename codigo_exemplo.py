from termcolor import colored
def imprimir_texto_cor(texto,cor):
    print(colored(texto,cor))



def Troco(pagar,dinheiro):
    if dinheiro <= 0 or dinheiro < pagar:
        imprimir_texto_cor("Não tem dinheiro suficiente","red")
        return None
    dinheiro = dinheiro - pagar
    imprimir_texto_cor(f"Pagou {pagar} e ficou com {dinheiro}","blue")
    return dinheiro

carteira = 100
carteira = Troco(50,carteira)
if carteira != None:
    imprimir_texto_cor(f"Tem na carteira {carteira}","green")
else:
    imprimir_texto_cor("Não tem dinheiro na carteira","red")