tallene = [12, 16, 5, 16]
innenfor = True
indeks = 0
while indeks<len(tallene):
    if tallene[indeks]<=10 or tallene[indeks]>=20:
        innenfor = False
    indeks +=1
assert innenfor==False
