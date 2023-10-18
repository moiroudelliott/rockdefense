import math as m
import pygame
from copy import copy
rock_bullet_img = pygame.image.load("textures/sprites/towers/bullets/rock_bullet1.png")

class rock:
    def __init__(self,positionDepart, objectif):
        self.sprite = rock_bullet_img
        self.position = copy(positionDepart)
        self.objectif = objectif
        self.type = 'physique'
        self.vitesse = 20
        self.degat = 10

        self.distance = self.calcule_Distance()

    def update(self, CanvasParent):
        pos = self.position
        obj = self.objectif.position

        dif_x = m.sqrt((pos[0] - obj[0])**2)
        dif_y = m.sqrt((pos[1] - obj[1])**2)

        dist = dif_x + dif_y

        if dist ==0:
            pass
        else:


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

        res = self.est_toucher(dist)

        if res:
            self.toucher()
        else:
            CanvasParent.blit(self.sprite, self.position)
        
        return res


    def est_toucher(self, distance):
        if distance < 20:
            return True
        return False

    def toucher(self):
        self.objectif.degat_inflige(self.degat, self.type)


    def calcule_Distance(self):

        pos = self.position
        obj = self.objectif.position

        dif_x = m.sqrt((pos[0] - obj[0])**2) #Il faut importer math as m au debut
        dif_y = m.sqrt((pos[1] - obj[1])**2)

        dist = dif_x + dif_y

        return dist