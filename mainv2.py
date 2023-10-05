from imports import *

### PYGAME SETUP

pygame.init()
width = 1280
height = 720
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

###  Police d'écritures

font = pygame.font.SysFont(None, 100)
font2 = pygame.font.SysFont(None, 20)

### VARIABLES

etat = "acceuil"
close = False

current_ennemies = []
emplacements = [emplacement.emplacement((220, 142)), emplacement.emplacement((220, 346)), emplacement.emplacement((220, 540)), emplacement.emplacement((460, 62)), emplacement.emplacement((460, 262)), emplacement.emplacement((460, 460)), emplacement.emplacement((730, 300)), emplacement.emplacement((730, 500)), emplacement.emplacement((826, 20)), emplacement.emplacement((976, 156))]
current_bullet = []
current_button = []
vagues = [vague.Vague([1, 2, 3, 4, 5, 30, 33, 36, 37, 150, 170, 171, 172, 173, 174, 175], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])]
current_vague = 0

money = 500
life = 100
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

        if event.type == pygame.MOUSEBUTTONDOWN:
            if cooldown < 0:
                if 416 < mouse[0] <= 880 and 320 < mouse[1] <= 488:
                    cooldown = 20
                    etat = "game"
                    f_count = 0
                    print("clicked")

        if 416 < mouse[0] <= 880 and 320 < mouse[1] <= 488:
            current_bg = menu_img_clicked
        else :
            current_bg = menu_img
#### FIN ACCEUIL


#### ETAT == GAME
    elif etat == "game":

        current_bg = bg_img

        if current_vague >= len(vagues) and current_ennemies == []:

            etat = "acceuil"

            for v in vagues:
                v.reset()
                current_vague = 0

            for e in emplacements:
                e.reset()

        elif current_vague < len(vagues):

            enn = vagues[current_vague].nextFrame()
            if enn == -1:
                current_vague += 1

            elif enn == 1:
                current_ennemies.append(ennemies.classique([0, 550]))

        for e in emplacements:
            e.display(screen, mouse)


### FIN GAME



    elif etat == "pause":
        pass
    elif etat == "game_over":
        pass
    elif etat == "map":
        pass
    elif etat == "arbre":
        pass
    elif etat =="credits":
        pass
    
    cooldown -= 1
    f_counter +=1

    pygame.display.flip()
    dt = clock.tick(30) / 1000

pygame.quit()
