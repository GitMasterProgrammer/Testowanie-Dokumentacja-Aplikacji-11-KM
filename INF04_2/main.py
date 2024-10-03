#*******************************************************
# nazwa funkcji: NWD
# parametry wejściowe: a - liczba, b - liczba
# wartość zwracana: Największy wspolny dzielnik liczb a i b
# informacje: Funkcja oblicza według algorytmu Euklidesa najwieszy wspolny dzielnik liczb a i b
# autor: 0696969
#****************************************************
def NWD(a, b):
    while b:
        temp = a
        a = b
        b = temp%b
    return a

a = int(input("Podaj a: "))


b = int(input("Podaj b: "))

print("NWD: "+str(NWD(a, b)))