def pris(gratis, alder):
    if gratis:
        svar = 0
    elif alder < 18:
        svar = 100
    else:
        svar = 200

    return svar

assert pris(False, 5)==100
assert pris(False, 50)==200
assert pris(True, 5)==0
assert pris(True, 50)==0
