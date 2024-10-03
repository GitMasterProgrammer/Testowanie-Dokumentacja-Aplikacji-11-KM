import math

n = 100

#*******************************************************
# nazwa funkcji: fillArr
# parametry wejściowe: n - liczba elementow tablicy
# wartość zwracana: tablice wypelniona wartosciami true
# informacje: Funkcja tworzy tablice
# autor: 0696969
#****************************************************
def fillArr(n):
    A=[]
    for i in range(n):
        A.append(True)
    return A

#*******************************************************
# nazwa funkcji: printArr
# parametry wejściowe: Tab - tablica
# wartość zwracana: None
# informacje: Fukcja do printowania elementow tablicy
# autor: 0696969669
#****************************************************
def printArr(Tab):
    for i in range(0, len(Tab), 1):
        if Tab[i] == False:
            print(i+1, end=";")

#*******************************************************
# nazwa funkcji: sito
# parametry wejściowe: n - liczba elementow tablicy
# wartość zwracana: Zwraca tablice gdzie liczby pierwsze sa oznaczone jako False
# informacje: Sito arystotelesa
# autor: 069696969
#****************************************************
def sito(n):
    A = fillArr(n)


    for i in range(2, int(math.sqrt(n)), 1):
        if A[i] == True:
            for j in range(i * i, n, i):
                A[j] = False

    return A


printArr(sito(n))