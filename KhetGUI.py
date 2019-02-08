import pygame
from pygame import *
import algorithmsKhet



dicoCouleur = {'marronF':(45,29,12),'marronC':(117,95,68)}

dicoMenuImg = {'wall':pygame.image.load('img/wallpaper1.png'),'menu':pygame.image.load('img/wallpaper2.png'),'terrain':pygame.image.load('img/terrain.png'),'vol1':pygame.image.load('img/vol1.png'),'vol2':pygame.image.load('img/vol2.png'),'vol3':pygame.image.load('img/vol3.png')}

dicoFleche = {'anti':pygame.image.load('img/fleches/anti.png'),'hor':pygame.image.load('img/fleches/horaire.png'),'bas':pygame.image.load('img/fleches/bas.png'),
              'haut':pygame.image.load('img/fleches/haut.png'),'droite':pygame.image.load('img/fleches/droite.png'),'gauche':pygame.image.load('img/fleches/gauche.png',)
             ,'diagonalebasgauche':pygame.image.load('img/fleches/diagonalebasgauche.png'),'diagonalehautgauche':pygame.image.load('img/fleches/diagonalehautgauche.png'),
              'diagonalebasdroite':pygame.image.load('img/fleches/diagonalebasdroite.png'),'diagonalehautdroite':pygame.image.load('img/fleches/diagonalehautdroite.png'),}

dicoJoueurs = {'221':pygame.image.load('img/bleu/pha1B.png'),'223':pygame.image.load('img/bleu/pha3B.png'),
            '222':pygame.image.load('img/bleu/pha2B.png'),'224':pygame.image.load('img/bleu/pha4B.png'),
            '231': pygame.image.load('img/bleu/mir1B.png'), '232':pygame.image.load('img/bleu/mir2B.png'),
            '233': pygame.image.load('img/bleu/mir3B.png'),'234':pygame.image.load('img/bleu/mir4B.png'),
            '241': pygame.image.load('img/bleu/anu1B.png'),'243':pygame.image.load('img/bleu/anu3B.png'),
            '242': pygame.image.load('img/bleu/anu2B.png'),'244':pygame.image.load('img/bleu/anu4B.png'),
            '251': pygame.image.load('img/bleu/pyr1B.png'),'252':pygame.image.load('img/bleu/pyr2B.png'),
            '253': pygame.image.load('img/bleu/pyr3B.png'),'254':pygame.image.load('img/bleu/pyr4B.png'),
            '261': pygame.image.load('img/bleu/sphi1B.png'),'263':pygame.image.load('img/bleu/sphi3B.png'),
            '262': pygame.image.load('img/bleu/sphi2B.png'), '264': pygame.image.load('img/bleu/sphi4B.png'),

            '321':pygame.image.load('img/rouge/pha1R.png'),'323':pygame.image.load('img/rouge/pha3R.png'),
             '322':pygame.image.load('img/rouge/pha2R.png'),'324':pygame.image.load('img/rouge/pha4R.png'),
            '331': pygame.image.load('img/rouge/mir1R.png'), '332':pygame.image.load('img/rouge/mir2R.png'),
            '333': pygame.image.load('img/rouge/mir3R.png'),'334':pygame.image.load('img/rouge/mir4R.png'),
            '341': pygame.image.load('img/rouge/anu1R.png'),'343':pygame.image.load('img/rouge/anu3R.png'),
             '342': pygame.image.load('img/rouge/anu2R.png'),'344':pygame.image.load('img/rouge/anu4R.png'),
            '351': pygame.image.load('img/rouge/pyr1R.png'),'352':pygame.image.load('img/rouge/pyr2R.png'),
            '353': pygame.image.load('img/rouge/pyr3R.png'),'354':pygame.image.load('img/rouge/pyr4R.png'),
            '361': pygame.image.load('img/rouge/sphi1R.png'),'363':pygame.image.load('img/rouge/sphi3R.png'),
             '362': pygame.image.load('img/rouge/sphi2R.png'),'364':pygame.image.load('img/rouge/sphi4R.png')}
dicoLaser = {'bleuV':pygame.image.load('img/laser/laserBleuVert.png'),'rougeV':pygame.image.load('img/laser/laserRougeVert.png'),'rougeH':pygame.image.load('img/laser/laserRougeHor.png'),'bleuH':pygame.image.load('img/laser/laserBleuHor.png')}

classic_map = [[2263,311,111,111,1243,1223,1243,1252,211,311],
               [211,111,1253,111,111,111,111,111,111,311],
               [211,111,111,1354,111,111,111,111,111,311],
               [2251,111,1353,111,1234,1231,111,1252,111,3354],
               [2252,111,1354,111,1333,1332,111,3251,111,3353],
               [211,111,111,111,111,111,1252,111,111,311],
               [211,111,111,111,111,111,111,1351,111,311],
               [211,311,1354,1341,1321,1341,111,111,211,3361]]

Imhotep_map=[[2263,311,111,111,1243,1223,1243,1233,211,311],
 [211,111,111,111,111,111,111,111,111,311],
 [211,111,111,1354,111,111,3251,111,111,311],
 [2251,1353,111,111,1352,1233,111,111,1252,3354],
 [2252,1354,111,111,1331,2254,111,111,3251,3353],
 [211,111,111,1353,111,111,1252,111,111,311],
 [211,111,111,111,111,111,111,111,111,311],
 [211,311,1331,1341,1321,1341,111,111,211,3361]]

Dynasty_map=[[2263,311,111,111,1253,1243,1252,111,211,311],
 [211,111,111,111,111,1223,111,111,111,311],
 [2251,111,111,111,1253,1243,1231,111,111,311],
 [2252,111,1234,111,3354,111,1352,111,111,311],
 [211,111,111,2254,111,1252,111,1332,111,3354],
 [211,111,111,1333,1341,3351,111,111,111,3353],
 [211,111,111,111,1321,111,111,111,111,311],
 [211,311,111,3354,1341,3351,111,111,211,3361]]


