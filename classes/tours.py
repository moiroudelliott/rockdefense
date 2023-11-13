import pygame
import math as m
import classes.bullet as b

rock_img1 = pygame.image.load("textures/sprites/towers/rock_lvl1.png")
rock_img2 = pygame.image.load("textures/sprites/towers/rock_lvl2.png")
rock_img3 = pygame.image.load("textures/sprites/towers/rock_lvl3.png")
rock_img4 = pygame.image.load("textures/sprites/towers/rock_lvl4.png")

rock_hover = pygame.image.load("textures/sprites/towers/amelioration.png")
rock_hover2 = pygame.image.load("textures/sprites/towers/amelioration_alt.png")

obj_img = pygame.image.load("textures/sprites/towers/cristal.png")
obj_img = pygame.transform.scale(obj_img,(200, 210))
obj_hover = pygame.image.load("textures/sprites/towers/obj_amelioration.png")
obj_hover2 = pygame.image.load("textures/sprites/towers/obj_amelioration_alt.png")

radio_img1 = pygame.image.load("textures/sprites/towers/radio_lvl1.png")
radio_img2 = pygame.image.load("textures/sprites/towers/radio_lvl2.png")
radio_img3 = pygame.image.load("textures/sprites/towers/radio_lvl3.png")
radio_img4 = pygame.image.load("textures/sprites/towers/radio_lvl4.png")

cristal_img1 = pygame.image.load("textures/sprites/towers/cristal_lvl1.png")
cristal_img2 = pygame.image.load("textures/sprites/towers/cristal_lvl2.png")
cristal_img3 = pygame.image.load("textures/sprites/towers/cristal_lvl3.png")
cristal_img4 = pygame.image.load("textures/sprites/towers/cristal_lvl4.png")

class Pierre:
    def __init__(self, pos):
        self.sprite = rock_img1
        self.bullet = [b.rock1, b.rock1, b.rock2, b.rock3]
        self.type_degat = "physique"
        self.niveau = 1
        self.hover = False
        self.hover_sprite = rock_hover
        self.hover_sprite_alt = rock_hover2
        self.realpos = pos
        self.pos = [self.realpos[0]+64, self.realpos[1]+64]
        self.prix = 70
        self.lvl_max = 4
        self.cooldown = 30
        self.range = 200
        self.upgrading = True
        self.next_up_price = 50


    def display(self, canvas, money, hover, font):

        canvas.blit(self.sprite, self.realpos)
        if self.next_up_price <= money:
            self.upgrading = True
        else:
            self.upgrading = False

        if hover:
            pygame.draw.circle(canvas, (255, 0, 0), self.pos, self.range-int(0.35*self.range), 2)
            if self.niveau < 4:
                prix = font.render(str(self.next_up_price), True, "yellow")
                canvas.blit(prix, (self.realpos[0], self.realpos[1]-15))
            if not self.upgrading:
                canvas.blit(self.hover_sprite_alt, self.realpos)
            else:
                canvas.blit(self.hover_sprite, self.realpos)


    def click(self, hover, mouse):
        m = 0
        if hover:
            if self.realpos[0] < mouse[0] < self.realpos[0] + 21 and self.realpos[1] < mouse[1] < self.realpos[1] + 21:
                if self.upgrading:
                    m = self.upgrade()

            if self.realpos[0] +107 < mouse[0] < self.realpos[0] + 128 and self.realpos[1] < mouse[1] < self.realpos[1] + 21:
                m = -self.prix
        
        return m
            

    def upgrade(self):
        self.niveau+=1
        if self.niveau ==2:
            self.sprite = rock_img2
            self.prix += 20
            self.range+=100
            self.cooldown -= 10
            res = self.next_up_price
            self.next_up_price = 100
        elif self.niveau == 3:
            self.sprite = rock_img3
            self.prix += 50
            res = self.next_up_price
            self.next_up_price = 200
        elif self.niveau ==4:
            self.sprite = rock_img4
            self.prix += 70
            self.range+=100
            self.cooldown -= 10
            self.next_up_price = 200
            res = self.next_up_price
            self.next_up_price = m.inf
            
        return res

    def sell(self):
        return self.prix

    def attack(self, ennemies_tab, timer):
        res = None
        if timer % self.cooldown == 0:
            found = False
            i = 0
            while not found and i < len(ennemies_tab):
                e = ennemies_tab[i]
                difx = abs(self.pos[0] - e.position[0])
                dify = abs(self.pos[1] - e.position[1])
                dist = difx + dify
                if self.range >= dist:
                    bullet = self.bullet[self.niveau-1](self.pos, e)
                    res =  bullet
                    found = True
                i +=1
        return res


