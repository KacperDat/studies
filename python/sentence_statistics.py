zdanie=input("wklej zdanie ")
zdanie=zdanie.lower()
alfabet = "aąbcćdeęfghijklłmnńoóprsśtuwyzźż "
licznik={znak: 0 for znak in alfabet }
for znak in zdanie:
    if znak in alfabet:
        licznik[znak]=licznik[znak]+1
for znak in alfabet:
    print(f"{znak} : {licznik[znak]}")
wszystkie_znaki = sum(licznik.values())
for znak in alfabet:

    if wszystkie_znaki > 0:
        procent = (licznik[znak] / wszystkie_znaki) * 100
    else:
        procent = 0
    print(f"{znak} : {licznik[znak]} razy, {procent:.2f}%")
