print("bienvenue dans notre restaurant")
print("pour un hamburger, tapez 1")
print("Pour une pizza, tapez 2")
print("Pour une salade, tapez 3")

choix=input("quel est votre choix?")
choix=int(choix)
while choix not in [ 1,2,3]:
    print("Veuillez répondre par 1, 2 ou 3")
    choix=input("quel est votre choix?")
    choix=int(choix)
if choix==1:
    print("Vous avez choisi : hamburger")
elif choix==2:
    print("Vous avez choisi : pizza")
elif choix==3:
    print("Vous avez choisi : salade")
