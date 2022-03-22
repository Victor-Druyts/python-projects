import time
versie = input("Welke versie wil je spelen? Die met lievelings dingen of die met dingen die je haat. Antwoord met lievelings of haat. ")
def madlips_lievelings():
    #versie lievelings
    if versie == "lievelings":
        #variabelen
        dier = input("Wat is je lievelings dier? ")
        getal = input("Wat is je lievelings getal? ")
        kleur = input("Wat is je lievelings kleur? ")
        if getal == "1":
            if dier == ("mens"):
                zin = "Jij bent een {} met {} been die {} ziet."
                print(zin.format(dier, getal, kleur))
            elif dier == ("paard"):
                zin = "Jij bent een {} met {} been die {} ziet."
                print(zin.format(dier, getal, kleur))

            else:
                zin = "Jij bent een {} met {} poot die {} ziet."
                print(zin.format(dier, getal, kleur))
        else:
            zin = "Jij bent een {} met {} poten die {} ziet."
            print(zin.format(dier, getal, kleur))
        time.sleep(2)

def madlips_haat():
    #versie haat
    if versie == "haat":
        #variabelen
        dier_haat = input("welk dier haat je? ")
        getal_haat = input("welke getal haat je? ")
        kleur_haat = input("welke kleur haat je? ")   
        if getal_haat == "1":
            if dier_haat == ("mens"):
                zin = "Jij bent een {} met {} been die {} ziet."
                print(zin.format(dier_haat, getal_haat, kleur_haat))
            elif dier_haat == ("paard"):
                zin = "Jij bent een {} met {} been die {} ziet."
                print(zin.format(dier_haat, getal_haat, kleur_haat))
            else:
                zin = "Jij bent een {} met {} poot die {} ziet."
                print(zin.format(dier_haat, getal_haat, kleur_haat))
        else:
            zin = "Jij bent een {} met {} poten die {} ziet."
            print(zin.format(dier_haat, getal_haat, kleur_haat))
        time.sleep(2)
    
madlips_lievelings()
vraag = input("Wil je nog eens spelen (ja/nee)? ")
while vraag == "ja":
    madlips_lievelings()
    vraag = input("Wil je nog eens spelen (ja/nee)? ")
while vraag == "nee":
    break

madlips_haat()
vraag = input("Wil je nog eens spelen (ja/nee)? ")
while vraag == "ja":
        madlips_haat()
        vraag = input("Wil je nog eens spelen (ja/nee)? ")
while vraag == "nee":
        break