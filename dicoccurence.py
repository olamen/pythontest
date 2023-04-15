chaine = input("saisire la chaine des caracters")
d= dict({})

for i in chaine:
    d[i] = chaine.count(i)
print(d)