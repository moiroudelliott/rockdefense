import pygame
import math
import classes.bullet as b
rock_img = pygame.image.load("textures/sprites/towers/rock_lvl1.png")

class Pierre:
    def __init__(self, pos):
        self.sprite = rock_img
        self.length = 120
        self.width = 120
        self.bullet = [b.rock, b.rock, b.rock, b.rock]
        self.type_degat = "physique"
        self.niveau = 1
        self.hover = False
        self.hover_sprite = "hover_sprite.png"
        self.hover_sprite_alt = "hover_sprite_alt.png" #Sprite quand upgrade pas dispo
        self.pos = pos
        self.prix = 70
        self.lvl_max = 4
        self.cooldown = 30
        self.range = 300


    def display(self, canvas, money):

        canvas.blit(self.sprite, self.pos)

        if self.hover:
            if money < self.prix:
                canvas.blit(self.hover_sprite_alt, self.pos)
            else:
                canvas.blit(self.hover_sprite, self.pos)

    def hover_check(self, mouse):
        if mouse[0] < self.pos[0] < mouse[0]+self.length and mouse[1] < self.pos[1] < mouse[1]+self.width:
            self.hover = True
        else:
            self.hover = False

    def click(self):
        ### A FAIRE QUAND ON AURA LES TEXTURES
        pass

    def upgrade(self):
        self.niveau+=1
        if self.niveau ==2:
            self.sprite = "sprite_lvl2.png"
            self.prix += 20
        elif self.niveau == 3:
            self.sprite = "sprite_lvl3.png"
            self.prix += 50
        elif self.niveau ==4:
            self.sprite = "sprite_lvl4.png"
            self.hover_sprite = "hover_sprite_alt.png"
            self.prix += 70

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
                if self.range > dist:
                    bullet = self.bullet[self.niveau-1](self.pos, e)
                    res =  bullet
                    found = True
                i +=1
        return res


