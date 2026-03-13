mot="anniversaire"
list_lettres_mot=[]

#on definit la liste de lettres du mot
for lettre in mot:
    if lettre not in list_lettres_mot:
        list_lettres_mot.append(lettre)
tentatives_autorisees=len(list_lettres_mot)+3

tentatives=0
    
list_propositions=[]
for i in range(tentatives_autorisees):
    for lettre in mot:
        if lettre in list_propositions :
            print( lettre,end="")
        else:
            print(" _",end="")
    print("")
    proposition=input("Faites une proposition de lettre ")
    list_propositions.append(proposition)
    tentatives+=1
    print(f" il vous reste {tentatives_autorisees-tentatives} tentatives")

#le joueur a trouvé le mot en proposant plusieur lettres a la fois
    if len(proposition)>1:
        if proposition==mot:
            print("tiéé un tigre")
            print(f"le mot etait bien : {mot}")
            break
#le joueur a trouvé toutes les lettres    
    if set(list_propositions).intersection(set(list_lettres_mot))==set(list_lettres_mot):
        print("tiééé un tigre")
        print(f"le mot etait bien : {mot}")
        break
    
    