pygame.mixer.pre_init(44100,-16,2,2048)
pygame.mixer.init()

pygame.init()
FPS = 30
fpsClock = pygame.time.Clock()
sonClic = pygame.mixer.Sound('sounds/clic2.wav')
sonLaser = pygame.mixer.Sound('sounds/laserTire.wav')
sonBoom = pygame.mixer.Sound('sounds/laserBoom.wav')


def KhetGUI():




    maSurface = pygame.display.set_mode((1440, 810))
    enCours= True
    demande="menu"
    while enCours:
        if demande == "menu":
            demande = Menu(maSurface)

        if demande == "classique":
            demande=GamePlay(maSurface,demande)
        elif demande == "Imhotep":
            demande=GamePlay(maSurface,demande)
        elif demande == "Dynasty":
            demande=GamePlay(maSurface,demande)
        elif demande == "quit":
            enCours =False




def Menu(maSurface):
    pygame.mixer.music.load('sounds/egypt.mp3')
    ##pygame.mixer.music.queue('sounds/egypt.mp3')
    pygame.mixer.music.play()

    clicToPlay = False
    numeroMenu = 1
    jouer = True
    vol=3
    while jouer:
        ####Debut de partie ####


        if not clicToPlay:
            maSurface.blit(dicoMenuImg['wall'], (0, 0))

        if clicToPlay:
            xhover, yhover = pygame.mouse.get_pos()
            maSurface.blit(dicoMenuImg['menu'], (0, 0))
            if vol == 3:
                maSurface.blit(dicoMenuImg['vol3'], (900, 680))
            elif vol == 2:
                maSurface.blit(dicoMenuImg['vol2'], (900, 680))
            else:
                maSurface.blit(dicoMenuImg['vol1'], (900, 680))

            if numeroMenu == 1:



                if xhover > 620 and yhover > 300 and xhover < 810 and yhover < 352:
                    TextMenuColor(maSurface, 'Jouer', 620, 300, 'marronC',60)
                else:
                    TextMenuColor(maSurface,'Jouer',620,300,'marronF',60)
                if xhover > 600 and yhover>400 and xhover < 845 and yhover < 452:
                    TextMenuColor(maSurface,'Quitter',600,400,'marronC',60)
                else:
                    TextMenuColor(maSurface, 'Quitter', 600, 400, 'marronF',60)


            elif numeroMenu == 2:

                if xhover > 610 and yhover > 300 and xhover < 830 and yhover < 330:
                    TextMenuColor(maSurface, 'Local JCJ', 610, 300, 'marronC', 40)
                else:
                    TextMenuColor(maSurface,'Local JCJ',610,300,'marronF',40)
                TextMenuColor(maSurface, 'En ligne(n/d)', 610, 400, 'marronF', 30)
                TextMenuColor(maSurface, 'Creation de map(n/d)', 550, 500, 'marronF', 30)
                if xhover > 530 and yhover > 700 and xhover < 625 and yhover < 720:
                    TextMenuColor(maSurface, 'Retour', 530, 700, 'marronC', 25)
                else:
                    TextMenuColor(maSurface, 'Retour', 530, 700, 'marronF', 25)

            elif numeroMenu == 3:

                if xhover > 610 and yhover > 300 and xhover < 830 and yhover < 330:
                    TextMenuColor(maSurface, 'Classique', 610, 300, 'marronC', 40)
                else:
                    TextMenuColor(maSurface, 'Classique', 610, 300, 'marronF', 40)

                if xhover > 630 and yhover > 360 and xhover < 850 and yhover < 390:
                    TextMenuColor(maSurface, 'Imhotep', 640, 360, 'marronC', 40)
                else:
                    TextMenuColor(maSurface, 'Imhotep', 640, 360, 'marronF', 40)

                if xhover > 650 and yhover > 420 and xhover < 870 and yhover < 450:
                    TextMenuColor(maSurface, 'Dynasty', 640, 420, 'marronC', 40)
                else:
                    TextMenuColor(maSurface, 'Dynasty', 640, 420, 'marronF', 40)

                if xhover > 530 and yhover > 700 and xhover < 625 and yhover < 720:
                    TextMenuColor(maSurface, 'Retour', 530, 700, 'marronC', 25)
                else:
                    TextMenuColor(maSurface, 'Retour', 530, 700, 'marronF', 25)




        for event in pygame.event.get():

            if event.type == QUIT:
                jouer = False

            if clicToPlay and event.type == MOUSEBUTTONDOWN:
                sonClic.play()

                if event.button == 1 :
                    if dicoMenuImg['vol3'].get_rect().move(900, 680).collidepoint(xhover, yhover) and vol==3:
                        vol= 2
                        pygame.mixer.music.set_volume(0.5)
                    elif dicoMenuImg['vol2'].get_rect().move(900, 680).collidepoint(xhover, yhover) and vol==2:
                        vol= 1
                        pygame.mixer.music.set_volume(0)
                    elif dicoMenuImg['vol1'].get_rect().move(900, 680).collidepoint(xhover, yhover)and vol==1:
                        vol= 3
                        pygame.mixer.music.set_volume(1)
                    if xhover > 610 and yhover > 300 and xhover < 830 and yhover < 330 and numeroMenu ==3:
                        return "classique"
                    if xhover > 630 and yhover > 360 and xhover < 850 and yhover < 390:
                        return "Imhotep"
                    if xhover > 650 and yhover > 420 and xhover < 870 and yhover < 450:
                        return "Dynasty"
                    if xhover > 600 and yhover > 300 and xhover < 820 and yhover < 330 and numeroMenu < 3:
                        numeroMenu += 1
                    if xhover > 530 and yhover > 700 and xhover < 625 and yhover < 720 and numeroMenu > 1:
                        numeroMenu -=1

                    if xhover > 620 and yhover > 300 and xhover < 810 and yhover < 352 and numeroMenu == 1:
                        numeroMenu = 2
                    if xhover > 600 and yhover > 400 and xhover < 845 and yhover < 452 and numeroMenu == 1:
                        jouer = False



            if clicToPlay == False and event.type == MOUSEBUTTONDOWN:
                ##if event.button == 1:
                clicToPlay = True



        pygame.display.update()

    return "quit"


