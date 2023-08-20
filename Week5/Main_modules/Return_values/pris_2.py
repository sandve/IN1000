def pris(gratis, alder):
    if gratis:
        return 0
    elif alder < 18:
        return 100
    else:
        return 200

assert pris(False, 5)==100
assert pris(False, 50)==200
assert pris(True, 5)==0
assert pris(True, 50)==0
