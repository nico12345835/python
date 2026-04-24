import random 

def gen_grid():
    grille=[[],[],[],[]]
    nombres_choisis=[]
    for i in range(16):
        number=random.randint(1,99)
        while number in nombres_choisis:
            number=random.randint(1,99)
        nombres_choisis.append(number)
    print(nombres_choisis)

if __name__=="__main__":
    gen_grid()