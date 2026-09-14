# Aplauso

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

def game(num):
    print()
    for i in range(1, (num + 1)):
        if (i != 1 and i % 10 == 1):
            print()
        if (i % 7 == 0 or i % 10 == 7):
            print(end=f"¡aplauso({i})! ")
        else:
            print(end=f"{i} ")
    print("\n")


num = getNumberGt0("Ingrese el numero a contar: ", "Ingrese un numero valido...")

game(num)
