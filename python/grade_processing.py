def oblicz_ocene_koncowa(srednia):
    # Zaokrąglanie średniej do najbliższej połówkowej
    return round(srednia * 2) / 2

def przetworz_dane(plik_wejsciowy, plik_wyjsciowy, kryterium_sortowania):
    with open(plik_wejsciowy, 'r') as wejsciowy:
        uczniowie = []

        
        for linia in wejsciowy:
            dane = linia.split()
            imie = dane[0]
            nazwisko = dane[1]
            oceny = list(map(int, dane[2:]))  # Przekształcenie ocen na liczby całkowite

            # Obliczanie średniej ocen
            srednia = sum(oceny) / len(oceny)
            ocena_koncowa = oblicz_ocene_koncowa(srednia)

            
            uczniowie.append((nazwisko, imie, oceny, srednia, ocena_koncowa))

       
        if kryterium_sortowania == 'srednia':
            uczniowie.sort(key=lambda x: x[3], reverse=True)  # Sortowanie po średniej malejąco
        elif kryterium_sortowania == 'nazwisko':
            uczniowie.sort(key=lambda x: x[0])  # Sortowanie po nazwisku rosnąco
        elif kryterium_sortowania == 'liczba_ocen':
            uczniowie.sort(key=lambda x: len(x[2]))  # Sortowanie po liczbie ocen rosnąco

        
        with open(plik_wyjsciowy, 'w') as wyjsciowy:
            for uczen in uczniowie:
                wynik = f"{uczen[0]} {uczen[1]} {' '.join(map(str, uczen[2]))} {uczen[3]:.2f} {uczen[4]}\n"
                wyjsciowy.write(wynik)


przetworz_dane('plik_wejsciowy2.txt', 'wynik_a.txt', kryterium_sortowania='srednia')  #srednia ocen
przetworz_dane('plik_wejsciowy2.txt', 'wynik_b.txt', kryterium_sortowania='nazwisko')  # Sortowanie po nazwisku (rosnąco)
przetworz_dane('plik_wejsciowy2.txt', 'wynik_c.txt', kryterium_sortowania='liczba_ocen')  # Sortowanie po liczbie ocen (rosnąco)
przetworz_dane('plik_wejsciowy2.txt', 'wynik_d.txt', kryterium_sortowania='srednia')  # Sortowanie po średniej (malejąco)
