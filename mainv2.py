from imports import *
pygame.mixer.set_num_channels(20)

## Stats
statistique = stats.statistique()
statistique.importToJson()

def affichageHUD (vie, money, actual_wave, screen, actual_level):
    life = font.render(str(vie), True, "red")
    screen.blit(life, actual_level.pos_life)

    moneyTxT = font.render(str(money), True, "yellow")
    screen.blit(moneyTxT, (0,0))

    vagueTxT = font.render(str(actual_wave+1), True, "purple")
    screen.blit(vagueTxT, (0,60))

    timeTxT = str(int(t.time())-actual_level.start_time)
    timeSurface = font.render(timeTxT, True, "blue")
    screen.blit(timeSurface, (1280-len(timeTxT)*40,0))


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

def quit_fct():
    global etat
    global actual_level
    global current_bg
    etat = "map"
    actual_level = None
    current_bg = map

## §§§
etat = "statistique"

while not close:
    screen.blit(current_bg,(0,0))
    mouse = pygame.mouse.get_pos()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close = True



#### ETAT == ACCEUIL
    if etat == "acceuil":
        if f_counter == 0:
            #Initialise la musique
            pygame.mixer.music.load('effects/tests/bg_music2.mp3')
            pygame.mixer.music.set_volume(0.1)
            pygame.mixer.music.play(-1)

        if 416 < mouse[0] <= 880 and 320 < mouse[1] <= 488:
            current_bg = menu_img_clicked
        else :
            current_bg = menu_img

        if event.type == pygame.MOUSEBUTTONDOWN:
            if cooldown < 0:
                #clic du bouton
                if 416 < mouse[0] <= 880 and 320 < mouse[1] <= 488:
                    hover_button_sound.play()
                    start_sound.play()
                    cooldown = 20
                    etat = "map"
                    current_bg = map

#### FIN ACCEUIL


