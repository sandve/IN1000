innlest_ord = []

while len(innlest_ord)<5:
    nytt_ord = input("Skriv inn ord! ")
    innlest_ord.append(nytt_ord)
print("***")
indeks=0
while indeks<len(innlest_ord):
    svar = input("Hva var ord " + str(indeks) + "? ")
    if svar == innlest_ord[indeks]:
        print("Riktig")
    else:
        print("Galt")
    indeks +=1
