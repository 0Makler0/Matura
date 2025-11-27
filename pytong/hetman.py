plik = open("szachownice.txt", "r")
dane = plik.readlines()
print(dane)




#ZADANIE 1

#  0  1  2  3  4  5  6  7
#  8  9 10 11 12 13 14 15
# 16 17 18 19 20 21 22 23
# 24 25 26 27 28 29 30 31
# 32 33 34 35 36 37 38 39
# 40 41 42 43 44 45 46 47
# 48 49 50 51 52 53 54 55
# 56 57 58 59 60 61 62 63

#potrzebne przedziały
# [0-7] po kolei
# [7-64] po 8
# [0-56] po 8
# [56 - 64] po kolei
lista = [0 , 1,  2  ,3  ,4 , 5 , 6 , 7,15,23,31,39,47,55,63,56 ,57, 58, 59, 60, 61, 62,8,16, 24,32,40,48,]


#print(dane[0].index("H"))
x = 0
obrzerza = 0
for i in dane:
    if dane[x].index("H") in lista:
        obrzerza +=1
        x +=1
    else:
        x +=1
print(obrzerza)




