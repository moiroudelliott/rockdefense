### MODULES
import pygame
import math as m

### PYGAME SETUP
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
close = False
game = "menu"
font = pygame.font.SysFont(None, 100)
font2 = pygame.font.SysFont(None, 20)

### FICHIERS

## images
bg_img = pygame.image.load("textures/bg/map1.png")

menu_img = pygame.image.load("textures/bg/menu_1.png")
menu_img_clicked = pygame.image.load("textures/bg/menu_1_clicked.png")

obj_img = pygame.image.load("textures/sprites/towers/cristal.png")
obj_img = pygame.transform.scale(obj_img,(200, 210))

ennemis_img = pygame.image.load("textures/sprites/ennemies/ennemy_tank.png")
ennemis2_img = pygame.image.load("textures/sprites/ennemies/ennemy_fast.png")
ennemis3_img = pygame.transform.scale(ennemis_img,(90, 90))

button_img = pygame.image.load("textures/sprites/emp/button.png")
button_pushed_img = pygame.image.load("textures/sprites/emp/button_pushed.png")
button_clicked_img = pygame.image.load("textures/sprites/emp/button_clicked.png")
button_clicked_pushed_img = pygame.image.load("textures/sprites/emp/button_clicked_pushed_1.png")

rock_img = pygame.image.load("textures/sprites/towers/rock_lvl1.png")
rock_bullet_img = pygame.image.load("textures/sprites/towers/bullets/rock_bullet1.png")

## sons

### VARIABLE
vague1 = [1, 1, 3, 1, 1, 1, 1, 2, 2,2, 2, 1, 1, 2, 2, 2, 2, 2, 0]
vague_timer1 = [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, ]
f_counter = 0
current = []
degats = 0
vie = 500
width = screen.get_width()
height = screen.get_height()
pos_emplacement = [(220, 142), (220, 346), (220, 540), (460, 62), (460, 262), (460, 460), (730, 300), (730, 500), (826, 20), (976, 156)]
pushed = [False, None]
troupes = []
money = 500
bullet_list = []
key_pressed = 0

### FONCTIONS
def vague_checker(vague_timer, f_counter):
    res = -1
    for i in range(len(vague_timer)):
        if vague_timer[i] == f_counter:
            res = i
    return res

def update(ennemis):
    pos = ennemis[1]
    if ennemis[0]==1:
        vit = 2
    elif ennemis[0]==2:
        vit = 3
    else:
        vit = 1
    deg_incr = 0
    if pos[0]<140:
        pos[0] += vit
    elif pos[1] > 80 and  pos[0]<350:
        pos[1] -= vit
    elif pos[0]<390:
        pos[0] += vit
    elif pos[1] < 610 and pos[0] < 650:
         pos[1] += vit
    elif pos[0] < 650:
         pos[0] += vit
    elif pos[1] > 40 and  pos[0]<655:
        pos[1] -= vit
    elif pos[0] < 1080:
        pos[0] +=vit
        pos[1] +=vit
    else : 
        deg_incr += 1
    ennemis[1] = pos
    return deg_incr

def emplacement(x, y):
    if x <= mouse[0] <= x+128 and y <= mouse[1] <= y+128:
        screen.blit(button_pushed_img, (x, y)) 
    else:
        screen.blit(button_img, (x, y)) 

def check_pos(mouse, pos, troupes):
    res = -1
    for i in range(len(pos)):
        if i not in troupes:
            if pos[i][0] <= mouse[0] <= pos[i][0]+128 and pos[i][1] <= mouse[1] <= pos[i][1]+128:
                res = i
    return res

def troupe_proche(current, troupe, pos_emplacement):
    for i in range(len(current)):
        el = current[i]
        pos_el = el[1]
        pos_troupe = (pos_emplacement[troupe][0]+64, pos_emplacement[troupe][1]+64)

        dif_x = m.sqrt((pos_el[0] - pos_troupe[0])**2)
        dif_y = m.sqrt((pos_el[1] - pos_troupe[1])**2)

        dist = dif_x + dif_y

        if dist < 300:
            return i

    return -1

def update_bullet(bullet):
    pos = bullet[0]
    obj = bullet[1][1]
    res = False

    dif_x = m.sqrt((pos[0] - obj[0])**2)
    dif_y = m.sqrt((pos[1] - obj[1])**2)

    dist = dif_x + dif_y

    if pos[0]>obj[0] and pos[1]>obj[1]:
        pos[0] -= int((dif_x/dist)*20)
        pos[1] -= int((dif_y/dist)*20)
    elif pos[0]<obj[0] and pos[1]>obj[1]:
        pos[0] += int((dif_x/dist)*20)
        pos[1] -= int((dif_y/dist)*20)
    elif pos[0]>obj[0] and pos[1]<obj[1]:
        pos[0] -= int((dif_x/dist)*20)
        pos[1] += int((dif_y/dist)*20)
    else: 
        pos[0] += int((dif_x/dist)*20)
        pos[1] += int((dif_y/dist)*20)

    if dist <= 20:
        res = True
    
    return res




