liczba=int(input("podaj liczbe ktora chcesz zamienic na system binarny"))
lista=[]
i=1
while(2*i <= liczba):
    i=i*2
    print(i)
while(i>=1):
    if liczba>=i:
        lista.append('1')
        liczba=liczba-i
    else:
        lista.append('0')
        
    
    i=i/2
lancuch= ' '.join(lista)
print(lancuch)