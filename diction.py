dicPC={"HP": 11, "Acer": 7, "Lenovo": 17, "Del": 23}
dicPhone={"Sumsung": 22, "Iphone": 9, "Other": 13}
dicTablette = {"Sumsung1": 15, "Other": 13}
dicPC.update(dicPhone)
dicPC.update(dicTablette)
print("le nouveaux dictionnaire est :")
print(dicPC)

# dexieme methode
def merge(dic1, dic2, dic3):
    dic = dic1 | dic2 | dic3
    return  dic


dic = merge(dicPC, dicPhone, dicTablette)
print("le nouveaux dictionnaire est :")
print(dic)