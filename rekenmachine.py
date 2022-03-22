#functie
def functie_bewerkingen():
    # Variabelen
    getal_1 = int(input("wat is je eerste getal? "))
    bewerking = input("welke bewerking wil je maken? ")
    getal_2 = int(input("wat is je tweede getal? "))
    # If-eliffunctie's (loops)
    if bewerking == "-":
        print(getal_1 -getal_2)
    elif bewerking == "+":
        print(getal_1+getal_2)
    elif bewerking == "*":
        print(getal_1*getal_2)
    elif bewerking == "/":
        print(getal_1/getal_2)
    elif bewerking == "**":
        print(getal_1**getal_2)
    elif bewerking == "min":
        print(getal_1-getal_2)
    elif bewerking == "plus":
        print(getal_1+getal_2)
    elif bewerking == "maal":
        print(getal_1*getal_2)
    elif bewerking == "delen":
        print(getal_1/getal_2)
    elif bewerking == "macht":
        print(getal_1**getal_2)
    else:
        foutmelding = input("Wat bedoel je? ")
        if foutmelding == "-":
            print(getal_1 - getal_2)
        elif foutmelding == "+":
            print(getal_1 + getal_2)
        elif foutmelding == "*":
            print(getal_1 * getal_2)
        elif foutmelding == "/":
            print(getal_1 / getal_2)
        elif foutmelding == "**":
            print(getal_1 ** getal_2)
        elif foutmelding == "min":
            print(getal_1 - getal_2)
        elif foutmelding == "plus":
            print(getal_1 + getal_2)
        elif foutmelding == "maal":
            print(getal_1 * getal_2)
        elif foutmelding == "delen":
            print(getal_1 / getal_2)
        elif foutmelding == "macht":
            print(getal_1 ** getal_2)

functie_bewerkingen()
vraag = input("Wil je nog iets uitreken? ")
if vraag == "ja":
    #oproep functie
    functie_bewerkingen()
    vraag = input("Wil je nog iets uitreken? ")
while vraag == "nee":
    break