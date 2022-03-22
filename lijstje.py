import time
# Dit zijn alle variabelen.
vraag1 = input("wat wil je doen? (toevogen/bekijken)")
while vraag1 == "toevoegen":
    lijstje_bestand = open("lijstje", "a")
    lijstje_bestand.write(input("Wat heb je vandaag gekocht? "))
    lijstje_bestand.write(" ")
    lijstje_bestand.write(input("Hoeveel heeft dat gekost? "))
    lijstje_bestand.write(" euro")
    lijstje_bestand.write("\n")
    vraag = input("Heb je nog iets gekocht?(ja/nee) ")

    # Dit is de loop waar de vragen worden gesteld.
    if vraag == "ja":
        lijstje_bestand.write(input("Wat heb je dan nog gekocht? "))
        lijstje_bestand.write(" ")
        lijstje_bestand.write(input("Hoeveel heeft dat gekost? "))
        lijstje_bestand.write(" euro")
        lijstje_bestand.write("\n")
        vraag = input("Heb je nog iets gekocht?(ja/nee) ")
    if vraag == "nee":
        break
    else:
        foutmelding = input("Wat bedoel je? ")
        while foutmelding == "ja":
                lijstje_bestand.write(input("Wat heb je vandaag gekocht? "))
                lijstje_bestand.write(" ")
                lijstje_bestand.write(input("Hoeveel heeft dat gekost? "))
                lijstje_bestand.write(" euro")
                lijstje_bestand.write("\n")
                vraag = input("Heb je nog iets gekocht?(ja/nee) ")
                while vraag == "ja":
                    lijstje_bestand.write(input("Wat heb je dan nog gekocht? "))
                    lijstje_bestand.write(" ")
                    lijstje_bestand.write(input("Hoeveel heeft dat gekost? "))
                    lijstje_bestand.write(" euro")
                    lijstje_bestand.write("\n")
                    vraag = input("Heb je nog iets gekocht?(ja/nee) ")
                while vraag == "nee":
                    break
        while foutmelding == "nee":
            break

    lijstje_bestand.close()

if vraag1 == "bekijken":
    time.sleep(1)
    lijstje_bestand = open("lijstje", "r")
    print(lijstje_bestand.read())
    lijstje_bestand.close
if vraag1 == "verwijderen":
    lijstje_bestand= open("lijstje", "a")
    