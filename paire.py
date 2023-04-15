#somme des valeur paire
def somepaire(S):
    long = len(S)
    somme =0
    for x in range (long):
        if S[x]%2!=0:
          somme= S[x]+somme
        else:
          somme= somme
    print("La somme des nombre impaire est:",somme)
    return S
S=[2,3,5,6,7,8,13,12]
print(somepaire(S))
