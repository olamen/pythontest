#les multiple de 3
def multi3(M):
    long = len(M)
    i = 0
    for x in range(long):
     if M[x]%3 ==0:
        print(M[x])
        i=i+1
     else:
       i=i
    print("le nombre des multiples de trois est de :",i)
    return M
       
       
M=[5,6,9,12,11,15,16,17]
print(multi3(M))