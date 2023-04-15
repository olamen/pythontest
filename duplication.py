def dupli(a):
    b = []
    for x in a:
        if a.count(x) > 1 and x not in b:
            b.append(x)
    return b


a = [1, 6, 7, 9, 5, 6, 9, 0, 1, 0, 5]
print("les element diplique sont :", dupli(a))