def TextMenuColor(maSurface,texte,x,y,couleur,taille):

    fontObj = pygame.font.Font('font/COPRGTL.TTF', taille)
    texteSurface = fontObj.render(texte, True, dicoCouleur[couleur], None)
    texteRect = texteSurface.get_rect()
    texteRect.topleft = (x, y)
    maSurface.blit(texteSurface, texteRect)


def GamePlay(maSurface,demande):

    jouer = True
    maSurface = pygame.display.set_mode((1000, 880))
    playmap ='nothing'
    joueur = 2
    select = False
    type = 1
    drawF = False
    ligne,colonne = 0,0
    ecartHaut = 145
    ecartGauche = 82
    xgauche = colonne * 84 + ecartGauche -50
    ygauche = ligne * 84 + ecartHaut +20
    xdroite = colonne * 84 + ecartGauche + 90
    ydroite = ligne * 84 + ecartHaut +20
    xhaut = colonne * 84 + ecartGauche + 15
    yhaut = ligne * 84 + ecartHaut - 75
    xbas = colonne * 84 + ecartGauche + 20
    ybas = ligne * 84 + ecartHaut + 100
    xanti = colonne * 84 + ecartGauche - 50
    yanti = ligne * 84 + ecartHaut + 20
    xhor = colonne * 84 + ecartGauche + 90
    yhor = ligne * 84 + ecartHaut + 20
    pygame.mixer.music.load('sounds/musicGame.mp3')
    ##pygame.mixer.music.queue('sounds/egypt.mp3')
    pygame.mixer.music.play()

    x = 0
    if demande == 'classique':
        playmap=classic_map
    if demande == "Imhotep":
        playmap= Imhotep_map
    if demande == "Dynasty":
        playmap = Dynasty_map

    while jouer :
        DrawBoard(maSurface,playmap,joueur)
        for event in pygame.event.get():
            if event.type == QUIT:
                jouer=False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if select == False:
                        select = True
                    else :
                        select = False
                    xpos,ypos=pygame.mouse.get_pos()
                    Possible = possible(playmap, ligne, colonne, dicoFleche, xgauche, ygauche, xpos, ypos, xdroite, ydroite, xbas,
                             ybas, xhaut, yhaut,type)
                    if Possible == 1:
                        if playmap[ligne][colonne-1] == 111 :
                            playmap[ligne][colonne-1] = playmap[ligne][colonne]
                            playmap[ligne][colonne] = 111
                        if playmap[ligne][colonne-1] == 211:
                            playmap[ligne][colonne-1] = playmap[ligne][colonne]
                            playmap[ligne][colonne] = 211
                        if playmap[ligne ][colonne-1] == 311:
                            playmap[ligne][colonne-1] = playmap[ligne][colonne]
                            playmap[ligne][colonne] = 311
                        x = 1
                    if Possible == 2 :
                        if playmap[ligne][colonne+1] == 111 :
                            playmap[ligne][colonne+1] = playmap[ligne][colonne]
                            playmap[ligne][colonne] = 111
                        if playmap[ligne][colonne+1] == 211:
                            playmap[ligne][colonne+1] = playmap[ligne][colonne]
                            playmap[ligne][colonne] = 211
                        if playmap[ligne ][colonne+1] == 311:
                            playmap[ligne][colonne+1] = playmap[ligne][colonne]
                            playmap[ligne][colonne] = 311
                        x = 1
                    if Possible == 3:
                        if playmap[ligne+1][colonne] == 111 :
                            playmap[ligne+1][colonne] = playmap[ligne][colonne]
                            playmap[ligne][colonne] = 111
                        if playmap[ligne + 1][colonne] == 211:
                            playmap[ligne +1][colonne] = playmap[ligne][colonne]
                            playmap[ligne][colonne] = 211
                        if playmap[ligne + 1][colonne] == 311:
                            playmap[ligne + 1][colonne] = playmap[ligne][colonne]
                            playmap[ligne][colonne] = 311
                        x = 1
                    if Possible == 4:
                        if playmap[ligne-1][colonne] == 111 :
                            playmap[ligne-1][colonne] = playmap[ligne][colonne]
                            playmap[ligne][colonne] = 111
                        if playmap[ligne - 1][colonne] == 211:
                            playmap[ligne - 1][colonne] = playmap[ligne][colonne]
                            playmap[ligne][colonne] = 211
                        if playmap[ligne - 1][colonne] == 311:
                            playmap[ligne - 1][colonne] = playmap[ligne][colonne]
                            playmap[ligne][colonne] = 311
                        x = 1
                    if Possible == 5:
                        if playmap[ligne+1][colonne+1] == 111 :
                            playmap[ligne+1][colonne+1] = playmap[ligne][colonne]
                            playmap[ligne][colonne] = 111
                        if playmap[ligne + 1][colonne+1] == 211:
                            playmap[ligne + 1][colonne+1] = playmap[ligne][colonne]
                            playmap[ligne][colonne] = 211
                        if playmap[ligne + 1][colonne+1] == 311:
                            playmap[ligne + 1][colonne+1] = playmap[ligne][colonne]
                            playmap[ligne][colonne] = 311
                        x = 1
                    if Possible == 6:
                        if playmap[ligne+1][colonne-1] == 111 :
                            playmap[ligne+1][colonne-1] = playmap[ligne][colonne]
                            playmap[ligne][colonne] = 111
                        if playmap[ligne + 1][colonne-1] == 211:
                            playmap[ligne + 1][colonne-1] = playmap[ligne][colonne]
                            playmap[ligne][colonne] = 211
                        if playmap[ligne + 1][colonne-1] == 311:
                            playmap[ligne + 1][colonne-1] = playmap[ligne][colonne]
                            playmap[ligne][colonne] = 311
                        x = 1
                    if Possible == 7:
                        if playmap[ligne-1][colonne+1] == 111 :
                            playmap[ligne-1][colonne+1] = playmap[ligne][colonne]
                            playmap[ligne][colonne] = 111
                        if playmap[ligne - 1][colonne+1] == 211:
                            playmap[ligne - 1][colonne+1] = playmap[ligne][colonne]
                            playmap[ligne][colonne] = 211
                        if playmap[ligne - 1][colonne+1] == 311:
                            playmap[ligne - 1][colonne+1] = playmap[ligne][colonne]
                            playmap[ligne][colonne] = 311
                        x = 1
                    if Possible == 8:
                        if playmap[ligne-1][colonne-1] == 111 :
                            playmap[ligne-1][colonne-1] = playmap[ligne][colonne]
                            playmap[ligne][colonne] = 111
                        if playmap[ligne - 1][colonne-1] == 211:
                            playmap[ligne - 1][colonne-1] = playmap[ligne][colonne]
                            playmap[ligne][colonne] = 211
                        if playmap[ligne - 1][colonne-1] == 311:
                            playmap[ligne - 1][colonne-1] = playmap[ligne][colonne]
                            playmap[ligne][colonne] = 311
                        x = 1

                    if Possible == 13:
                        stock = playmap[ligne][colonne - 1]
                        playmap[ligne][colonne - 1] = playmap[ligne][colonne]
                        playmap[ligne][colonne] = stock
                        x = 1
                    if Possible == 23:
                        stock = playmap[ligne][colonne + 1]
                        playmap[ligne][colonne + 1] = playmap[ligne][colonne]
                        playmap[ligne][colonne] = stock
                        x = 1
                    if Possible == 33:
                        stock = playmap[ligne+1][colonne]
                        playmap[ligne+1][colonne] = playmap[ligne][colonne]
                        playmap[ligne][colonne] = stock
                        x = 1
                    if Possible == 43:
                        stock = playmap[ligne-1][colonne]
                        playmap[ligne-1][colonne] = playmap[ligne][colonne]
                        playmap[ligne][colonne] = stock
                        x = 1
                    if Possible == 53:
                        stock = playmap[ligne + 1][colonne + 1]
                        playmap[ligne + 1][colonne + 1] = playmap[ligne][colonne]
                        playmap[ligne][colonne] = stock
                        x = 1
                    if Possible == 63:
                        stock = playmap[ligne + 1][colonne - 1]
                        playmap[ligne + 1][colonne - 1] = playmap[ligne][colonne]
                        playmap[ligne][colonne] = stock
                        x = 1
                    if Possible == 73:
                        stock = playmap[ligne - 1][colonne + 1]
                        playmap[ligne - 1][colonne + 1] = playmap[ligne][colonne]
                        playmap[ligne][colonne] = stock
                        x = 1
                    if Possible == 83:
                        stock = playmap[ligne - 1][colonne - 1]
                        playmap[ligne - 1][colonne - 1] = playmap[ligne][colonne]
                        playmap[ligne][colonne] = stock
                        x = 1
                    if x !=1 and type == 2:
                        x=Rotation(xanti,yanti,xhor,yhor,xpos,ypos,playmap,ligne,colonne)
                    print(playmap)
                    drawF,ligne,colonne=algorithmsKhet.possibleFleche(xpos,ypos,playmap,joueur)
                    xgauche = colonne * 84 + ecartGauche - 50
                    ygauche = ligne * 84 + ecartHaut + 20
                    xdroite = colonne * 84 + ecartGauche + 90
                    ydroite = ligne * 84 + ecartHaut + 20
                    xhaut = colonne * 84 + ecartGauche + 15
                    yhaut = ligne * 84 + ecartHaut - 75
                    xbas = colonne * 84 + ecartGauche + 20
                    ybas = ligne * 84 + ecartHaut + 100
                    xanti = colonne * 84 + ecartGauche - 50
                    yanti = ligne * 84 + ecartHaut +20
                    xhor = colonne * 84 + ecartGauche + 90
                    yhor = ligne * 84 + ecartHaut + 20
                if x == 1:

                    fin=Laser(maSurface,joueur,playmap)
                    if fin == "win":
                        return Win(maSurface,joueur)

                    if joueur == 2 :
                        joueur = 3
                        x = 0
                    if joueur == 3 and x== 1:
                        joueur = 2
                        x = 0
                if event.button == 3:
                    if type == 1:
                        type = 2
                    elif type == 2:
                        type = 1


        if drawF == True and select == True :
            DrawFleche(maSurface,ligne,colonne,type,playmap,joueur)


        pygame.display.update()
    return "quit"





