import pygame
import classes.tours as t

button_img = pygame.image.load("textures/sprites/emp/button.png")
button_pushed_img = pygame.image.load("textures/sprites/emp/button_pushed.png")
button_clicked_img = pygame.image.load("textures/sprites/emp/button_clicked.png")
button_clicked_pushed_img = pygame.image.load("textures/sprites/emp/button_clicked_pushed_1.png")

class emplacement:

    def __init__(self, position): #Le contient en parametre ne sers à rien
        self.contient = None #Doit être toujours initialiser à None, un nouvel emplacement ne contiens jamais rien
        self.pos = position
        self.sprite = button_img
        self.spriteHover = button_pushed_img
        self.spriteClickedHover = button_clicked_pushed_img
        self.spriteClicked = button_clicked_img
        self.hover = False
        self.pushed_hover = 0
        self.clicked = False

    def display(self, canvas, mouse, money):

        self.hover_check(mouse, money)

        if self.contient == None:
            if self.clicked:
                if self.pushed_hover == 1:
                    canvas.blit(self.spriteClickedHover, self.pos)
                else: 
                    canvas.blit(self.spriteClicked, self.pos)
            elif self.hover:
                canvas.blit(self.spriteHover, self.pos)
           
            else:
                canvas.blit(self.sprite, self.pos)
        else:
            self.contient.display(canvas, money, self.hover)

    def hover_check(self, mouse, money):

        x = self.pos[0]
        y = self.pos[1]

        if self.pos[0] < mouse[0] < self.pos[0]+128 and self.pos[1] < mouse[1] < self.pos[1]+128:
            self.hover = True
        else:
            self.hover = False

        if x <= mouse[0] <= x+128 and y <= mouse[1] <= y+32:
            if money >= 100:
                self.pushed_hover = 1
        elif x <= mouse[0] <= x+128 and y+33 <= mouse[1] <= y+64:
            if money >= 100:
                self.pushed_hover = 2
        elif x <= mouse[0] <= x+128 and y+65 <= mouse[1] <= y+96:
            if money >= 100:
                self.pushed_hover = 3
        elif x <= mouse[0] <= x+128 and y+97 <= mouse[1] <= y+128:
            if money >= 100:
                self.pushed_hover = 4
        else: 
            self.pushed_hover = 0

            

    def click(self):

        m = 0

        if self.clicked and self.pushed_hover == 0:
            self.clicked = False

        if self.hover and not self.clicked:
            self.clicked = True

        elif self.pushed_hover == 1:
            self.clicked = False
            self.contient = t.Pierre(self.pos)
            m = 100
        return m
    
    def reset(self):
        self.contient = None
        self.hover = False
        self.clicked = False

    def event(self, f, ennemies_tab):
        res  = None
        if self.contient != None:
            res = self.contient.attack(ennemies_tab, f)

        return res