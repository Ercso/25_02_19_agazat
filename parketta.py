"""1. feladat Parkettázás
Írjon programot parketta.py néven, ami billentyűzetről bekéri egy szoba szélességét és magasságát méterben, valamint, hogy hány csomag parkettával rendelkezünk. Tudjuk, hogy egy csomag parketta 2 m2 felület burkolására elegendő, ezek alapján a program számolja ki és írja ki a burkolandó helység területét, és azt, hogy szükséges-e még parkettát vásárolnunk! A burkolandó területet a terület = szélesség * magasság képlettel kaphatjuk meg.
Minta:
Kérem a szoba szélességét: 4.2
Kérem a szoba hosszúságát: 5.6
Hány csomag parketta van: 10
A szoba területe 23.52 négyzetméter.
Szükséges még parkettát vásárolni!
Kérem a szoba szélességét: 5.2
Kérem a szoba hosszúságát: 3.9
Hány csomag parketta van: 12
A szoba területe 20.28 négyzetméter.
Van elegendő parketta!"""

# szoba_sz = float(input("Kérem a szoba szélességét: "))
# szoba_hossz = float(input("Kérem a szoba hosszúságát: "))
# csomagok_szama = int(input("Hány csomag parketta van: "))

# terulet = szoba_sz * szoba_hossz
# print("A szoba területe ", terulet, "négyzetméter.")

# if csomagok_szama * 2 >= terulet:
#     print("Van elegendő parketta!")
# else:
#     print("Szükséges más parkettát vásárolni!")

"""2. feladat: Negatív	14 pont
Írjon programot negativ.py néven. A programban hozzon létre egy függvényt negativ néven, ami egy egész számot kap paraméterként, és igaz értéket ad vissza, ha a szám 0-nál kisebb, egyébként hamis értékkel térjen vissza. Ezt követően generáljon 100 db -50 és 50 közé eső véletlen számot, és a függvény felhasználásával számolja meg, hogy a generált számok közül hány volt negatív. A választ a mintát látható módon írja ki a képernyőre!
Minta:
A generált számok között 47 negatív szerepelt."""

import random

def negativ(szam):
    if szam < 0:
        return True
    else:
        return False

negativ_szamok = 0
for i in range(100):
    szam = random.randint(-50, 50)
    if negativ(szam):
        negativ_szamok += 1
print("A generált számok Közt", negativ_szamok, "negatív szerepelt.")