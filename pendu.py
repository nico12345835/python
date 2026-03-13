mot="anniversaire"
list_lettres_mot=[]
for lettre in mot:
    if lettre not in list_lettres_mot:
        list_lettres_mot.append(lettre)
tentatives_autorisees=len(list_lettres_mot)+3
    
list_propositions=[]
for i in range(10):
    for lettre in mot:
        if lettre in list_propositions :
            print( lettre,end="")
        else:
            print(" _",end="")
    print("")
    proposition=input("Faites une proposition de lettre ")
    list_propositions.append(proposition)
    if len(proposition)>1:
        if proposition==mot:
            print("tiéé un tigre")
    if set(list_propositions).intersection(set(list_lettres_mot))==set(list_lettres_mot):
        print("tiééé un tigre")
        print(f"le mot etait bien : {mot}")
        break
    