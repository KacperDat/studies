slownik = {
    1: "0x1", 
    2: "0x2",                   #tworzenie slownika
    3: "0x3", 
    4: "0x4", 
    5: "0x5"
}
def dodawanie(slownik, klucz, wartosc):
    slownik[klucz] = wartosc                                            #dodawanie elementow
    print(f"Dodano: {klucz} -> {wartosc}")
def usun_element(slownik, klucz):
    if klucz in slownik:
        del slownik[klucz]                                              #usuwanie elementow
        print(f"Usunieto: {klucz}")
    else:
        print(f"Taki klucz nie istnieje")

def wyswietl_slownik(slownik):
    print("Słownik:")
    for klucz, wartosc in slownik.items():                                  #wyswietlanie slownika
        print(f"{klucz} , {wartosc}")

def wyswietl_klucze(slownik):
    print("Klucze :", list(slownik.keys()))                                             #wyswietlanie kluczy

def wyswietl_wartosci(slownik):                                                     #wyswietlanie wartosci
    print("Wartości:", list(slownik.values()))

def wyswietl_ilosc_kluczy(slownik):                                             #wyswietlanie ilosci kluczy
    print(f"Ilość kluczy: {len(slownik)}")

def modyfikuj_wartosc(slownik, klucz, nowa_wartosc):
    if klucz in slownik:
        slownik[klucz] = nowa_wartosc                                                   #modyfikacja wybranych wartosci
        print(f"Modyfikacja: {klucz} -> {nowa_wartosc}")
    else:
        print(f"taki klucz nie istnieje!")
def sumowanie_kluczy(slownik):
    suma = sum(slownik.keys())                                                          #sumowanie kluczy
    print(f"Suma wszystkich kluczy: {suma}")

def slownik_parzyste(slownik):
    parzyste = {klucz: wartosc for klucz, wartosc in slownik.items() if klucz % 2 == 0}                 #tworzenie slownika z prazystymi liczbami
    return parzyste

dodawanie(slownik, 7, "0x7")
usun_element(slownik, 2)
wyswietl_slownik(slownik)
wyswietl_klucze(slownik)                                                            #wyswietlanie wynikow
wyswietl_wartosci(slownik)
wyswietl_ilosc_kluczy(slownik)
modyfikuj_wartosc(slownik, 2, "0x5")
sumowanie_kluczy(slownik)

parzyste_slownik = slownik_parzyste(slownik)
print("Słownik z parzystymi kluczami:",wyswietl_slownik(parzyste_slownik))