#### ETAT == GAME
    elif etat == "game":
        statistique.importToJson()


        if actual_level.f_counter == 0:
            #initialisation musique
            pygame.mixer.music.load(actual_level.game_music)
            pygame.mixer.music.set_volume(0.1)
            pygame.mixer.music.play(-1)

        #Boucle sur els emplacements (et les tours)
        for e in actual_level.emplacements:
            # Affichage de l'emplacement (ou de la tour)
            e.display(screen, mouse, actual_level.money, font2)

            # Récupération du nouveau bullet créer par cet emplacement s'il y en à un
            bull = e.event(actual_level.f_counter, actual_level.ennemies, actual_level)

            # Si un bullet à été récupéré on l'ajoute à la liste des bullets
            if bull != None:
                actual_level.bullets.append(bull)

        # Si le bouton est préssé
        if event.type == pygame.MOUSEBUTTONDOWN and cooldown <= 0:
            # On augmente le cooldown (pour pas avoir des clics en boucle)
            cooldown = 5

            # On tourne dans les emplacements
            for e in actual_level.emplacements:
                # On ajoute ou pas un tour
                event_e = e.click(actual_level.money, mouse)
                actual_level.money -= event_e

                ## Stats (!!! ici ça fonctionne pas il faut le faire que quand le clic nous à couter de l'argent event_e > 0)
                if ( event_e > 0 ):
                    statistique.set_nombreTourConstruite( statistique.get_nombreTourConstruite() +1 )

            # On fait pareil pour l'bjectif
            actual_level.obj.click(mouse)
            actual_level.next_button.click(mouse)


            if actual_level.rock_fall_default_pos[0] < mouse[0] < actual_level.rock_fall_default_pos[0] + 48 and actual_level.rock_fall_default_pos[1] < mouse[1] < actual_level.rock_fall_default_pos[1] + 48:
                if actual_level.rock_clicked:
                    actual_level.rock_clicked = False
                elif actual_level.rock_cooldown ==0:
                    actual_level.rock_clicked = True
            else:
                if actual_level.rock_clicked:
                    actual_level.rock_cooldown =actual_level.rock_cooldown_default
                    actual_level.rock_clicked = False
                    actual_level.bullets.append(bullet.rock_fall((mouse[0]+48, mouse[1]+48), mouse))




        # On boucle sur tous les ennemis
        for i in range(len(actual_level.ennemies)-1, -1, -1):
            e = actual_level.ennemies[i]

            # S'il à encore de la vie on l'affiche
            if e.vie > 0:
                deg = e.display(screen, font2 , actual_level.f_counter, Liste_ennemies, actual_level, actual_level.ennemies, actual_level.bullets)
                # On enlève des dégats à notre objectif
                actual_level.vie -= deg

                ## Stats
                statistique.set_viePerdu( statistique.get_viePerdu() + deg )

            else:
                # On ajout la valeur de l'ennemis à notre argent
                actual_level.money += e.valeur

                ## Stats
                statistique.set_argentTotale( statistique.get_argentTotale() +e.valeur )
                statistique.set_nombreTotalEnnemieTuer( statistique.get_nombreTotalEnnemieTuer() +1 )

                # print(actual_level.ennemies[i].nom)

                ennemieInStat = statistique.get_detailNombreTotalEnnemieTuer().get(actual_level.ennemies[i].nom, 0)
                statistique.detailNombreTotalEnnemieTuer[actual_level.ennemies[i].nom] = ennemieInStat +1

                # On supprime l'ennemis de notre liste
                actual_level.ennemies.pop(i)

        # On tourne à l'enver dans les bulllets
        for i in range(len(actual_level.bullets)-1, -1, -1):
            #On les affiches et on les updates
            b = actual_level.bullets[i]
            ret = b.update(screen, actual_level.ennemies, actual_level.f_counter)

            # On les supprime de la liste des bullets si elles ont atenit leurs objectif
            if ret:
                actual_level.bullets.pop(i)


        # On effectue l'action d'attaque de l'bjectif
        bull = actual_level.obj.attack(actual_level.ennemies, actual_level.f_counter, actual_level.plus_loins)
        if bull != None:
                actual_level.bullets.append(bull)

        # On augmente le comptage de frame
        actual_level.f_counter += 1

        # On affiche l'bjectif
        actual_level.obj.display(screen, actual_level.money, mouse, font3)

        if not actual_level.rock_clicked:
            if actual_level.rock_cooldown == 0:
                screen.blit(actual_level.rock_fall_small_img, actual_level.rock_fall_default_pos)
            else:
                screen.blit(actual_level.rock_fall_small_img_op, actual_level.rock_fall_default_pos)
                actual_level.rock_cooldown -= 1
        else:
            screen.blit(actual_level.rock_fall_img, (mouse[0]-48, mouse[1]-48))

        ##[03/11] Affichage centralisé dans une fonction (voir dans une classe ?)
        affichageHUD (actual_level.vie, actual_level.money, actual_level.actual_wave, screen, actual_level)

        # On vérifie si on a perdu
        if actual_level.vie < 0:
            # On réinitialise le compteur et on passe en état game over
            etat = "game_over"
            f_counter = 0
            actual_level = None

            ## Stats
            statistique.set_nombreDefaite( statistique.get_nombreDefaite() +1 )


        # Si le niveau actuel n'est pas finis
        if actual_level!= None:

            #On passe au prochain ennemis de la vague
            enn = actual_level.vagues[actual_level.actual_wave].nextFrame()

            #si la vague est finis
            if enn == -1:
                #Si le niveau est finis
                if actual_level.actual_wave >= len(actual_level.vagues)-1 and len(actual_level.ennemies) == 0:
                    temps = int(t.time())-actual_level.start_time
                    if type(actual_level)==niveau.Niveau1:
                        statistique.victoirelvl1 = True
                        if (temps < statistique.tempslvl1 or statistique.tempslvl1 == -1 ):
                            statistique.tempslvl1 = temps
                    if type(actual_level)==niveau.Niveau2:
                        statistique.victoirelvl2 = True
                        if (temps < statistique.tempslvl2 or statistique.tempslvl2 == -1 ):
                            statistique.tempslvl2 = temps
                    #On passe à l'état de victoire
                    actual_level = None
                    f_counter = 0
                    etat = "win"

                    ## Stats
                    statistique.set_nombreVictoire( statistique.get_nombreVictoire() +1 )
                # Si il reste des vagues dans le niveau
                elif actual_level.actual_wave < len(actual_level.vagues)-1:
                    #On affiche le bouton de la vague suivante
                    actual_level.next_button.display(mouse, screen)
                    #On vérifie si le bouton est préssé
                    if actual_level.next_button_state:
                        actual_level.money += actual_level.recompense[actual_level.actual_wave]
                        actual_level.actual_wave += 1
                        actual_level.next_button_state = False
                        pygame.mixer.Sound.play(new_wave_sound)

            # Si un ennemis doit appraitre
            elif enn > 0:
                # On génère notre ennemis
                if enn > len(Liste_ennemies):
                    enn = 1

                created_ennemie = generateEnemie(Liste_ennemies[enn -1], actual_level, actual_level.start)

                actual_level.ennemies.append( created_ennemie )


            # Menu pause
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                if cooldown<0:
                    cooldown = 5
                    etat = "pause"
                    hover_button_sound.play()
                    current_bg = pause_bg







