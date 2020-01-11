def funkcjaZwyczajna(x):
    return x+1

def funkcjaOdFunkcji(f, x):
    return f(x)

#print(funkcjaOdFunkcji(funkcjaZwyczajna, 4))

def funkcjaZew(x):
    def funkcjaWew(y):
        return x*y
    return funkcjaWew

#f = funkcjaZew(3)
#print(f(2))

def dekoratorek(f):
    def funkcjaWew(x):
        print("Tutaj funkcja wewnętrzna")
        wynik = f(x)
        return wynik+1
    return funkcjaWew

@dekoratorek
def funkcjaZwyczajna(x):
    return x+1

print(funkcjaZwyczajna(2))