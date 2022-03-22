import random 

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456"
def paswoord_generator():
    paswoord_lengte = int(input("Hoe lang wil je dat je passwoord wordt: "))
    passwoord_count = int(input("Hoe veel passwoorden wil je hebben: "))
    for x in range(0,passwoord_count):
        paswoord = ""
        for x in range(0,paswoord_lengte):
            paswoord_chars = random.choice(chars)
            paswoord       = paswoord + paswoord_chars
        if passwoord_count >1 :
            print("Hier zijn jouw paswoorden: ", paswoord)
        elif passwoord_count <1000:
            print("Hier is jouw paswoord:",paswoord)

paswoord_generator()
vraag = input("Wil je nog een paswoord maken? ")
while vraag == "ja":
    paswoord_generator()
    vraag = input("Wil je nog een paswoord maken? ")
while vraag == "nee":
    break