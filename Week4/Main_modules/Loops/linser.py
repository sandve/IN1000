import random
boks = ["v", "v", "h", "h"]
antall_trekk = 0
antall_suksess = 0

while antall_trekk<100000:
    antall_trekk += 1
    random.shuffle(boks)
    linse1 = boks[0]
    linse2 = boks[1]

    if (linse1 != linse2):
        antall_suksess += 1
print("Suksessrate: ", 100*antall_suksess/antall_trekk, "%")
