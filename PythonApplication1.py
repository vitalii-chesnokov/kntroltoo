# #Valik 1
# #Ülesanne 5
# a=int(input("Sisestage arv A"))
# b=int(("Sisestage arv B"))
# a.spam()
# b.eggs()
# if a>b:
#     k=b-a
#     s=sum(k)
#     print("Seeriate summa",s)
# else b >a:
#     z=a-b
#     l=sum(k)
#     print("Seeriate summa",l)
   
#5/ Пытался что-то сделать, пока не получилось до конца

#Valik 1
#Ülesanne 4
n = int(input("Sisestage naturaalarv: "))
n = str(n)
even_count = 0
odd_count = 0
for digit in n:
    digit_int = int(digit)
    if digit_int % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print(f"Paarisarvud: {even_count}, Paaritud arvud: {odd_count}")



#Valik 1
#Ülesanne 3
N = int(input("Sisestage numbrite arv: "))
count_positive = -1 #Использовал функцию count_positive()
for count_positive in range(N):
    num = float(input("Sisestage arv: "))
    if num > 0:
        count_positive += 1
print(f"Positiivsede arvude arv: {count_positive}")



#Valik 1
#Ülesanne 2
R = int(input("Sisestage arv: "))
tl = 1
for R in range(R + 1):
    if R % 2 != 0:
        tl *= R
print(f"Lisamine tulemus {R}: {tl}")


#Valik 1
#Ülesanne 1
n=int(input("Sisestage arv vahemikus 1 kuni 9: "))
if n<10:
    for i in range(n):
        print("/V\".center(15," "))
        print("/ V \".center(15," "))
        print("/ V V \".center(15," "))
        print("/VV V VV\".center(15," "))
else:
    print(Viga!)
















#######
#Valik 7
#Ülesanne 2
s = [14, 20] #sõprade võimalik vanus  
k = 0  #Kui palju sõpru sai õhtusööki
for i in (s):
    if i >= 16:
        k += 1
        print(f"Sõprade arv, kes said õhtusöögi: {k}")



##Valik 7
##Ülesanne 1
#n=int(input("Sisestage arv vahemikus 1 kuni 9: "))
#if n < 10:
#    for i in range(n):
#        print("^".center(15," "))
#        print("/ /".centetr(15," "))
#        print("\ \".center(15," "))
#        print("/ /__".center(15," "))
#else:
#    print(Viga!) 


