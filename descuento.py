# Descuento sobre descuento

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

def getNumberGte0Lte100(message, error):
    num = -1
    while (num < 0 or num > 100):
        try:
            num = int(input(message))
            if (num < 0):
                print("\nIngrese un numero mayor o igual a 0...\n")
            if (num > 100):
                print("\nIngrese un numero mayor o igual a 100...\n")
        except:
            print(f"\n{error}\n")
    return num

def ticket(price, d1, d2):
    firstDisc = price - (price * (d1 / 100))
    finalPrice = firstDisc - (firstDisc * (d2 / 100))
    message = f"""\n====== Ticket ======
Precio inicial           ${price:.2f}
1er descuento (-{d1}%)   ${firstDisc:.2f}
2do descuento (-{d2}%)   ${finalPrice:.2f}
-------------------
Precio final             ${finalPrice:.2f}
"""
    print(message)

initialPrice = getNumberGt0("Ingrese un precio: $", "Ingrese un precio valido...")
disc1 = getNumberGte0Lte100("Ingrese el primer descuento (%): ", "Ingrese un descuento valido")
disc2 = getNumberGte0Lte100("Ingrese el segundo descuento (%): ", "Ingrese un descuento valido")

ticket(initialPrice, disc1, disc2)
