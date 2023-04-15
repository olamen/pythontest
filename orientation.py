def saisir():
    new = "O"  # O -> oui ; N -> non
    fichier = open("etudiant.txt", "a")
    genre = {"h": "homme", "f": "femme"}
    while new == "O":
        id = input("Saisir id : ")
        math = float(input("Saisir la note du math : "))
        pc = float(input("Saisir la note du pc : "))
        sn = float(input("saisir la note du sn "))
        gr = input("saisir la genre h homme f femme")
        mo = float((math*6+pc*5+sn*4)/15)
        ligne = id + ":" + str(math) + ":" + str(pc) + ":" + str(sn)+":" + genre[gr]+":"+str(mo)+"\n"
        fichier.write(ligne)
        new = input("Saisir un nouveau etudiant, (O / N) ?")
    fichier.close()
saisir()