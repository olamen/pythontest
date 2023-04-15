etudiants = {"etudiant_1": 13, "etudiant_2": 17, "etudiant_3": 9, "etudiant_4": 15,
             "etudiant_5": 8, "etudiant_6": 14, "etudiant_7": 16, "etudiant_8": 12,
             "etudiant_9": 13, "etudiant_10": 15, "etudiant_11": 14, "etudiant_112": 9,
             "etudiant_13": 10, "etudiant_14": 12, "etudiant_15": 13, "etudiant_16": 7,
             "etudiant_17": 12, "etudiant_18": 15, "etudiant_19": 9, "etudiant_20": 17, }

etudiantAdmis = dict({})
etudiantNonAdmis = dict({})

for k, v in etudiants.items():
    if v < 10:
        etudiantNonAdmis[k] = v
    else:
        etudiantAdmis[k] = v

print("Les etudiants admis : ", etudiantAdmis)
print("Les etudiants non admis : ", etudiantNonAdmis)
