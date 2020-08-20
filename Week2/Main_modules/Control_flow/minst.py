innlest1 = input("Skriv tall 1: ")
tall1 = int(innlest1)
innlest2 = input("Skriv tall 1: ")
tall2 = int(innlest2)
if tall1<tall2:
    minst = tall1
else:
    minst = tall2

assert minst <= tall1
assert minst <= tall2
print(minst)
