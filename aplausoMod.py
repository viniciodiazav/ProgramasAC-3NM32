def getNumberGt0(message, error):
    num = -1;
    while (num <= 0):
        try:
            num = int(input(message))
            if (num <= 0):
                print("\nIngrese un numero mayor a 0...\n")
        except:
            print(f"\n{error}\n")
    return num

def getNumberGte0Lte10(message, error):
    num = -1
    while (num < 0 or num > 10):
        try:
            num = int(input(message))
            if (num < 0):
                print("\nIngrese un numero mayor o igual a 0...\n")
            if (num > 10):
                print("\nIngrese un numero mayor o igual a 10...\n")
        except:
            print(f"\n{error}\n")
    return num

def game(num, gNum):
    print()
    for i in range(1, (num + 1)):
        if (i != 1 and i % 10 == 1):
            print()
        if (i % gNum == 0 or i % 10 == gNum):
            print(end=f"¡aplauso({i})! ")
        else:
            print(end=f"{i} ")
    print("\n")


num = getNumberGt0("Ingrese el numero a contar: ", "Ingrese un numero valido...")
gameNum = getNumberGte0Lte10("Ingrese el numero con el que se jugara: ", "Ingrese un numero valido...")

game(num, gameNum)