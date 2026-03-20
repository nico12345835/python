import random 


recommencer=True
while recommencer :
    nombre_inconnu=random.randint(1,20)
    proposition=int()
    while proposition != nombre_inconnu :
        proposition=input("faites une proposition!")
        proposition=int(proposition)
        
        if proposition==nombre_inconnu:
            print("tiéééééééé un tigre")
            recommencer=input("voulez vous recommencer (o/n)?")
            while recommencer not in ["o","n"]:
                print("veuillez repondre par oui(o) ou non (n)")
                recommencer=input("voulez vous recommencer (o/n)?")
            if recommencer=="o" : recommencer=True
            else : recommencer=False
            
        elif proposition<nombre_inconnu:
            print("le nombre recherché est plus grand")
        elif proposition>nombre_inconnu:
            print("le nombre recherché est plus petit")
    
