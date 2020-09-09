elemendid = []

# lisame ELEMENT juurde

def lisa_element(nimetus,hind,kogus):
    global elemendid
    elemendid.append({"nimetus": nimetus, "hind": hind, "kogus": kogus})

# lisame ELEMENDID KORRAGA juurde
def lisa_elemendid(elementide_nimekiri):
    global elemendid
    elemendid = elementide_nimekiri

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
    print(katse_elemendid)
    print("-----------")

    # testime üksiku elemendi lisamist

    lisa_element("kohupiim", 0.6, 15)
    print(elemendid)

# käivitamine
if __name__ == "__main__":
    main()
