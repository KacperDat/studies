lista=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','r','s','t','u','w','x','y','z']   #tworzenie listy z alfabetem
x=int(input("podaj liczbe"))    #wczytywanie wielkosci podlist
i=0
podlista=[]          #tworzenie pustej podlisty
while i<len(lista):
    podlista.append(lista[i:i+x])   #dolanczanie do podlisty elementy z listy
    i=i+x
slowa = [''.join(elementy) for elementy in podlista]    #tworzenie slow
zdanie = ' '.join(slowa)                    #tworzenie zdan
print(podlista)
print(slowa)                            #wypisywanie wynikow
print(zdanie)
