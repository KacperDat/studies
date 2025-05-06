import itertools
zbior = {1, 2, 3}
def zbior_potegowy(zbior):
    potegowy = []
    for i in range(len(zbior) + 1):                                         # petla o dlugosci rozmiaru zbioru +1 (w tym przypadku rozmiar zbioru wynosi 3)
        for podzbior in itertools.combinations(zbior, i):                   #generowanie wszyskich mozliwosci 
            potegowy.append(set(podzbior))                                    #zamiana na zbior aby uniknac powtorek
    return potegowy
potegowy = zbior_potegowy(zbior)
for podzbior in potegowy:
    print(podzbior)                                         #wyswietlanie wynikow
print(f"Liczba podzbiorów wynosi: {len(potegowy)}")                     #dla zbioru n-elementowego wyszlo 2^n podzbiorów( 2^3=8)