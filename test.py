def saisir():
    new = "O"  # O -> oui ; N -> non
    fichier = open("concours.txt", "a")
    decision = {"a": "admis(e)", "r": "refuse(e)", "aj": "ajourne(e)"}
    while new == "O":
        cin = input("Saisir le Numero CIN : ")
        nom = input("Saisir le Nom : ")
        prenom = input("Saisir le prenom : ")
        age = input("saisir l age ")
        dec = input("saisir la decision a(admis(e))r(refuse(e)) aj(ajourne(e)): ")
        ligne = cin + ";" + nom + ";" + prenom + ";" + age + ";" + decision[dec] + "\n"
        fichier.write(ligne)
        new = input("Saisir un nouveau candidat, (O / N) ?")
    fichier.close()



def admis():
    fichier = open("concours.txt")
    dest = open("admis.txt", "a")
    for ligne in fichier:
        L = ligne.split(";")
        if L[4].strip() == "admis(e)":
            print(L)
            dest.write(ligne)
    fichier.close()
    dest.close()


def admismn30():
    fichier = open("admis.txt")
    destf = open("admismn30.txt", "a")
    lign = "cin;nom;prenom;age;decision" + "\n"
    destf.write(lign)
    for ligne in fichier:
        L = ligne.split(";")
        if int(L[3]) <= 30:
            destf.write(ligne)
    fichier.close()
    destf.close()


# plus de 30 ans
def attent():
    fichier = open("concours.txt")
    dest = open("attent.txt", "a")
    lign = "cin;nom;prenom" + "\n"
    dest.write(lign)
    for ligne in fichier:
        L = ligne.split(";")
        if int(L[3]) >= 30 and L[4].strip() == "admis(e)":
            ligne = L[0] + ";" + L[1] + ";" + L[2] + "\n"
            dest.write(ligne)
    fichier.close()
    dest.close()


# pourcentage
def dec():
    fichier = open("admismn30.txt","r")
    L = fichier.readline()
    fichier.close()
    admin = []
    ref = []
    aj = []
    for ligne in L:
        L = ligne.split(";")
        print(L[4])
    print("le porcentage des admin est:", len(L))


dec()





