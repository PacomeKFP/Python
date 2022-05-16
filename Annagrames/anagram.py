from random import *

Errors = ("Alerte !, il n'y a pas de mot dans cette chaine", )#Ma liste d'erreurs possibles
def main():

    print('Bienvenus dans ce jeu\n Les points sont comptés à partir du nombre de caractères utilisés pour former ta chaine !\n')
    score = [0, 0]
    Alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    dic = open('fr.txt')
    dio = ""
    for line in dic:
        dio += line + " "
    dio = dio.lower()
    dico = dio.split()
    dic.close()

    while True:
        #le PC choisi un mot et l'affiche
        s=""
        shazam = ""
        sham = choice(dico)
        m = False
        while not m:
            m=True
            for elm in sham:
                if not elm in Alphabet:
                    m = False
                    sham = choice(dico)

        for element in choices(Alphabet, k=randint(3,8)):
            s+=element
        for elm in sample(s+sham, len(s+sham)):
            shazam += elm

        affichage = shazam[ :]
        shazam = recherche(dico, affichage, len(affichage))
        reponse = input("Quel est votre mot?\n" + affichage.upper() + '\n')

        if(reponse in dico):
            print("Bien joué\n le meilleur coup est :", shazam )
            score[0] += len(reponse)
        else:
            score[1] += 10
            print("Mot invalide !, vous auriez pu entrer:\n")
            possibles = autre(dico, affichage, len(affichage))
            for element in possibles:
                print(element.upper(), end=' , ')

        #Au joueur de proposer une liste
        sesam = input("Vos lettres : ")
        coup = recherche(dico, sesam, len(sesam))
        if coup not in Errors:
            print("Le meilleur mot est ", coup)
            score[1] += len(coup)
        else:
            test = input("Aucun coup possible!\n Que proposez vous?")
            score[1]+=10
        print("Les scores sont :\nJoueur --- ", score[0],"\n  PC  --- ", score[1])


def autre(Liste, chaine, long):
    result = []
    if(long == 0):
        return result
    for line in Liste:
        ok = True
        if len(line) == long:
            for letter in line:
                if line.count(letter) > chaine.count(letter):
                    ok=False
                    break
        else:
            ok= False
        if ok:
            result.append(line)
    return result + autre(Liste, chaine, long-1)


def recherche(Liste, chaine, long):
    if(long == 0):
        return Errors[0]
    for line in Liste:
        ok = True
        if len(line) == long:
            for letter in line:
                if line.count(letter) > chaine.count(letter):
                    ok = False
                    break
        else:
            ok = False
        if ok:
            return line
    return recherche(Liste, chaine, long-1)




if(__name__=="__main__"):
   main()