class obj:    
    def __init__(self, pos):
        self.sprite = obj_img
        self.bullet = [b.rock3, b.rock3, b.rock3, b.rock3]
        self.type_degat = "physique"
        self.niveau = 1
        self.hover = False
        self.hover_sprite = obj_hover
        self.hover_sprite_alt = obj_hover2
        self.realpos = pos
        self.pos = [self.realpos[0]+100, self.realpos[1]+105]
        self.prix = 70
        self.lvl_max = 4
        self.cooldown = 30
        self.range = 400
        self.upgrading = True
        self.next_up_price = 40


    def display(self, canvas, money, mouse, font):

        self.hoverCheck(mouse)


        canvas.blit(self.sprite, self.realpos)
        if self.next_up_price <= money:
            self.upgrading = True
        else:
            self.upgrading = False

        if self.hover:
            pygame.draw.circle(canvas, (255, 0, 0), self.pos, self.range-int(0.35*self.range), 2)
            if self.niveau < 4:
                prix = font.render(str(self.next_up_price), True, "yellow")
                canvas.blit(prix, (self.realpos[0], self.realpos[1]-25))
            if not self.upgrading:
                canvas.blit(self.hover_sprite_alt, self.realpos)
            else:
                canvas.blit(self.hover_sprite, self.realpos)


    def click(self, mouse):
        m = 0
        if self.hover:
            if self.realpos[0] < mouse[0] < self.realpos[0] + 33 and self.realpos[1] < mouse[1] < self.realpos[1] + 34:
                if self.upgrading:
                    m = self.upgrade()
        
        return m
    
    def hoverCheck(self, mouse):
        if self.realpos[0] < mouse[0] < self.realpos[0]+200 and self.realpos[1] < mouse[1] < self.realpos[1]+210:
            self.hover = True
        else:
            self.hover = False
            

    def upgrade(self):
        self.niveau+=1
        if self.niveau ==2:
            res = self.next_up_price
            self.next_up_price = 80

            self.range+=100
            self.cooldown -= 10

        elif self.niveau == 3:
            res = self.next_up_price
            self.next_up_price = 120

            self.cooldown -= 10
            self.range+=50

        elif self.niveau ==4:
            res = self.next_up_price
            self.next_up_price = m.inf

            self.range += 70
            self.cooldown -= 5
            
        return res

    def sell(self):
        return self.prix

    def attack(self, ennemies_tab, timer):
        res = None
        if timer % self.cooldown == 0:
            found = False
            i = 0
            while not found and i < len(ennemies_tab):
                e = ennemies_tab[i]
                difx = abs(self.pos[0] - e.position[0])
                dify = abs(self.pos[1] - e.position[1])
                dist = difx + dify
                if self.range >= dist:
                    bullet = self.bullet[self.niveau-1](self.pos, e)
                    res =  bullet
                    found = True
                i +=1
        return res


