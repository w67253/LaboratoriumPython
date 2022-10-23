liczba1 = int(input("Liczba 1: "))
liczba2 = int(input("Liczba 2: "))

if(liczba1 > liczba2):
    wieksza = liczba1
    mniejsza = liczba2
else:
    wieksza = liczba2
    mniejsza = liczba1

while(mniejsza <= wieksza):
    print(mniejsza, end=' ')
    mniejsza = mniejsza + 1