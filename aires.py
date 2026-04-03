from math import pi
def menu():
    print("pour calculer l'aire d'un carré, tapez 1")
    print("pour calculer l'aire d'un triangle, tapez 2")
    print("pour calculer l'aire d'un cercle Bruges, tapez 3")
    print("pour quitter tapez 0")
    choix=input("votre choix: ")

    valid=False 
    while not valid:
        try:
            choix=int(choix)
            if choix in[0,1,2,3]:
                valid=True
            else:
                raise 
        except:
            print("veuillez repondre par 0 1 2 ou 3")
            choix=input("votre choix: ")
    if choix==1:
        aire_carre()
    elif choix==2:
        aire_triangle()
    elif choix==3:
        aire_cercle()
    elif choix==0:
        quit()

def quit():
    print("au revoir")
    
def aire_carre():
    cote=input("quel est la longeur du coté de votre carrée?")
    cote=float(cote)
    aire=cote**2
    print(f"l'aire du carré vaut : {aire}")

def aire_triangle():
    base=input("quel est la base du triangle")
    base=float(base)
    hauteur=input("quel est la hauteur du triangle")
    hauteur=float(base)
    aire=base*hauteur/2
    print(f"l'aire du triangle vaut : {round(aire,4)}")

def aire_cercle():
    rayon=input("quelle est la longeur du rayon?")
    rayon=float(rayon)
    aire=pi*rayon**2
    print(f"l'aire du cercle vaut {round(aire,4)}")

if __name__=="__main__":
    menu()