def DrawBoard(maSurface,map,joueur):

    maSurface.blit(dicoMenuImg['terrain'], (0, 0))
    if joueur == 2:
        maSurface.blit(pygame.image.load('img/boutonB.png'),(35,5))
        maSurface.blit(pygame.image.load('img/boutonRD.png'), (865, 5))
    else:
        maSurface.blit(pygame.image.load('img/boutonBD.png'), (35, 5))
        maSurface.blit(pygame.image.load('img/boutonR.png'), (865, 5))

    DrawCell(maSurface,map)


def DrawCell (maSurface,map):
    ecartHaut = 65
    ecartGauche = 82
    for ligne in range(0,8):
        for colonne in range (0,10):
            case = map [ligne][colonne]
            if case > 1000:
                case = case % 1000

                maSurface.blit(dicoJoueurs[str(case)],((colonne*84+ecartGauche),(ligne*84+ecartHaut)))

def DrawFleche(maSurface,ligne,colonne,type,playmap,joueur):

    ecartHaut = 145
    ecartGauche = 82

    if type == 1:
        maSurface.blit(dicoFleche['gauche'], ((colonne * 84 + ecartGauche -50), (ligne * 84 + ecartHaut +20 )))
        maSurface.blit(dicoFleche['droite'], ((colonne * 84 + ecartGauche + 90), (ligne * 84 + ecartHaut +20 )))
        maSurface.blit(dicoFleche['haut'], ((colonne * 84 + ecartGauche + 15), (ligne * 84 + ecartHaut - 75)))
        maSurface.blit(dicoFleche['bas'], ((colonne * 84 + ecartGauche + 20), (ligne * 84 + ecartHaut + 100)))
        maSurface.blit(dicoFleche['diagonalehautdroite'],
                       ((colonne * 84 + ecartGauche + 90), (ligne * 84 + ecartHaut - 60)))
        maSurface.blit(dicoFleche['diagonalebasdroite'],
                       ((colonne * 84 + ecartGauche + 90), (ligne * 84 + ecartHaut + 90)))
        maSurface.blit(dicoFleche['diagonalehautgauche'],
                   ((colonne * 84 + ecartGauche - 70), (ligne * 84 + ecartHaut - 60)))
        maSurface.blit(dicoFleche['diagonalebasgauche'], ((colonne * 84 + ecartGauche - 60), (ligne * 84 + ecartHaut + 90)))
    if type == 2:
        maSurface.blit(dicoFleche['anti'], ((colonne * 84 + ecartGauche - 50), (ligne * 84 + ecartHaut + 20)))
        maSurface.blit(dicoFleche['hor'], ((colonne * 84 + ecartGauche + 90), (ligne * 84 + ecartHaut + 20)))

