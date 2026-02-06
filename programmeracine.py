from math import sqrt #on importe le module permettant de calculer des racines carrées

print("Bonjour et bienvenue dans ce programme de calcul des racines d'une fonction du deuxième degré.")#on affiche un message de bienvenue
print("Dans l'équation y=ax²+bx+c,")#on précise le contexte et le nom des variables

a=input("Quelle est la valeur de a? ")#on récupère la valeur de a et on la stocke dans la variable a
b=input("Quelle est la valeur de b? ")#même chose pour b
c=input("Quelle est la valeur de c? ")#même chose pour c

a=float(a) #on converti en un nombre décimal
b=float(b) #même chose
c=float(c) #même chose

#################################
#continue le code à partir d'ici#
#################################
delta=b**2-4*a*c
if delta <0:
	    print("il n'y a pas de racines a la fonction")
elif delta==0:
        x=(-b)/(2*a)
        print("il y a une racine a cette fonction")
        print(f"sa valeur est de: x={round (x,4)}")
elif delta > 0:
        x1=(-b-sqrt(delta))/(2*a)
        x2=(-b+sqrt(delta))/(2*a)
        x1=round(x1 , 5)
        x2=round(x2 , 5)
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")


