import pygame
import classes.tours as t

button_img = pygame.image.load("textures/sprites/emp/button.png")
button_pushed_img = pygame.image.load("textures/sprites/emp/button_pushed.png")
button_clicked_img = pygame.image.load("textures/sprites/emp/button_clicked.png")
button_clicked_pushed_img = pygame.image.load("textures/sprites/emp/button_clicked_pushed_1.png")
button_clicked_pushed_img2 = pygame.image.load("textures/sprites/emp/button_clicked_pushed_2.png")
button_clicked_pushed_img3 = pygame.image.load("textures/sprites/emp/button_clicked_pushed_3.png")
button_clicked_pushed_img4 = pygame.image.load("textures/sprites/emp/button_clicked_pushed_4.png")


class emplacement:

    def __init__(self, position): #Le contient en parametre ne sers à rien
        self.contient = None #Doit être toujours initialiser à None, un nouvel emplacement ne contiens jamais rien
        self.pos = position
        self.sprite = button_img
        self.spriteHover = button_pushed_img
        self.spriteClickedHover = button_clicked_pushed_img
        self.spriteClickedHover2 = button_clicked_pushed_img2
        self.spriteClickedHover3 = button_clicked_pushed_img3
        self.spriteClickedHover4 = button_clicked_pushed_img4
        self.spriteClicked = button_clicked_img
        self.hover = False
        self.pushed_hover = 0
        self.clicked = False

    def display(self, canvas, mouse, money, font):

        self.hover_check(mouse, money)

        if self.contient == None:
            if self.clicked:
                if self.pushed_hover == 1:
                    canvas.blit(self.spriteClickedHover, self.pos)
                elif self.pushed_hover == 2:
                    canvas.blit(self.spriteClickedHover2, self.pos)
                elif self.pushed_hover == 3:
                    canvas.blit(self.spriteClickedHover3, self.pos)
                elif self.pushed_hover == 4:
                    canvas.blit(self.spriteClickedHover4, self.pos)
                else: 
                    canvas.blit(self.spriteClicked, self.pos)
            elif self.hover:
                canvas.blit(self.spriteHover, self.pos)
           
            else:
                canvas.blit(self.sprite, self.pos)
        else:
            self.contient.display(canvas, money, self.hover, font)

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

            

    def click(self, money, mouse):

        m = 0

        if self.contient == None:
            if self.clicked and self.pushed_hover == 0:
                self.clicked = False

            if self.hover and not self.clicked:
                self.clicked = True

            elif self.pushed_hover == 1:
                self.clicked = False
                self.contient = t.Pierre(self.pos)
                m = 100
            
            elif self.pushed_hover == 2:
                self.clicked = False
                self.contient = t.Radio(self.pos)
                m = 150

            elif self.pushed_hover == 3:
                self.clicked = False
                self.contient = t.Cristal(self.pos)
                m = 150

        else:
            m = self.contient.click(self.hover, mouse)
            if m <0:
                self.contient = None
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