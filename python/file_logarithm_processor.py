import math

def odczytaj_plik_i_oblicz_logarytmy():
    nazwa_pliku = input("Podaj nazwę pliku z liczbami: ")

    if not nazwa_pliku:
        print("Nie podano nazwy pliku.")
        return

    try:
        with open(nazwa_pliku, "r") as plik:
            zawartosc = plik.readlines()
    except FileNotFoundError:
        print("Plik o podanej nazwie nie istnieje.")
        return
    except OSError:
        print("Nie można otworzyć pliku o podanej nazwie.")
        return

    try:
        liczby = [float(linia.strip()) for linia in zawartosc]
    except ValueError:
        print("Plik zawiera dane, które nie są liczbami.")
        return

    try:
        logarytmy = [math.log(liczba) for liczba in liczby if liczba > 0]
        if len(logarytmy) != len(liczby):
            print("Ostrzeżenie: Nie wszystkie liczby były dodatnie. Pominęto wartości ujemne lub zero.")
    except ValueError:
        print("Błąd podczas obliczania logarytmów.")
        return

    nazwa_wyjscia = "logarytmy.txt"
    try:
        with open(nazwa_wyjscia, "w") as plik:
            plik.write("\n".join(map(str, logarytmy)))
        print(f"Logarytmy zostały zapisane w pliku {nazwa_wyjscia}.")
    except OSError:
        print("Nie udało się zapisać pliku z logarytmami.")

if __name__ == "__main__":
    odczytaj_plik_i_oblicz_logarytmy()
