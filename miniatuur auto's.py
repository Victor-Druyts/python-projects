vraag = input("Wat wil je doen. Je lijst bekijken of iets toevoegen? ")

def toevoegen():   
    miniatuurautos_bestand = open("miniatuurautos", "a")
    miniatuurautos_bestand.write(input("Welke auto heb je gekocht? "))
    miniatuurautos_bestand.write("\n")
    miniatuurautos_bestand.close
              
    vraag2 = input("Wil je nog iets toevoegen? ")
    while vraag2 == "ja":
        miniatuurautos_bestand = open("miniatuurautos", "a")
        miniatuurautos_bestand.write(input("Welke auto heb je gekocht? "))
        miniatuurautos_bestand.write("\n")
        miniatuurautos_bestand.close
        vraag2 = input("Wil je nog iets toevoegen? ")
    while vraag2 == "nee":
        break
    else:
        foutmelding = input("Wat bedoel je? ")
        while foutmelding == "ja":
                miniatuurautos_bestand = open("miniatuurautos", "a")
                miniatuurautos_bestand.write(input("Welke auto heb je gekocht? "))
                miniatuurautos_bestand.write("\n")
                miniatuurautos_bestand.close
                vraag2 = input("Wil je nog iets toevoegen? ")
                while vraag2 == "ja":
                    miniatuurautos_bestand = open("miniatuurautos", "a")
                    miniatuurautos_bestand.write(input("Welke auto heb je gekocht? "))
                    miniatuurautos_bestand.write("\n")
                    miniatuurautos_bestand.close
                    vraag2 = input("Wil je nog iets toevoegen? ")
        while foutmelding == "nee":
            break


def bekijken():
    miniatuurautos_bestand = open("miniatuurautos", "r")
    print(miniatuurautos_bestand.read())
    miniatuurautos_bestand.close


if vraag == "toevoegen":
    toevoegen()
elif vraag == "bekijken":
    bekijken()
else:
    foutmelding = input("Wat bedoel je? ")
    while foutmelding == "toevoegen":
        toevoegen()
    if foutmelding == "bekijken":
        bekijken()