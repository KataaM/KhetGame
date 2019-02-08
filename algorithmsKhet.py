

def possibleFleche(xpos,ypos,map,joueur):
    ecartHaut = 145
    ecartGauche = 82
    for ligne in range (0,8):
        for colonne in range ( 0 ,10 ):
            if xpos>84*colonne+ecartGauche and xpos<84*colonne + ecartGauche + 84 and ypos > 84*ligne + ecartHaut and ypos < 84*ligne + ecartHaut + 84 :

                if (map[ligne][colonne]%1000)//100 == joueur and map[ligne][colonne] > 1000 and map[ligne][colonne]%100//10 != 6:
                    return True,ligne,colonne
                else:
                    return False,0,0
    return False,0,0


def Trajectoire(map,joueur,orientation,ligne,colonne):

    if orientation == 3 and ligne < 7:## bas
        if map[ligne+1][colonne]%100== 31 or map[ligne+1][colonne]%100== 33 or map[ligne+1][colonne]%100== 54 :
            orientation = 4
            return ligne+1,colonne,orientation
        if map[ligne + 1][colonne] % 100 == 32 or map[ligne + 1][colonne] % 100 == 34 or map[ligne + 1][colonne] % 100 == 51 :
            orientation = 2
            return ligne + 1, colonne, orientation
        if map[ligne + 1][colonne] % 100 == 42 or map[ligne + 1][colonne] % 100 == 44  or map[ligne + 1][colonne] % 100 == 43 or map[ligne + 1][colonne] % 100 == 53 or map[ligne + 1][colonne] % 100 == 52:
            orientation = "boom"
            return ligne + 1, colonne, orientation
        if map[ligne + 1][colonne] % 100 == 41:
            orientation = "bloc"
            return ligne + 1, colonne, orientation
        if (map[ligne + 1][colonne] % 1000//10 == 22 and joueur == 3) or (map[ligne + 1][colonne] % 1000//10 == 32 and joueur == 2):
            orientation = "win"
            return ligne + 1, colonne, orientation


        else:
            return ligne + 1, colonne, orientation





    elif orientation == 1 and ligne > 0:###haut
        if map[ligne-1][colonne]%100== 31 or map[ligne-1][colonne]%100== 33 or map[ligne-1][colonne]%100== 52 :
            orientation = 2
            return ligne-1,colonne,orientation
        if map[ligne - 1][colonne] % 100 == 32 or map[ligne - 1][colonne] % 100 == 34 or map[ligne - 1][colonne] % 100 == 53:
            orientation = 4
            return ligne - 1, colonne, orientation
        if map[ligne - 1][colonne] % 100 == 42 or map[ligne - 1][colonne] % 100 == 44  or map[ligne -1][colonne] % 100 == 41 or map[ligne - 1][colonne] % 100 == 51 or map[ligne - 1][colonne] % 100 == 54:
            orientation = "boom"
            return ligne - 1, colonne, orientation
        if map[ligne - 1][colonne] % 100 == 43:
            orientation = "bloc"
            return ligne - 1, colonne, orientation
        if (map[ligne -1][colonne] % 1000//10 == 22 and joueur == 3) or (map[ligne - 1][colonne] % 1000//10 == 32 and joueur == 2):
            orientation = "win"
            return ligne - 1, colonne, orientation

        else:
            return ligne - 1, colonne, orientation



    elif orientation == 2 and colonne < 9 :###droite
        if map[ligne][colonne+1]%100== 31 or map[ligne][colonne+1]%100== 33 or map[ligne][colonne+1]%100== 54 :
            orientation = 1
            return ligne,colonne+1,orientation
        if map[ligne][colonne+1] % 100 == 32 or map[ligne][colonne+1] % 100 == 34 or map[ligne][colonne+1] % 100 == 53 :
            orientation = 3
            return ligne, colonne+1, orientation
        if map[ligne][colonne+1] % 100 == 42 or map[ligne][colonne+1] % 100 == 43  or map[ligne][colonne+1] % 100 == 41 or map[ligne][colonne+1] % 100 == 51 or map[ligne][colonne+1] % 100 == 52:
            orientation = "boom"
            return ligne, colonne+1, orientation
        if map[ligne ][colonne+1] % 100 == 44:
            orientation = "bloc"
            return ligne , colonne+1, orientation
        if (map[ligne][colonne+1] % 1000//10 == 22 and joueur == 3) or (map[ligne][colonne+1] % 1000//10 == 32 and joueur == 2):
            orientation = "win"
            return ligne, colonne+1, orientation
        else:
            return ligne , colonne+1, orientation

    elif orientation == 4 and colonne > 0:###gauche
        if map[ligne][colonne-1]%100== 31 or map[ligne][colonne-1]%100== 33 or map[ligne][colonne-1]%100== 52 :
            orientation = 3
            return ligne,colonne-1,orientation
        if map[ligne][colonne-1] % 100 == 32 or map[ligne][colonne-1] % 100 == 34 or map[ligne][colonne-1] % 100 == 51 :
            orientation = 1
            return ligne, colonne-1, orientation
        if map[ligne][colonne-1] % 100 == 44 or map[ligne][colonne-1] % 100 == 43  or map[ligne][colonne-1] % 100 == 41 or map[ligne][colonne-1] % 100 == 53 or map[ligne][colonne-1] % 100 == 54:
            orientation = "boom"
            return ligne, colonne-1, orientation
        if map[ligne ][colonne-1] % 100 == 42:
            orientation = "bloc"
            return ligne , colonne-1, orientation
        if (map[ligne][colonne-1] % 1000//10 == 22 and joueur == 3) or (map[ligne][colonne-1] % 1000//10 == 32 and joueur == 2):
            orientation = "win"
            return ligne, colonne-1, orientation
        else:
            return ligne , colonne-1, orientation

    else :
        return "stop",0,0



