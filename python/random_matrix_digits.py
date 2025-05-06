import random
def rozmiar():
    while True:
        x=int(input("liczba"))              #tworzenie rozmiaru macierzy
        if 3<= x <=12:
            return x
        else:
            print("zla liczb")
def tworzenie_macierzy(x):
    macierz= [[chr(random.randint(32, 127)) for _ in range(x)] for _ in range(x)]       #tworzenie macierzy z losowych elementow
    return macierz
def wyswietlanie(macierz):
    for wiersz in macierz:
         print(" ".join(wiersz))                            #wyswietlanie macierzy
def suma(macierz):
    suma=0
    for wiersz in macierz:
        for znak in wiersz:                             #sumowanie liczb w macierzy
            if znak.isdigit():
                suma+= int(znak)
    return suma
macierze=tworzenie_macierzy(rozmiar())
wyswietlanie(macierze)                                      
print(f"suma wynosi: {suma(macierze)}")                     