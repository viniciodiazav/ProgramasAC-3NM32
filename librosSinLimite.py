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
        bs = 0
        ma = books[i]
        for j in range(i, i + 3):
            try:
                bs += 1
                print(end=f"{books[j]} ")
                # print(f"{ma} [{j}] es menor que {books[j + 1]} [{j + 1}][{(j - i) + bs}]")
                if ((ma < books[j + 1]) and ((j - i) + bs) != 5):
                    ma = books[j + 1]
            except:
                bs -= 1
                "" 
        print(f"--> Packete {inx} -- cant: {bs} --- mayor: {ma}")
        inx += 1 
        total += ma
    print(f"Total = {total}")
        

p = [5,6,8,9,7,4,2,1,5,7,9,6,3,5,4,4,5,6,9,8,7,1,2,6,8,4,3,2,1,6,9,8,4,1]

makePackages(p)

