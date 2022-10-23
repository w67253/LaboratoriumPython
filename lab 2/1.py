# ----Zadanie 1----
wiek = int(input("Wiek: "))

if(wiek < 4):
    print("Cena 0zł")
elif(wiek >= 4 and wiek < 18):
    print("Cena 10zł")
elif(wiek >= 18):
    print("Cena 20")