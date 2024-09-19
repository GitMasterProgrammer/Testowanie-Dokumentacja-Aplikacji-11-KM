import random
# ************************************************
#   nazwa: sumPoints
#   opis: Sumuje punkty do gry w kosci
#   parametry: tablica losowych liczb
#   zwracany typ i opis: Number - zwracana suma
#   autor: Ja
# ************************************************
def sumPoints(tab):
    t2 = []
    for i in range(len(tab)):
        for j in range(len(tab)):
            if (j != i and tab[i] == tab[j]):
                if (tab[i] not in t2):
                    t2.append(tab[i])
    sum = 0
    for i in range(len(tab)):
        if tab[i] in t2:
            sum += tab[i]

    return sum
# ************************************************
#   nazwa: randomTab
#   opis: Losuje liczby do gry
#   parametry: liczba rzutow kostka
#   zwracany typ i opis: array t- ablica wylosowanych liczba
#   autor: Ja
# ************************************************
def randomTab(n):
    r_tab=[]
    for i in range(n):
        rand = random.randint(1, 6)

        print(f"Kostka {i + 1}:", rand)
        r_tab.append(rand)
    return r_tab

n = 0
choice = "t"

while (choice == "t"):

    while (n < 3 or n > 10):
        n = int(input("Ile kostek rzucić?(3-10): "))

    points = 0
    r_tab = randomTab(n)
    points = sumPoints(r_tab)

    print(points)

    choice = input("Jescze raz? (t/n) ")
    n = 0
