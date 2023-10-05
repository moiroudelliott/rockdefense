import pygame
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
        self.hover = False
        self.clicked = False

    def display(self, canvas, mouse):

        self.hover_check(mouse)

        if self.contient == None:
            if self.hover:
                canvas.blit(self.spriteHover, self.pos)
            else:
                canvas.blit(self.sprite, self.pos)
        else:
            self.contient.display()

    def hover_check(self, mouse):
        if self.pos[0] < mouse[0] < self.pos[0]+128 and self.pos[1] < mouse[1] < self.pos[1]+128:
            self.hover = True
        else:
            self.hover = False

    def click(self, tour):
        # Enlever de l'or ?
        # pour enlever l'or je pense que le plus simple serais de mettre l'or en entrée et quand on modifiera dans la fonction ça modifiera aussi en dehors
        # Comment savoir quelle tour acheter ?
        #On vérifie la tour qu'on achète selon l'emplacement du clic, il faut donc mettre en entrée la position de mouse


        # mouse = pygame.mouse.get_pos()
        #
        # if mouseX == (x,y):
        #     self.contient = tourClassique
        pass

    def reset(self):
        self.contient = None
        self.hover = False
        self.clicked = False