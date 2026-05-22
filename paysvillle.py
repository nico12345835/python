#est-ce que j'ai pas raison ? Oui tu as raison, ANDERLECHT ANDERLECHT ANDERLECHT champion !! Allez Allez Allez Allez we are the champions we are the champions allez allez allez allez we are the champions 
#j'ai été voir jouer une autre équipe la semaine dernière (STANDARD) il n'y avait pas un chat et le parking était désert (standard) je me suis dit je me suis trompé de date ou bien d'horraire pourtant en face de moi y'a trois gichets qui sont ouvert à l'un des trois gichets j'ai dit et alors quelle nouvelle 
#le match est-il remis au lundi de pâque ou à noel le type en face de moi a dit ne t'énerve pas mon vieux comme t'es venu tout seul on commence à l'heure que tu veux 
#est-ce que j'ai pas raison ? Oui tu as raison, ANDERLECHT ANDERLECHT ANDERLECHT champion !! Allez Allez Allez Allez we are the champions we are the champions allez allez allez allez we are the champions 

#import 
import string
import random

#les fonctions
def choose_lettre ():
    alphabet=string.ascii_lowercase
    alphabet_list=list(alphabet)
    lettre=random.choice(alphabet_list)
    return lettre
def gen_users_list():
    users_list=[]
    user="__"
    while user!="":
        user=input("quel est le nom du nouv joueur? laissez vide pour terminer")
        if user !="":
            users_list.append(user)
    return users_list

def gen_categories():
    list_categories=["pays","ville","animal","fruit"]
    return list_categories

def new_game(lettre,user_list,list_categories):
    print(f"nous jouons aavec la lettre : {lettre}")
    for user in users_list:
        print(f"c'est à {user} de jouer")
        for categories in list_categories:
            reponse=input(f"donne un ou une  {categories} commencant par la lettre {lettre}")


#boucles principales
if __name__=="__main__":
    lettre=choose_lettre()
    users_list=gen_users_list()
    list_categories=gen_categories()
    #new_game()
     