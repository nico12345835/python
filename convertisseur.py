print("bienvenu dans le convertisseur d'unités")
unité = input("que voulez vous convertir? (kilomètres, degrés, euro)")
while unité not in ["kilomètres", "degrés", "euro"]:
    print("veuillez répondre par kilomètres, degrés ou euro")
    unité = input("que voulez vous convertir? (kilomètres, degrés, euro)")


def kilomètrestomiles():
    kilomètres=input("combiens de kilomètres voulez vous convertir en miles ?")
    kilomètres=float(kilomètres)
    miles=kilomètres/1.6093445
    miles=float(miles)
    print(f"{kilomètres} kilomètres = {miles} miles")

def degréstofahrenheit():
    degrés=input("combien de degrés voulez vous convertir en fahrenheit ?")
    degrés=float(degrés)
    fahrenheit=degrés*9/5+32
    fahrenheit=float(fahrenheit)
    print(f"{degrés} degrés = {fahrenheit} fahrenheit")

def eurotodollar():
    euro=input("combien d'euro voulez vous convertir en dollar ?")
    euro=float(euro)
    dollar=euro*1.1464
    dollar=float(dollar)
    print(f"{euro} euro = {dollar} dollar")

if unité == "kilomètres":
    kilomètrestomiles()

elif unité == "degrés":
    degréstofahrenheit()

elif unité == "euro":
    eurotodollar()


