import random

def tworzenie_tabeli():
    macierz = []
    k = int(input("Podaj liczbę wierszy: "))
    w = int(input("Podaj liczbę kolumn: "))
    for i in range(k):
        lista = [random.randint(1, 100) for j in range(w)]
        macierz.append(lista)
    for lista in macierz:
        print(lista)
    return macierz

def sumowanie(tabela):
    x = 0
    for wiersz in tabela:
        x = x + sum(wiersz)
    print("Suma wynosi:", x)

def liczby_podzielne(lista, p):
    count = 0
    for liczba in lista:
        if liczba % p == 0:
            count += 1
    return count

def indeksy_min(lista):
    min_wartosc = min(lista)
    indeksy = [i for i, x in enumerate(lista) if x == min_wartosc]
    return indeksy

p = int(input("Podaj liczbę p (do podzielności): "))
macierz = tworzenie_tabeli()
sumowanie(macierz)

for wiersz in macierz:
    print("Indeksy minimalnych wartości w wierszu:", indeksy_min(wiersz))

for wiersz in macierz:
    print(f"Liczba liczb podzielnych przez {p} w wierszu:", liczby_podzielne(wiersz, p))
