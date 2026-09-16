# Libros sin limite

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

def getBooks():
    print("====== Libreria ¡promocion de 3x1! ======\n*** precione la tecla \"q\" para salir ***")
    books = []
    book = -1
    i = 1
    while (book != 'q' or book <= 0):
        book = input(f"Libro [{i}]: $")
        if (book == 'q'):
            print("\nSaliendo...\n")
            return books
        try:
            book = float(book)
            if (book <= 0):
                print("\n*** Ingrese un precio mayor a 0 ****\n")
            else:
                books.append(book)
                i += 1
        except:
            print("\n*** Ingrese un precio valido ***\n")

def makePackages(books):
    lenght = len(books)
    inx = 1;
    bs = 0
    total = 0
    for i in range(0, lenght, 3):
        ma = books[i]
        for j in range(i, i + 3):
            try:
                print(end=f"${books[j]} ")
                if ((ma < books[j + 1]) and ((j - i) + bs) != 5):
                    ma = books[j + 1]
            except:
                "" 
        print(f"--> Paquete {inx}, Libro de mayor precio: ${ma}")
        inx += 1 
        total += ma
    print(f"====== Ticket ======\nTotal a pagar: ${total}")
        

books = getBooks()
makePackages(books)