### FIN GAME



    elif etat == "pause":
        ## Stats
        statistique.exportToJSON()

        keys = pygame.key.get_pressed()
        bt = button.Button((20, 600), (200, 100), quit, quit, quit_fct)
        bt.display(mouse, screen)
        if event.type == pygame.MOUSEBUTTONDOWN:
            bt.click(mouse)
            cooldown = 20
        if keys[pygame.K_ESCAPE]:
            if cooldown<0:
                cooldown = 5
                etat = "game"
                current_bg = actual_level.bg
                hover_button_sound.play()

        if keys[pygame.K_UP]:
            if cooldown<0:
                actual_level.money += 500
                cooldown += 5



    elif etat == "game_over":
        screen.blit(game_over,(0,0))
        if f_counter > 90:
            etat = "map"
            current_bg = map

        ## Stats
        statistique.exportToJSON()

    elif etat == "win":
        screen.blit(win_text,(0,0))
        if f_counter > 90:
            etat = "map"
            current_bg = map
        statistique.exportToJSON()

    elif etat == "map":
        statistique.importToJson()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if cooldown < 0:
                if 91 < mouse[0] <= 188 and 294 < mouse[1] <= 393:
                    hover_button_sound.play()
                    start_sound.play()
                    cooldown = 20
                    actual_level=niveau.Niveau1()
                    etat = "game"
                    current_bg = actual_level.bg

                if 563 < mouse[0] <= 672 and 501 < mouse[1] <= 614:
                    hover_button_sound.play()
                    start_sound.play()
                    cooldown = 20
                    actual_level=niveau.Niveau2()
                    etat = "game"
                    current_bg = actual_level.bg
        if 91 < mouse[0] <= 188 and 294 < mouse[1] <= 393:
            screen.blit(label1, (84, 143))
            if statistique.tempslvl1 != -1:
                timeTxT = "Temps :"
                timeTxT2 = str(statistique.tempslvl1) + " s"
                timeSurface = font2.render(timeTxT, True, "red")
                timeSurface2 = font2.render(timeTxT2, True, "red")
                screen.blit(timeSurface, (107, 220))
                screen.blit(timeSurface2, (124-2*len(timeTxT2), 235))
            else:
                timeTxT = "Pas encore"
                timeTxT2 = "de temps"
                timeSurface = font2.render(timeTxT, True, "red")
                timeSurface2 = font2.render(timeTxT2, True, "red")
                screen.blit(timeSurface, (97, 220))
                screen.blit(timeSurface2, (105, 235))

        if 563 < mouse[0] <= 672 and 501 < mouse[1] <= 614:
            screen.blit(label2, (567, 357))
            if statistique.tempslvl2 != -1:
                timeTxT = "Temps :"
                timeTxT2 = str(statistique.tempslvl2) + " s"
                timeSurface = font2.render(timeTxT, True, "red")
                timeSurface2 = font2.render(timeTxT2, True, "red")
                screen.blit(timeSurface, (590, 434))
                screen.blit(timeSurface2, (607-2*len(timeTxT2), 449))
            else:
                timeTxT = "Pas encore"
                timeTxT2 = "de temps"
                timeSurface = font2.render(timeTxT, True, "red")
                timeSurface2 = font2.render(timeTxT2, True, "red")
                screen.blit(timeSurface, (580, 434))
                screen.blit(timeSurface2, (587, 449))


        if not statistique.victoirelvl1:
            screen.blit(boss1, (74, 293))

        if not statistique.victoirelvl2:
            screen.blit(boss2, (567, 507))

    ## Ecran stats
    elif etat == "statistique":
        # background à changer ?
        current_bg = bg_stats

        TextExitToMap = font3.render('Aller à la carte', True, (255,0,0) )
        screen.blit(TextExitToMap, (20, 20))

        # click retour map
        if event.type == pygame.MOUSEBUTTONDOWN:
            if cooldown < 0:
                # +20 par rapport au blit de TextExitToMap
                if 20 < mouse[0] <= TextExitToMap.get_size()[0]+20 and 20 < mouse[1] <= TextExitToMap.get_size()[1]+20:
                    hover_button_sound.play()
                    start_sound.play()
                    cooldown = 20
                    etat = "map"

    elif etat == "livre":
        pass
    elif etat =="credits":
        pass

    cooldown -= 1
    f_counter +=1

    pygame.display.flip()
    dt = clock.tick(30) / 1000

## Stats
statistique.exportToJSON()

pygame.quit()