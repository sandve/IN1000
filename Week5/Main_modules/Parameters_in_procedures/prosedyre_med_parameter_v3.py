def skrivAlder(alder):
    if alder > 6:
        print("Velkommen til mitt program");
    else:
        print("Gaa heller ut og lek i skogen");

innlest = int(input("Hvor gammel er du? "))
skrivAlder(innlest)

print("Hacket av en toaaring: ")
skrivAlder(2)
print("Hacket av en attenaaring: ")
skrivAlder(18)