class Radio:
    def __init__(self, pos):
        self.sprite = radio_img1
        self.bullet = [b.radio1, b.radio1, b.radio1, b.radio1]
        self.type_degat = "magique"
        self.niveau = 1
        self.hover = False
        self.hover_sprite = rock_hover
        self.hover_sprite_alt = rock_hover2
        self.realpos = pos
        self.pos = [self.realpos[0]+64, self.realpos[1]+64]
        self.prix = 90
        self.lvl_max = 4
        self.cooldown = 200
        self.range = 2000
        self.upgrading = True
        self.next_up_price = 50


    def display(self, canvas, money, hover, font):

        canvas.blit(self.sprite, self.realpos)
        if self.next_up_price <= money:
            self.upgrading = True
        else:
            self.upgrading = False

        if hover:
            if self.niveau < 4:
                prix = font.render(str(self.next_up_price), True, "yellow")
                canvas.blit(prix, (self.realpos[0], self.realpos[1]-15))
            if not self.upgrading:
                canvas.blit(self.hover_sprite_alt, self.realpos)
            else:
                canvas.blit(self.hover_sprite, self.realpos)


    def click(self, hover, mouse):
        m = 0
        if hover:
            if self.realpos[0] < mouse[0] < self.realpos[0] + 21 and self.realpos[1] < mouse[1] < self.realpos[1] + 21:
                if self.upgrading:
                    m = self.upgrade()

            if self.realpos[0] +107 < mouse[0] < self.realpos[0] + 128 and self.realpos[1] < mouse[1] < self.realpos[1] + 21:
                m = -self.prix
        
        return m
            

    def upgrade(self):
        self.niveau+=1
        if self.niveau ==2:
            self.sprite = radio_img2
            self.prix += 20
            self.range+=100
            self.cooldown -= 10
            res = self.next_up_price
            self.next_up_price = 100
        elif self.niveau == 3:
            self.sprite = radio_img3
            self.prix += 50
            res = self.next_up_price
            self.next_up_price = 150
        elif self.niveau == 4:
            self.sprite = radio_img4
            self.prix += 100
            res = self.next_up_price
            self.next_up_price = m.inf
            
        return res

    def sell(self):
        return self.prix

    def attack(self, ennemies_tab, timer):
        res = None
        if timer % self.cooldown == 0:
            bullet = self.bullet[self.niveau-1](self.pos, self.realpos)
            res =  bullet
        return res
    

class Cristal:
    def __init__(self, pos):
        self.sprite = cristal_img1
        self.bullet = [b.cristal1, b.cristal2, b.cristal2, b.cristal3]
        self.type_degat = "magique"
        self.niveau = 1
        self.hover = False
        self.hover_sprite = rock_hover
        self.hover_sprite_alt = rock_hover2
        self.realpos = pos
        self.pos = [self.realpos[0]+64, self.realpos[1]+64]
        self.prix = 150
        self.lvl_max = 4
        self.cooldown = 60
        self.range = 250
        self.upgrading = True
        self.next_up_price = 150


    def display(self, canvas, money, hover, font):

        canvas.blit(self.sprite, self.realpos)
        if self.next_up_price <= money:
            self.upgrading = True
        else:
            self.upgrading = False

        if hover:
            pygame.draw.circle(canvas, (255, 0, 0), self.pos, self.range-int(0.35*self.range), 2)
            if self.niveau < 4:
                prix = font.render(str(self.next_up_price), True, "yellow")
                canvas.blit(prix, (self.realpos[0], self.realpos[1]-15))
            if not self.upgrading:
                canvas.blit(self.hover_sprite_alt, self.realpos)
            else:
                canvas.blit(self.hover_sprite, self.realpos)


    def click(self, hover, mouse):
        m = 0
        if hover:
            if self.realpos[0] < mouse[0] < self.realpos[0] + 21 and self.realpos[1] < mouse[1] < self.realpos[1] + 21:
                if self.upgrading:
                    m = self.upgrade()

            if self.realpos[0] +107 < mouse[0] < self.realpos[0] + 128 and self.realpos[1] < mouse[1] < self.realpos[1] + 21:
                m = -self.prix
        
        return m
            

    def upgrade(self):
        self.niveau+=1
        if self.niveau ==2:
            self.sprite = cristal_img2
            self.prix += 100
            self.range+=50
            self.cooldown -= 15
            res = self.next_up_price
            self.next_up_price = 200
        elif self.niveau == 3:
            self.sprite = cristal_img3
            self.prix += 150
            self.range+=200
            self.cooldown -= 30
            res = self.next_up_price
            self.next_up_price = 350
        elif self.niveau ==4:
            self.sprite = cristal_img4
            self.prix += 70
            self.range+=100
            self.cooldown -= 5
            self.next_up_price = 200
            res = self.next_up_price
            self.next_up_price = m.inf
            
        return res

    def sell(self):
        return self.prix

    def attack(self, ennemies_tab, timer):
        res = None
        if timer % self.cooldown == 0:
            found = False
            i = 0
            while not found and i < len(ennemies_tab):
                e = ennemies_tab[i]
                difx = abs(self.pos[0] - e.position[0])
                dify = abs(self.pos[1] - e.position[1])
                dist = difx + dify
                if self.range >= dist:
                    bullet = self.bullet[self.niveau-1](self.pos, e)
                    res =  bullet
                    found = True
                i +=1
        return res
