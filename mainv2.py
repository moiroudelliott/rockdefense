from imports import *
# import random as r

# def gerateEnemie (classe, actual_level):
#     listeCoordonneAleatoire = [0, r.randint(500, 670)]
#     res = classe(listeCoordonneAleatoire, actual_level)
#     return res

def affichageHUD (vie, money, current_vague, screen):
    life = font.render(str(vie), True, "red")
    screen.blit(life, (1090,660))

    moneyTxT = font.render(str(money), True, "yellow")
    screen.blit(moneyTxT, (0,0))

    vagueTxT = font.render(str(current_vague+1), True, "purple")
    screen.blit(vagueTxT, (0,60))

##[03/11]Mettre Liste_ennemies dans le fichier imports ?
# Liste_ennemies = [ennemies.classique, ennemies.tank, ennemies.rapide]

### PYGAME SETUP

pygame.init()
width = 1280
height = 720
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

###  Police d'écritures

font = pygame.font.SysFont(None, 100)
font2 = pygame.font.SysFont(None, 20)
font3 = pygame.font.SysFont(None, 40)

### VARIABLES

etat = "acceuil"
close = False

actual_level = niveau.Niveau1()
current_ennemies = []
current_bullet = []
current_button = []
vagues = actual_level.vagues
emplacements = actual_level.emplacements
current_vague = 0

money_init = actual_level.money_init
money = money_init

vie_init = actual_level.vie_init
vie = vie_init

f_counter = 0
cooldown = 0

obj = tours.obj([1050,450]) # Cristal

current_bg = menu_img

def reset(money_max, vagues, emplacements, vie_max):
    global money
    global current_ennemies
    global current_bullet
    global current_vague
    global vie

    money = money_max
    current_ennemies = []
    current_bullet = []

    for e in emplacements:
        e.reset()

    for v in vagues:
        v.reset()

    vie = vie_max
    current_vague = 0

while not close:
    screen.blit(current_bg,(0,0))
    mouse = pygame.mouse.get_pos()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close = True



#### ETAT == ACCEUIL
    if etat == "acceuil":

        if event.type == pygame.MOUSEBUTTONDOWN:
            if cooldown < 0:
                if 416 < mouse[0] <= 880 and 320 < mouse[1] <= 488:
                    cooldown = 20
                    etat = "game"
                    f_count = 0

        if 416 < mouse[0] <= 880 and 320 < mouse[1] <= 488:
            current_bg = menu_img_clicked
        else :
            current_bg = menu_img
#### FIN ACCEUIL


#### ETAT == GAME
    elif etat == "game":

        if f_counter %10 == 0:current_ennemies = actual_level.tri_ennemis(c.copy(current_ennemies))
        current_bg = bg_img

        if event.type == pygame.MOUSEBUTTONDOWN and cooldown <= 0:
            cooldown = 5
            for e in emplacements:
                money -= e.click(money, mouse)
            obj.click(mouse)
            actual_level.next_button.click()


        if current_vague >= len(vagues) and current_ennemies == []:

            reset(money_init, vagues, emplacements, vie_init)
            f_counter = 0
            etat = "win"
            '''
            for v in vagues:
                v.reset()
                current_vague = 0

            for e in emplacements:
                e.reset()
            '''

        elif current_vague < len(vagues):

            enn = vagues[current_vague].nextFrame()
            ### à la place de if elif mettre ennemies dans une liste et faire Ce.append(Liste ennemies[i])
            ##[03/11]Fait
            # print(enn)
            if enn == -1:
                actual_level.next_button.display(mouse, screen)
                if actual_level.next_button_state:
                    money += actual_level.recompense[current_vague]
                    current_vague += 1
                    actual_level.next_button_state = False
            elif enn > 0:
                if enn > len(Liste_ennemies):
                    enn = 1

                created_ennemie = generateEnemie(Liste_ennemies[enn -1], actual_level)
                # print(created_ennemie)

                current_ennemies.append( created_ennemie )

            # elif enn == 1:
            #     current_ennemies.append(ennemies.classique([0, r.randint(500, 670)], actual_level))
            #
            # elif enn == 2:
            #     current_ennemies.append(ennemies.tank([0, r.randint(500, 670)], actual_level))
            #
            # elif enn == 3:
            #     current_ennemies.append(ennemies.rapide([0, r.randint(450, 600)], actual_level))

        for i in range(len(current_bullet)-1, -1, -1):
            b = current_bullet[i]
            ret = b.update(screen, current_ennemies, f_counter)
            # (self, CanvasParent, ennemis, timer)

            if ret:
                current_bullet.pop(i)

        # print( current_bullet )

        for e in emplacements:
            e.display(screen, mouse, money, font2)
            bull = e.event(f_counter, current_ennemies)
            if bull != None:
                current_bullet.append(bull)

        bull = obj.attack(current_ennemies, f_counter)
        if bull != None:
                current_bullet.append(bull)

        for i in range(len(current_ennemies)-1, -1, -1):

            e = current_ennemies[i]
            # print(e.etat['vitesse'])
            # print( e.vitesse * e.coefficientEtat( 'vitesse' ) )

            if e.vie > 0:
                deg = e.display(screen, font2 , f_counter, Liste_ennemies, actual_level, current_ennemies, current_bullet)
                # degat = e.degat
                ## Mettre couldown
                vie -= deg
            else:
                money += e.valeur
                current_ennemies.pop(i)





        if vie < 0:
            etat = "game_over"
            f_counter = 0
            reset(money_init, vagues, emplacements, vie_init)

        obj.display(screen, money, mouse, font3)

        ##[03/11] Affichage centralisé dans une fonction (voir dans une classe ?)
        affichageHUD (vie, money, current_vague, screen)


        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            if cooldown<0:
                cooldown = 5
                etat = "pause"
                current_bg = pause_bg



### FIN GAME



    elif etat == "pause":
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            if cooldown<0:
                cooldown = 5
                etat = "game"
                current_bg = bg_img


    elif etat == "game_over":
        obj.display(screen, 0, mouse, font3)
        screen.blit(game_over,(0,0))
        if f_counter > 90:
            etat = "acceuil"

    elif etat == "win":
        obj.display(screen, 0, mouse, font3)
        screen.blit(win_text,(0,0))
        if f_counter > 90:
            etat = "acceuil"

    elif etat == "map":
        pass
    elif etat == "arbre":
        pass
    elif etat == "livre":
        pass
    elif etat =="credits":
        pass

    cooldown -= 1
    f_counter +=1

    pygame.display.flip()
    dt = clock.tick(30) / 1000

pygame.quit()
