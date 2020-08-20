voksen = input("Er du voksen? (ja/nei)")
gravid = input("Er du gravid? (ja/nei)")

if voksen=="ja":
    print "Du er stor nok"
    if gravid=="ja":
        print "men har dessverre ikke lov"
    else:
        print "velkommen ombord!"
