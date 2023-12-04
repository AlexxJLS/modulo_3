"""
calcular a medida de uma reta entre 2 pontos do cartesiano
"""

import math

def DistanciaDoisPontos(x1,y1,x2,y2):
    cateto1 = x2 - x1
    cateto2 = y2 - y1
    distancia = math.sqrt(cateto1**2 + cateto2**2)
    print(distancia)
    
def main():
    DistanciaDoisPontos(1,2,4,6)

if __name__ == "__main__":
    main()