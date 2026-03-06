mot="anniversaire"
list_propositions=[]
for i in range(5):
    for lettre in mot:
        if lettre in list_propositions :
            print(lettre,end="")
        else:
            print( "_",end="")
    print("")
    proposition=input("faites une proposition")
    list_propositions.append(proposition)