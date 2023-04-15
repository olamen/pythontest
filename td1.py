def echangList(L):
       # on garde le dernieur valeur
   dernieur = L[-1]
   #remplace le dernier element
   L[-1] = L[0]
  # remplce le premier elemt
   L[0]= dernieur
   return L
   
L=["Pyton","Java","Math","Anglais"]
print(echangList(L))


        