from random import randint
antall_trekk = 0
store = 0

while antall_trekk<100000:
    antall_trekk +=1
    t1 = randint(1,6)
    t2 = randint(1,6)
    if t1+t2 >= 10:
        store += 1

print(store/antall_trekk)
