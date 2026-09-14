# Libros

def getNumberGt0(message: str, error: str):
    num = -1;
    while (num <= 0):
        try:
            num = float(input(message))
            if (num <= 0):
                print("\nIngrese un numero mayor a 0...\n")
        except:
            print(f"\n{error}\n")
    return num

def getPrices():
    prices = []
    for i in range(1, 4):
        prices.append(getNumberGt0(f"Ingrese el precio del libro {i}: $", "Ingrese un precio valido..."))
    prices.sort()
    return prices

def ticket():
    prices = getPrices()
    totalB = sum(prices)
    totalN = prices[-1]
    message = f"""\n====== Ticket ======
Total bruto    ${totalB}
Descuento      ${totalB - totalN}
-----------
Total neto     ${totalN}
"""
    print(message)

ticket()