def Laser(maSurface,joueur,map):
    stop = False
    DrawBoard(maSurface,map,joueur)

    for ligne in range (0,8):
        for colonne in range (0,10):

            if map[ligne][colonne]%100//10 == 6 and map[ligne][colonne]%1000//100 == joueur:
                orientation = map[ligne][colonne] % 10
                sonLaser.play()
                while  stop == False:

                    ligne,colonne,neworientation = algorithmsKhet.Trajectoire(map,joueur,orientation,ligne,colonne)
                    if ligne != "stop":
                        if neworientation =="win":
                            return "win"
                        if neworientation == "boom":
                            sonBoom.play()
                            if map[ligne][colonne]//1000 == 2:
                                map[ligne][colonne]= 211
                            elif map[ligne][colonne]//1000 == 3:
                                map[ligne][colonne]= 311
                            else:
                                map[ligne][colonne]=111
                            stop = True
                        elif neworientation == "bloc":
                            stop = True

                        elif neworientation == orientation:

                            DrawLaser(maSurface, joueur, map, orientation, ligne, colonne)
                        orientation = neworientation
                    else:
                        stop = True
                return "no-win"


def DrawLaser(maSurface,joueur,map,orientation,ligne,colonne):
    ecartHaut = 145
    ecartGauche = 82
    if joueur == 2 :
        if orientation == 1 or orientation == 3 :
            laser =dicoLaser['bleuV']

        else:
            laser = dicoLaser['bleuH']

    else:
        if orientation == 1 or orientation == 3:
            laser = dicoLaser['rougeV']
        else:
            laser = dicoLaser['rougeH']



    if orientation == 3 : ###bas



        for i in range (0,5):

            DrawCell(maSurface,map)
            maSurface.blit(laser,((colonne*84 + ecartGauche+30),((ligne)*84+ecartHaut+(17*i))))
            pygame.time.wait(20)
            pygame.display.update()

    if orientation == 1  : ###haut



        for i in range (0,5):
            DrawCell(maSurface,map)
            maSurface.blit(laser,((colonne*84 + ecartGauche+30),((ligne)*84+ecartHaut-(17*i)+67)))
            pygame.time.wait(20)
            pygame.display.update()

    if orientation == 2  : ###droite



        for i in range (0,5):
            DrawCell(maSurface,map)
            maSurface.blit(laser,((colonne*84 + ecartGauche+(17*i),((ligne)*84+ecartHaut+30))))
            pygame.time.wait(20)
            pygame.display.update()

    if orientation == 4  : ###gauche



        for i in range (0,5):
            DrawCell(maSurface,map)
            maSurface.blit(laser,((colonne*84 + ecartGauche-(17*i)+67,((ligne)*84+ecartHaut+30))))
            pygame.time.wait(20)
            pygame.display.update()











