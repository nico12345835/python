def menu():
    print("pour calculer l'aire d'un carré, tapez 1")
    print("pour calculer l'aire d'un triangle, tapez 2")
    print("pour calculer l'aire d'un cercle Bruges, tapez 3")
    print("pour quitter tapez 0")

    choix=input("votre choix: ")
    choix=int(choix)

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
    hauteur=input("quel est la base du triangle")
    hauteur=float(base)
    aire=base*hauteur/2
    print(f"l'aire du triangle vaut : {aire}")

if __name__=="__main__":
    menu()