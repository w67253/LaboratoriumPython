
# ----Zadanie 3----

operacja = int(input("""Jaką operację chcesz wykonać? 
1) dodawanie
2) odejmowanie
3) mnożenie
4) dzielenie
5) potęgowanie
Wpisz numer operacji: """))
if(operacja > 5 or operacja < 1):
    print("Błąd numeru operacji!!!!")
    exit()

argument1 = float(input("Podaj argument 1: "))
argument2 = float(input("Podaj argument 2: "))


if(operacja == 1):
    print(argument1 + argument2)
elif(operacja == 2):
    print(argument1 - argument2)
elif(operacja == 3):
    print(argument1 * argument2)
elif(operacja == 4):
    if (argument2 == 0):
        print("Nie dzielimy przez 0")
    else:
        print(argument1 / argument2)
elif(operacja == 5):
    print(argument1 ** argument2)