def possible (playmap,ligne,colonne,dicoFleche,xgauche, ygauche, xpos, ypos, xdroite, ydroite, xbas, ybas, xhaut, yhaut,type):
    if dicoFleche['gauche'].get_rect().move(xgauche, ygauche).collidepoint(xpos, ypos) and 0 < colonne and ( playmap[ligne][colonne] % 100 // 10 == 2 or playmap[ligne][colonne] % 100 // 10 == 4 or playmap[ligne][colonne] % 100 // 10 == 5)  and type == 1:
        if playmap[ligne][colonne]%1000//100 == 2 and playmap[ligne][colonne-1] == 211 or playmap[ligne][colonne-1] == 111:
            Possible = 1
            return Possible
        elif playmap[ligne][colonne]%1000//100 == 3 and playmap[ligne][colonne-1] == 311 or playmap[ligne][colonne-1] == 111:
            Possible = 1

            return Possible
    elif dicoFleche['droite'].get_rect().move(xdroite, ydroite).collidepoint(xpos, ypos) and 9 > colonne and (playmap[ligne][colonne] % 100 // 10 == 2 or playmap[ligne][colonne] % 100 // 10 == 4 or playmap[ligne][colonne] % 100 // 10 == 5)  and type == 1:
        if playmap[ligne][colonne]%1000//100 == 2 and playmap[ligne][colonne+1] == 211 or playmap[ligne][colonne+1] == 111:
            Possible = 2
            return Possible
        elif playmap[ligne][colonne]%1000//100 == 3 and playmap[ligne][colonne+1] == 311 or playmap[ligne][colonne+1] == 111:
            Possible = 2
            return Possible
    elif dicoFleche['bas'].get_rect().move(xbas, ybas).collidepoint(xpos, ypos) and 7 > ligne and (playmap[ligne][colonne] % 100 // 10 == 2 or playmap[ligne][colonne] % 100 // 10 == 4 or playmap[ligne][colonne] % 100 // 10 == 5)  and type == 1:
        if playmap[ligne][colonne]%1000//100 == 2 and playmap[ligne+1][colonne] == 211 or playmap[ligne+1][colonne] == 111:
            Possible = 3
            return Possible
        elif playmap[ligne][colonne]%1000//100 == 3 and playmap[ligne+1][colonne] == 311 or playmap[ligne+1][colonne] == 111:
            Possible = 3
            return Possible
    elif dicoFleche['haut'].get_rect().move(xhaut, yhaut).collidepoint(xpos, ypos) and 0 < ligne and (playmap[ligne][colonne] % 100 // 10 == 2 or playmap[ligne][colonne] % 100 // 10 == 4 or playmap[ligne][colonne] % 100 // 10 == 5)  and type == 1:
        if playmap[ligne][colonne]%1000//100 == 2 and playmap[ligne-1][colonne] == 211 or playmap[ligne-1][colonne] == 111:
            Possible = 4
            return Possible
        elif playmap[ligne][colonne]%1000//100 == 3 and playmap[ligne-1][colonne] == 311 or playmap[ligne-1][colonne] == 111:
            Possible = 4
            return Possible
    if dicoFleche['diagonalebasgauche'].get_rect().move(xgauche, ybas).collidepoint(xpos, ypos) and 0 < colonne and 7 > ligne and (playmap[ligne][colonne] % 100 // 10 == 2 or playmap[ligne][colonne] % 100 // 10 == 4 or playmap[ligne][colonne] % 100 // 10 == 5)  and type == 1:
        if playmap[ligne][colonne]%1000//100 == 2 and (playmap[ligne+1][colonne-1] == 211 or playmap[ligne+1][colonne-1] == 111):
            Possible = 6
            return Possible
        elif playmap[ligne][colonne]%1000//100 == 3 and playmap[ligne+1][colonne-1] == 311 or playmap[ligne+1][colonne-1] == 111:
            Possible = 6
            return Possible
    elif dicoFleche['diagonalebasdroite'].get_rect().move(xdroite, ybas).collidepoint(xpos, ypos) and 9 > colonne and 7 > ligne and (playmap[ligne][colonne] % 100 // 10 == 2 or playmap[ligne][colonne] % 100 // 10 == 4 or playmap[ligne][colonne] % 100 // 10 == 5)  and type == 1:
        if playmap[ligne][colonne]%1000//100 == 2 and playmap[ligne+1][colonne+1] == 211 or playmap[ligne+1][colonne+1] == 111:
            Possible = 5
            return Possible
        elif playmap[ligne][colonne]%1000//100 == 3 and playmap[ligne+1][colonne+1] == 311 or playmap[ligne+1][colonne+1] == 111:
            Possible = 5
            return Possible
    elif dicoFleche['diagonalehautdroite'].get_rect().move(xdroite, yhaut).collidepoint(xpos, ypos) and 7 > ligne and 9 > colonne and (playmap[ligne][colonne] % 100 // 10 == 2 or playmap[ligne][colonne] % 100 // 10 == 4 or playmap[ligne][colonne] % 100 // 10 == 5)  and type == 1:
        if playmap[ligne][colonne]%1000//100 == 2 and playmap[ligne-1][colonne+1] == 211 or playmap[ligne-1][colonne+1] == 111:
            Possible = 7
            return Possible
        elif playmap[ligne][colonne]%1000//100 == 3 and playmap[ligne-1][colonne+1] == 311 or playmap[ligne-1][colonne+1] == 111:
            Possible = 7
            return Possible
    elif dicoFleche['diagonalehautgauche'].get_rect().move(xgauche, yhaut).collidepoint(xpos, ypos) and 0 < ligne and 0 < colonne and (playmap[ligne][colonne] % 100 // 10 == 2 or playmap[ligne][colonne] % 100 // 10 == 4 or playmap[ligne][colonne] % 100 // 10 == 5)  and type == 1:
        if playmap[ligne][colonne]%1000//100 == 2 and playmap[ligne-1][colonne-1] == 211 or playmap[ligne-1][colonne-1] == 111:
            Possible = 8
            return Possible
        elif playmap[ligne][colonne]%1000//100 == 3 and playmap[ligne-1][colonne-1] == 311 or playmap[ligne-1][colonne-1] == 111:
            Possible = 8
            return Possible



    elif dicoFleche['gauche'].get_rect().move(xgauche, ygauche).collidepoint(xpos, ypos) and 0 < colonne and playmap[ligne][colonne]%100//10 == 3 and type == 1:
        if playmap[ligne][colonne]%1000//100 == 2 and (playmap[ligne][colonne-1] == 211 or playmap[ligne][colonne-1] == 111 or playmap[ligne][colonne-1]%100//10 == 4 or playmap[ligne][colonne-1]%100//10 == 5) and playmap[ligne][colonne-1]//1000 != 3:
            if playmap[ligne][colonne-1] == 211 or playmap[ligne][colonne-1] == 111 :
                Possible = 1
            else :
                Possible = 13
            return Possible
        elif playmap[ligne][colonne]%1000//100 == 3 and (playmap[ligne][colonne-1] == 311 or playmap[ligne][colonne-1] == 111 or playmap[ligne][colonne-1]%100//10 == 4 or playmap[ligne][colonne-1]%100//10 == 5) and playmap[ligne][colonne-1]//1000 != 2:
            if playmap[ligne][colonne-1] == 311 or playmap[ligne][colonne-1] == 111 :
                Possible = 1
            else :
                Possible = 13
            return Possible
    elif dicoFleche['droite'].get_rect().move(xdroite, ydroite).collidepoint(xpos, ypos) and 9 > colonne and playmap[ligne][colonne] % 100 // 10 == 3 and type == 1:
        if playmap[ligne][colonne] % 1000 // 100 == 2 and (playmap[ligne][colonne + 1] == 211 or playmap[ligne][colonne + 1] == 111 or playmap[ligne][colonne+1]%100//10 == 4 or playmap[ligne][colonne+1]%100//10 == 5) and playmap[ligne][colonne+1]//1000 != 3:
            if playmap[ligne][colonne+1] == 211 or playmap[ligne][colonne+1] == 111 :
                Possible = 2
            else :
                Possible = 23
            return Possible
        elif playmap[ligne][colonne] % 1000 // 100 == 3 and (playmap[ligne][colonne + 1] == 311 or playmap[ligne][colonne + 1] == 111 or playmap[ligne][colonne+1]%100//10 == 4 or playmap[ligne][colonne+1]%100//10 == 5) and playmap[ligne][colonne+1]//1000 != 2:
            if playmap[ligne][colonne+1] == 311 or playmap[ligne][colonne+1] == 111 :
                Possible = 2
            else :
                Possible = 23
            return Possible
    elif dicoFleche['bas'].get_rect().move(xbas, ybas).collidepoint(xpos, ypos) and 7 > ligne and playmap[ligne][colonne]%100//10 == 3 and type == 1:
        if playmap[ligne][colonne]%1000//100 == 2 and (playmap[ligne+1][colonne] == 211 or playmap[ligne+1][colonne] == 111 or playmap[ligne+1][colonne]%100//10 == 4 or playmap[+1][colonne]%100//10 == 5) and playmap[ligne+1][colonne]//1000 != 3:
            if playmap[ligne+1][colonne] == 211 or playmap[ligne+1][colonne] == 111 :
                Possible = 3
            else :
                Possible = 33
            return Possible
        elif playmap[ligne][colonne]%1000//100 == 3 and (playmap[ligne+1][colonne] == 311 or playmap[ligne+1][colonne] == 111 or playmap[ligne+1][colonne]%100//10 == 4 or playmap[ligne+1][colonne]%100//10 == 5) and playmap[ligne+1][colonne]//1000 != 2:
            if playmap[ligne + 1][colonne] == 311 or playmap[ligne + 1][colonne] == 111:
                Possible = 3
            else:
                Possible = 33
            return Possible
    elif dicoFleche['haut'].get_rect().move(xhaut, yhaut).collidepoint(xpos, ypos) and 0 < ligne and playmap[ligne][colonne]%100//10 == 3 and type == 1:
        if playmap[ligne][colonne]%1000//100 == 2 and (playmap[ligne-1][colonne] == 211 or playmap[ligne-1][colonne] == 111 or playmap[ligne-1][colonne]%100//10 == 4 or playmap[ligne-1][colonne]%100//10 == 5) and playmap[ligne-1][colonne]//1000 != 3:
            if playmap[ligne-1][colonne] == 211 or playmap[ligne-1][colonne] == 111 :
                Possible = 4
            else :
                Possible = 43
            return Possible
        elif playmap[ligne][colonne]%1000//100 == 3 and (playmap[ligne-1][colonne] == 311 or playmap[ligne-1][colonne] == 111 or playmap[ligne-1][colonne]%100//10 == 4 or playmap[ligne-1][colonne]%100//10 == 5) and playmap[ligne-1][colonne]//1000 != 2:
            if playmap[ligne -1][colonne] == 311 or playmap[ligne -1][colonne] == 111:
                Possible = 4
            else:
                Possible = 43
            return Possible
    elif dicoFleche['diagonalebasdroite'].get_rect().move(xdroite, ybas).collidepoint(xpos,ypos) and 7 > ligne and 9 > colonne and playmap[ligne][colonne] % 100 // 10 == 3 and type == 1:
        if playmap[ligne][colonne] % 1000 // 100 == 2 and (playmap[ligne  +1][colonne + 1] == 211 or playmap[ligne + 1][colonne + 1] == 111 or playmap[ligne + 1][colonne + 1] % 100 // 10 == 4 or playmap[ligne + 1][colonne + 1] % 100 // 10 == 5) and playmap[ligne + 1][colonne + 1] // 1000 != 3:
            if playmap[ligne+1][colonne +1] == 211 or playmap[ligne+1][colonne +1] == 111 :
                Possible = 5
            else :
                Possible = 53
            return Possible
        elif playmap[ligne][colonne] % 1000 // 100 == 3 and (playmap[ligne + 1][colonne + 1] == 311 or playmap[ligne + 1][colonne + 1] == 111 or playmap[ligne + 1][colonne + 1] % 100 // 10 == 4 or playmap[ligne - 1][colonne + 1] % 100 // 10 == 5) and playmap[ligne + 1][colonne + 1] // 1000 != 2:
            if playmap[ligne + 1][colonne +1] == 311 or playmap[ligne + 1][colonne +1] == 111:
                Possible = 5
            else:
                Possible = 53
            return Possible
    elif dicoFleche['diagonalebasgauche'].get_rect().move(xgauche, ybas).collidepoint(xpos,ypos) and 7 > ligne and 0 < colonne and playmap[ligne][colonne] % 100 // 10 == 3 and type == 1:
        if playmap[ligne][colonne] % 1000 // 100 == 2 and (playmap[ligne + 1][colonne - 1] == 211 or playmap[ligne + 1][colonne - 1] == 111 or playmap[ligne + 1][colonne - 1] % 100 // 10 == 4 or playmap[ligne + 1][colonne - 1] % 100 // 10 == 5) and playmap[ligne + 1][colonne - 1] // 1000 != 3:
            if playmap[ligne + 1][colonne- 1] == 211 or playmap[ligne + 1][colonne- 1] == 111:
                Possible = 6
            else:
                Possible = 63
            return Possible
        elif playmap[ligne][colonne] % 1000 // 100 == 3 and (playmap[ligne + 1][colonne - 1] == 311 or playmap[ligne + 1][colonne - 1] == 111 or playmap[ligne + 1][colonne - 1] % 100 // 10 == 4 or playmap[ligne + 1][colonne - 1] % 100 // 10 == 5) and playmap[ligne + 1][colonne - 1] // 1000 != 2:
            if playmap[ligne + 1][colonne- 1] == 311 or playmap[ligne + 1][colonne- 1] == 111:
                Possible = 6
            else:
                Possible = 63
            return Possible
    elif dicoFleche['diagonalehautdroite'].get_rect().move(xdroite, yhaut).collidepoint(xpos,ypos) and 0 < ligne and 9 > colonne and playmap[ligne][colonne] % 100 // 10 == 3 and type == 1:
        if playmap[ligne][colonne] % 1000 // 100 == 2 and (playmap[ligne - 1][colonne + 1] == 211 or playmap[ligne - 1][colonne + 1] == 111 or playmap[ligne - 1][colonne + 1] % 100 // 10 == 4 or playmap[ligne - 1][colonne + 1] % 100 // 10 == 5) and playmap[ligne - 1][colonne + 1] // 1000 != 3:
            if playmap[ligne- 1][colonne+1] == 211 or playmap[ligne- 1][colonne+1] == 111 :
                Possible = 7
            else :
                Possible = 73
            return Possible
        elif playmap[ligne][colonne] % 1000 // 100 == 3 and (playmap[ligne - 1][colonne + 1] == 311 or playmap[ligne - 1][colonne + 1] == 111 or playmap[ligne - 1][colonne + 1] % 100 // 10 == 4 or playmap[ligne - 1][colonne + 1] % 100 // 10 == 5) and playmap[ligne - 1][colonne + 1] // 1000 != 2:
            if playmap[ligne - 1][colonne+1] == 311 or playmap[ligne - 1][colonne+1] == 111:
                Possible = 7
            else:
                Possible = 73
            return Possible

    elif dicoFleche['diagonalehautgauche'].get_rect().move(xgauche, yhaut).collidepoint(xpos,ypos) and 0 < ligne and 0 < colonne and playmap[ligne][colonne] % 100 // 10 == 3 and type == 1:
        if playmap[ligne][colonne] % 1000 // 100 == 2 and (playmap[ligne - 1][colonne - 1] == 211 or playmap[ligne - 1][colonne - 1] == 111 or playmap[ligne - 1][colonne - 1] % 100 // 10 == 4 or playmap[ligne - 1][colonne - 1] % 100 // 10 == 5) and playmap[ligne - 1][colonne - 1] // 1000 != 3:
            if playmap[ligne - 1][colonne- 1] == 211 or playmap[ligne - 1][colonne- 1] == 111:
                Possible = 8
            else:
                Possible = 83
            return Possible
        elif playmap[ligne][colonne] % 1000 // 100 == 3 and (playmap[ligne - 1][colonne - 1] == 311 or playmap[ligne - 1][colonne - 1] == 111 or playmap[ligne - 1][colonne - 1] % 100 // 10 == 4 or playmap[ligne - 1][colonne - 1] % 100 // 10 == 5) and playmap[ligne - 1][colonne - 1] // 1000 != 2:
            if playmap[ligne - 1][colonne- 1] == 311 or playmap[ligne - 1][colonne- 1] == 111:
                Possible = 8
            else:
                Possible = 83
            return Possible
    else :
        return False

def Rotation(xanti,yanti,xhor,yhor,xpos,ypos,playmap,ligne,colonne):
    if dicoFleche['anti'].get_rect().move(xanti, yanti).collidepoint(xpos, ypos) and playmap[ligne][
        colonne] % 100 // 10 != 6:
        if playmap[ligne][colonne] % 10 == 1:
            playmap[ligne][colonne] += 3
        else:
            playmap[ligne][colonne] -= 1
        x = 1
        return 1
    if dicoFleche['hor'].get_rect().move(xhor, yhor).collidepoint(xpos, ypos) and playmap[ligne][
        colonne] % 100 // 10 != 6:
        if playmap[ligne][colonne] % 10 == 4:
            playmap[ligne][colonne] -= 3
        else:
            playmap[ligne][colonne] += 1
        x = 1
        return  1


def Win(maSurface,joueur):
    maSurface = pygame.display.set_mode((1440, 810))
    clicToPlay = False

    jouer = True
    while jouer:
        ####Debut de partie ####





        xhover, yhover = pygame.mouse.get_pos()
        maSurface.blit(pygame.image.load('img/WallpaperFin.png'), (0, 0))

        fontObj = pygame.font.SysFont('font/COPRGTL.TTF', 55)
        texteSurface = fontObj.render('Le joueur {} a gagné'.format(joueur-1), True, (176, 58, 46), None)
        maSurface.blit(texteSurface, (540, 300))
        if xhover > 600 and yhover > 400 and xhover < 800 and yhover < 452:
            TextMenuColor(maSurface, 'Rejouer', 600, 400, 'marronC', 60)
        else:
                TextMenuColor(maSurface, 'Rejouer', 600, 400, 'marronF', 60)
        if xhover > 600 and yhover > 500 and xhover < 845 and yhover < 552:
                TextMenuColor(maSurface, 'Quitter', 600, 500, 'marronC', 60)
        else:
            TextMenuColor(maSurface, 'Quitter', 600, 500, 'marronF', 60)



        for event in pygame.event.get():

            if event.type == QUIT:
                jouer = False

            if  event.type == MOUSEBUTTONDOWN:
                sonClic.play()

                if event.button == 1:
                    if xhover > 600 and yhover > 400 and xhover < 800 and yhover < 452 :
                        return "menu"

                    if xhover > 600 and yhover > 500 and xhover < 845 and yhover < 552:
                        jouer = False
        pygame.display.update()
    return "quit"


KhetGUI()