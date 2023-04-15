'''fichier = open("text22.txt",'rt')
texte = fichier.read()
print(texte)
lignes = fichier.readlines()
print(lignes)
fichier.close()
fichier = open("texte22.txt",'wt')
fichier.write("mollis sem id tellus auctor hendrerit.")
fichier.close()



def Affichage():
    nbF=0
    nbH=0
    fichier = open("list.txt")
    for ligne in fichier :
        L = ligne.split(":")
        if L[1].strip() == "F":
            nbF = nbF + 1
        if L[1].strip() == "M":
            nbH = nbH + 1
    print("  "+str(nbF)+"   "+str(nbH))
    fichier.close()
Affichage()'''

def Separation(): 
    fichier = open("list.txt")
    f1 = open('Homme.txt','x')
    f2 = open('Femme.txt', 'x')
    for ligne in fichier:
        L = ligne.split(":")
        if L[1].strip()  == 'M' :
            enreg = L[2] + ";" + L[3] + ";" + L[4] + "\n"
            f1.write(enreg)
        elif L[1].strip()  == 'F':
            enreg = L[2] + ";" + L[3] + ";" + L[4] + "\n"
            f2.write(enreg)
    fichier.close()
    f1.close()
    f2.close()
Separation()
