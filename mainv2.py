from imports import *
pygame.mixer.set_num_channels(20)

def affichageHUD (vie, money, actual_wave, screen):
    life = font.render(str(vie), True, "red")
    screen.blit(life, (1090,660))

    moneyTxT = font.render(str(money), True, "yellow")
    screen.blit(moneyTxT, (0,0))

    vagueTxT = font.render(str(actual_wave+1), True, "purple")
    screen.blit(vagueTxT, (0,60))

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

actual_level = None

f_counter = 0

cooldown = 0

current_bg = menu_img


while not close:
    screen.blit(current_bg,(0,0))
    mouse = pygame.mouse.get_pos()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close = True



#### ETAT == ACCEUIL
    if etat == "acceuil":
        if f_counter == 0:
            pygame.mixer.music.load('effects/tests/bg_music2.mp3')
            pygame.mixer.music.set_volume(0.1)
            pygame.mixer.music.play(-1)

        if 416 < mouse[0] <= 880 and 320 < mouse[1] <= 488:
            current_bg = menu_img_clicked
        else :
            current_bg = menu_img

        if event.type == pygame.MOUSEBUTTONDOWN:
            if cooldown < 0:
                if 416 < mouse[0] <= 880 and 320 < mouse[1] <= 488:
                    hover_button_sound.play()
                    start_sound.play()
                    cooldown = 20
                    etat = "game"
                    actual_level = niveau.Niveau1()
                    current_bg = actual_level.bg

#### FIN ACCEUIL


#### ETAT == GAME
    elif etat == "game":


        if actual_level.f_counter == 0:
            pygame.mixer.music.load(actual_level.game_music)
            pygame.mixer.music.set_volume(0.1)
            pygame.mixer.music.play(-1)

        
        if event.type == pygame.MOUSEBUTTONDOWN and cooldown <= 0:
            cooldown = 5
            for e in actual_level.emplacements:
                actual_level.money -= e.click(actual_level.money, mouse)
            actual_level.obj.click(mouse)
            actual_level.next_button.click(mouse)


        if actual_level.actual_wave >= len(actual_level.vagues) and actual_level.ennemies == []:
            actual_level = None
            f_counter = 0
            etat = "win"

        elif actual_level.actual_wave < len(actual_level.vagues):

            enn = actual_level.vagues[actual_level.actual_wave].nextFrame()

            if enn == -1:
                actual_level.next_button.display(mouse, screen)

                if actual_level.next_button_state:
                    actual_level.money += actual_level.recompense[actual_level.actual_wave]
                    actual_level.actual_wave += 1
                    actual_level.next_button_state = False
                    pygame.mixer.Sound.play(new_wave_sound)

            elif enn > 0:

                if enn > len(Liste_ennemies):
                    enn = 1

                created_ennemie = generateEnemie(Liste_ennemies[enn -1], actual_level, actual_level.start)

                actual_level.ennemies.append( created_ennemie )

        for i in range(len(actual_level.bullets)-1, -1, -1):
            b = actual_level.bullets[i]
            ret = b.update(screen, actual_level.ennemies, actual_level.f_counter)

            if ret:
                actual_level.bullets.pop(i)

        for e in actual_level.emplacements:
            e.display(screen, mouse, actual_level.money, font2)

            bull = e.event(actual_level.f_counter, actual_level.ennemies, actual_level)

            if bull != None:
                actual_level.bullets.append(bull)

        bull = actual_level.obj.attack(actual_level.ennemies, actual_level.f_counter, actual_level.plus_loins)
        if bull != None:
                actual_level.bullets.append(bull)

        for i in range(len(actual_level.ennemies)-1, -1, -1):
            e = actual_level.ennemies[i]

            if e.vie > 0:
                deg = e.display(screen, font2 , actual_level.f_counter, Liste_ennemies, actual_level, actual_level.ennemies, actual_level.bullets)
                actual_level.vie -= deg

            else:
                actual_level.money += e.valeur
                actual_level.ennemies.pop(i)



        actual_level.obj.display(screen, actual_level.money, mouse, font3)

        ##[03/11] Affichage centralisé dans une fonction (voir dans une classe ?)
        affichageHUD (actual_level.vie, actual_level.money, actual_level.actual_wave, screen)


        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            if cooldown<0:
                cooldown = 5
                etat = "pause"
                hover_button_sound.play()
                current_bg = pause_bg

        actual_level.f_counter += 1

        
        if actual_level.vie < 0:
            etat = "game_over"
            actual_level = None



### FIN GAME



    elif etat == "pause":
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            if cooldown<0:
                cooldown = 5
                etat = "game"
                current_bg = bg_img
                hover_button_sound.play()


    elif etat == "game_over":
        screen.blit(game_over,(0,0))
        if f_counter > 90:
            etat = "acceuil"

    elif etat == "win":
        actual_level.obj.display(screen, 0, mouse, font3)
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
