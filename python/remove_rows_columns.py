def usun_wie_kol(input_file, output_file):
    with open(input_file, "r") as infile, open(output_file, "w") as outfile:
                                                                                # Wczytanie pierwszych dwóch linii
        usuwanie_wierszy = list(map(int, infile.readline().strip().split()))  
        usuwanie_kolumn = list(map(int, infile.readline().strip().split()))  
        
        infile.readline()                                           # Pomijanie pustej linijki
        
        
        macierz = [list(map(int, linia.strip().split())) for linia in infile]

        
        macierz = [wiersz for i, wiersz in enumerate(macierz) if i + 1 not in usuwanie_wierszy]                     # Usuwanie wierszy
        
        macierz = [[wiersz[j] for j in range(len(wiersz)) if j + 1 not in usuwanie_kolumn] for wiersz in macierz]                   # Usuwanie kolumn



        for wiersz in macierz:
            outfile.write(" ".join(map(str, wiersz)) + "\n")                    # Zapis do nowego pliku


usun_wie_kol("plik_wejsciowy.txt", "plik_wyjsciowy.txt")
