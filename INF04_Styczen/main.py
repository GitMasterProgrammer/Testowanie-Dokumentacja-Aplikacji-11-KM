#**********************************************
#   nazwa funkcji: sprawdzPlec
#   opis funkcji: odczytuje plec z danego peselu
#   parametry: pesel
#   zwracany typ i opis: str - zwraca K (jezeli kobieta) lub M (jezeli mezczyzna)
#   autor: 12345678910
#***********************************************

def sprawdzPlec(psl):
    if(int(psl[9]) % 2 == 0):
        return 'K'
    return 'M'

#**********************************************
#   nazwa funkcji: sprawdzSume
#   opis funkcji: sprawdza czy suma danego peselu jest poprawna
#   parametry: pesel
#   zwracany typ i opis: boolean - zwraca true jezeli suma jest poprawna, false gdy nie jest
#   autor: 12345678910
#***********************************************

def sprawdzSume(psl):
    wagi = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    S=0
    c=0
    for i in psl:
        if(c < 10):
            S+=(int(i) * wagi[c])
            c+=1

    M=S%10

    if(M==0):
        R = 0
    else:
        R = 10-M

    return R == int(psl[10])

PSL = "55030101193"

PSL = input("Podaj pesel: ")

if (sprawdzPlec(PSL) == 'K'):
    print("Kobieta")

elif(sprawdzPlec(PSL) == 'M'):
    print("Mezczyzna")



if(sprawdzSume(PSL)):
    print("PESEL poprawny")

else:
    print("PESEL niepoprawny")

