
def statistiques(dec):
    fichier = open("concours.txt")
    L = fichier.readlines()
    fichier.close()
    L1 = []  # candidats admis
    L2 = []  # candidats refuses
    L3 = []  # candidats ajournes
    for ligne in L:
        L = ligne.split(";")
        if L[4].strip() == "admis(e)":
            L1.append(ligne)
        elif L[4].strip() == "refuse(e)":
            L2.append(ligne)
        else:
            L3.append(ligne)
    if dec == "admis":
        return (len(L1) / len(L)) * 100
    elif dec == "refuse":
        return (len(L2) / len(L)) * 100
    else:
        return (len(L3) / len(L)) * 100


def supprimer():
    fichier = open("admis.txt")
    candidat = []  # contient les candidats restants
    for ligne in fichier:
        L = ligne.split(";")
        if int(L[3]) < 30:
            candidat.append(ligne)
    fichier.close()
    # reecrire la nouvelle liste
    fichier = open("admis.txt", "w")
    fichier.writelines(candidat)
    fichier.close()


statistiques("refuse")