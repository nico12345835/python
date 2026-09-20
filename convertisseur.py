#demander à l'utilisateur quelle unité il veut convertir
def demander_choix(message, choix_possibles):
    choix=input(message)

    while choix not in choix_possibles:
        print("choix invalide")
        choix=input(message)

    return choix

#demander à l'utilisateur la quantité de ce qu'il veut convertir
def demander_valeur(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("erreur: entre un nombre valide")
        

historique=[]
#faire la conversion
def convertir(valeur, facteur, unité_départ, unité_arrivé):
    resultat = round(valeur * facteur, 2)
    conversion = (f"{valeur} {unité_départ} = {resultat} {unité_arrivé}")
    historique.append(conversion)
    print(conversion)
    print("historique", historique)


facteurs_kilometres = {
    "miles": 1 / 1.6093445,
    "mètres": 1000
}

facteurs_euro = {
    "dollar": 1.15,
    "livre": 0.86
}

facteurs_kilogrammes = {
    "grammes":1000,
    "livre":2.20462262
}

print("bienvenu dans le convertisseur d'unités")
while True:
    unité = demander_choix("que voulez vous convertir?(kilomètres, kilogrammes, euro ou quitter)", ["kilomètres", "kilogrammes", "euro", "quitter"])
    if unité == "quitter":
        print("au revoir")
        break

    elif unité == "kilomètres":
        unitésecondaire = demander_choix("en quoi voulez vous converir? (mètres, miles)", ["mètres", "miles"])
        kilomètres = demander_valeur("Combien de kilomètres ?")
        facteur = facteurs_kilometres[unitésecondaire]
        convertir(kilomètres, facteur, "kilomètres", unitésecondaire)
        
    elif unité == "euro":
        unitésecondaire = demander_choix("en quoi voulez-vous convertir ? (dollar, livre)", ["dollar", "livre"])
        euro = demander_valeur("combien d'euro ?")
        facteur = facteurs_euro[unitésecondaire]
        convertir(euro, facteur, "euro", unitésecondaire)

    elif unité == "kilogrammes":
        unitésecondaire = demander_choix("en quoi voulez-vous convertir ? (grammes, livre)", ["grammes", "livre"])
        kilogrammes = demander_valeur("combien de kilogrammes ?")
        facteur = facteurs_kilogrammes[unitésecondaire]
        convertir(kilogrammes, facteur, "kilogrammes", unitésecondaire)
        



