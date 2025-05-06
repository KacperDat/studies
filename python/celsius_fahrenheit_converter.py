import random
import sys

def celsjusz_na_fahrenheit(celsjusz):
    """Funkcja konwertująca temperaturę z Celsjusza na Fahrenheita"""
    return celsjusz * 9 / 5 + 32

def fahrenheit_na_celsjusz(fahrenheit):
    """Funkcja konwertująca temperaturę z Fahrenheita na Celsjusza"""
    return (fahrenheit - 32) * 5 / 9

def generuj_losowe_temperatury_celsjusz(n):
    """Funkcja generująca n losowych temperatur w Celsjuszach w przedziale [-30, 50]"""
    return [round(random.uniform(-30, 50), 2) for _ in range(n)]

def main():
    # Sprawdzenie, czy argument z liczbą temperatur został przekazany
    if len(sys.argv) != 2:
        print("Błąd: Nie podano liczby temperatur.")
        print("Użycie: python temperatures_program.py <liczba_temperatur>")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        if n <= 0:
            raise ValueError("Liczba temperatur musi być większa od zera.")
    except ValueError as e:
        print(f"Błąd: {e}")
        print("Użycie: python temperatures_program.py <liczba_temperatur>")
        sys.exit(1)

    # Generowanie losowych temperatur w Celsjuszach
    celsjusz_temperatury = generuj_losowe_temperatury_celsjusz(n)

    # Zapisanie temperatur do pliku celsjusz.txt
    with open("celsjusz.txt", "w") as file:
        file.write("\n".join(map(str, celsjusz_temperatury)))
    print(f"Plik celsjusz.txt został utworzony z {n} temperaturami.")

    # Odczytanie temperatur z pliku celsjusz.txt
    try:
        with open("celsjusz.txt", "r") as file:
            celsjusz_temperatury = file.readlines()
    except FileNotFoundError:
        print("Błąd: Plik celsjusz.txt nie istnieje.")
        return
    except Exception as e:
        print(f"Błąd podczas odczytu pliku: {e}")
        return

    # Przekształcanie odczytanych danych na liczby zmiennoprzecinkowe
    try:
        celsjusz_temperatury = [float(temp.strip()) for temp in celsjusz_temperatury]
    except ValueError:
        print("Błąd: Plik celsjusz.txt zawiera nieprawidłowe dane.")
        return

    # Konwersja temperatur z Celsjusza na Fahrenheita
    fahrenheit_temperatury = [celsjusz_na_fahrenheit(temp) for temp in celsjusz_temperatury]

    # Zapisanie przekształconych temperatur do pliku fahrenheit.txt
    try:
        with open("fahrenheit.txt", "w") as file:
            file.write("\n".join(map(str, fahrenheit_temperatury)))
        print("Plik fahrenheit.txt został utworzony.")
    except Exception as e:
        print(f"Błąd podczas zapisu do pliku fahrenheit.txt: {e}")

if __name__ == "__main__":
    main()
