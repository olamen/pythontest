def readfill():
  f = open("concours.txt", "r")
  pr_ad = 0
  for ligne in f:
      L = ligne.strip(";")
      if L[4] != "ajourne(e)":
         pr_ad = pr_ad + 1
  print(pr_ad)


readfill()