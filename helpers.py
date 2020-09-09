elemendid = []

# lisame ELEMENT juurde

def lisa_element(nimetus,hind,kogus):
    global elemendid
    nimetused = []
    for element in elemendid:
        if nimetus in element.values():
            nimetused.append(nimetus)
    if nimetus in nimetused:
        print("Element {} on juba olemas".format(nimetus))
    else:
        elemendid.append({"nimetus": nimetus, "hind": hind, "kogus": kogus})

# lisame ELEMENDID KORRAGA juurde
def lisa_elemendid(elementide_nimekiri):
    global elemendid
    elemendid = elementide_nimekiri

#loeme elemendid korraga
def loe elemendid():

def main():
    # teeme katseandemstik
    katse_elemendid = [
        {"nimetus": "leib", "hind": 0.80, "kogus": 20},
        {"nimetus": "piim", "hind": 0.50, "kogus": 15},
        {"nimetus": "vein", "hind": 5.60, "kogus": 5},
    ]

    # testime elementide lisamist
    lisa_elemendid(katse_elemendid)
    lisa_elemendid(elemendid)


    # testime üksiku elemendi lisamist

    lisa_element("kohupiim", 0.6, 15)


    lisa_element("leib", 0.8, 5)

# käivitamine
if __name__ == "__main__":
    main()

