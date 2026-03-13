mot="anniversaire"
list_propositions=[]
list_lettres_mot = list(mot)
for i in range(12):
    for lettre in mot:
        if lettre in list_propositions :
            print(lettre,end="")
        else:
            print( "_",end="")
    print("")
    if set(list_lettres_mot).intersection(set(list_propositions)) == set(list_lettres_mot):
        print("Bravo ! Vous avez trouvé le mot :", mot)
        break
    proposition=input("faites une proposition")
    list_propositions.append(proposition)
   