### GAME
while not close:

    mouse = pygame.mouse.get_pos()
    if game == "menu":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if 416 < mouse[0] <= 880 and 320 < mouse[1] <= 488:
                    game = "game"
                    f_count = 0

        if 416 < mouse[0] <= 880 and 320 < mouse[1] <= 488:
            screen.blit(menu_img_clicked,(0,0))
        else :
            screen.blit(menu_img,(0,0))

    elif game == "over":
        game = "menu"
    elif game == "game":
        screen.blit(bg_img,(0,0))
        screen.blit(obj_img,(1050,450))

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            if key_pressed<0:
                current.append([1, [0, 550], 200])
                key_pressed = 10
        if keys[pygame.K_DOWN]:
            if key_pressed < 0:
                current.append([2, [0, 550], 40])
                key_pressed = 10
        if keys[pygame.K_LEFT]:
            if key_pressed < 0:
                current.append([3, [0, 550], 1000])
                key_pressed = 10

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close = True
            if event.type == pygame.MOUSEBUTTONDOWN:

                if pushed[0]:
                    x = pos_emplacement[pushed[1]][0]
                    y = pos_emplacement[pushed[1]][1]
                    if x <= mouse[0] <= x+128 and y <= mouse[1] <= y+32:
                        if money >= 100:
                            troupes.append(pushed[1])
                            pushed = [False, None]
                            money -= 100

                i = check_pos(mouse, pos_emplacement, troupes)
                if i >= 0:
                    pushed = [True, i]
                else :
                    pushed = [False, None]

        for i in range(len(pos_emplacement)):
            emp = pos_emplacement[i]
            x = emp[0]
            y = emp[1]

            if i in troupes:
                screen.blit(rock_img, (x, y)) 

        
            elif pushed[0] and pushed[1] == i:
                if x <= mouse[0] <= x+128 and y <= mouse[1] <= y+32:
                    if money >= 100:
                        screen.blit(button_clicked_pushed_img, (x, y)) 
                    else: 
                        screen.blit(button_clicked_img, (x, y)) 
                else:
                    screen.blit(button_clicked_img, (x, y)) 

            else:
                emplacement(emp[0], emp[1])

            


        if vague1[vague_checker(vague_timer1, f_counter)] == 1:
            current.append([1, [0, 550], 100])
        if vague1[vague_checker(vague_timer1, f_counter)] == 2:
            current.append([2, [0, 550], 40])
        if vague1[vague_checker(vague_timer1, f_counter)] == 3:
            current.append([3, [0, 550], 1000])

        if f_counter%30 == 0:
            for troupe in troupes:
                proche = troupe_proche(current, troupe, pos_emplacement)
                if proche >= 0:
                    bullet_list.append([[pos_emplacement[troupe][0]+64, pos_emplacement[troupe][1]+64], current[proche]])

        for ennemis in current:
            if ennemis[0] == 1:
                screen.blit(ennemis_img, ennemis[1])
            elif ennemis[0] == 2:
                screen.blit(ennemis2_img, ennemis[1])
            elif ennemis[0] == 3:
                screen.blit(ennemis3_img, ennemis[1])
            vie_ennemis = font2.render(str(ennemis[2]), True, "red")
            screen.blit(vie_ennemis, (ennemis[1][0],ennemis[1][1]-10))
            deg_incr = update(ennemis)
            degats += deg_incr

        if f_counter % 30 == 0:
            vie -= degats
        
        pop = []
        for i in range(len(bullet_list)):
            bullet = bullet_list[i]
            screen.blit(rock_bullet_img, (bullet[0][0],bullet[0][1]))
            a = update_bullet(bullet)
            if a:
                bullet[1][2] -= 20
                pop.append(i)
        for i in range(len(pop), 0, -1):
                bullet_list.pop(pop[i-1])
                pop2 = []
                for i in range(len(current)):
                    if current[i][2] <= 0:
                        pop2.append(i)
                for i in range(len(pop2), 0, -1):
                    current.pop(pop2[i-1])
                    money += 20

        
        life = font.render(str(vie), True, "red")
        screen.blit(life, (1090,660))

        moneyTxT = font.render(str(money), True, "yellow")
        screen.blit(moneyTxT, (0,0))
        degats = 0
        if vie <= 0:
            vie = 500
            current = []
            game = "over"

    key_pressed -= 1
    pygame.display.flip()
    f_counter +=1
        
    dt = clock.tick(30) / 1000



