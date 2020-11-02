dagsregn = {}
for linje in open("regn.csv"):
	biter = linje.split()
	dato = biter[0]
	regn = float(biter[1])
	dagsregn[dato] = regn

dagssok = {}
for linje in open("trends.csv"):
	biter = linje.split()
	dato = biter[0]
	score = int(biter[1])
	dagssok[dato] = score

assert dagsregn.keys() == dagssok.keys()
datoer = dagsregn.keys()

for dato in datoer:
	print(dato, dagsregn[dato], dagssok[dato])
