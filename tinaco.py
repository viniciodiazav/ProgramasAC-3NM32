# Tinaco

import math as m

def getNumberGt0(message, error):
    num = -1;
    while (num <= 0):
        try:
            num = float(input(message))
            if (num <= 0):
                print("\nIngrese un numero mayor a 0...\n")
        except:
            print(f"\n{error}\n")
    return num

def getVolume(r, h):
    return m.pi * pow(r, 2) * h

def printResults(r, h):
    volume = getVolume(r, h)

    message = f"""\n====== Resultados ======
Volumenes:
{volume:.2f} m^3
{(volume * 1000):.2f} Litros\n"""

    print(message)

radius = getNumberGt0("Ingrese el perimetro en cm: ", "Ingrese un perimetro valido...") / 200
height = getNumberGt0("Ingrese la altura en cm: ", "Ingrese una altura valida...") / 100

printResults(radius, height)
