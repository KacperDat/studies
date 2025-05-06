import math


def generator_nieparzystych(n):
    for i in range(1, 2*n, 2):  
        yield i

def oblicz_pierwiastki(n):
    generator = generator_nieparzystych(n)
    pierwiastki = []
    pierwiastki_calkowite = 0
    
    for liczba in generator:
        pierwiastek = math.sqrt(liczba)
        pierwiastki.append(pierwiastek)
        if pierwiastek.is_integer():
            pierwiastki_calkowite += 1

    return pierwiastki, pierwiastki_calkowite


n = 10  
pierwiastki, pierwiastki_calkowite = oblicz_pierwiastki(n)

# Wyniki
print(f"Pierwiastki z wygenerowanych liczb nieparzystych: {pierwiastki}")
print(f"Liczba pierwiastków całkowitych: {pierwiastki_calkowite}")
