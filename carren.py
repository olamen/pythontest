a = int(input("entre en entier :"))
dic = dict({})
for i in range(1, (a+1)):
    dic[i] = i*i
print("le dictionnair carre de "+str(a)+" est de :")
print(dic)

