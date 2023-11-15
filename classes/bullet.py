import math as m
import pygame
from copy import copy
rock_bullet_img1 = pygame.image.load("textures/sprites/towers/bullets/rock_bullet1.png")
rock_bullet_img2 = pygame.image.load("textures/sprites/towers/bullets/rock_bullet2.png")
rock_bullet_img3 = pygame.image.load("textures/sprites/towers/bullets/rock_bullet3.png")

cristal_bullet_img1 = pygame.image.load("textures/sprites/towers/bullets/cristal_bullet1.png")
cristal_bullet_img2 = pygame.image.load("textures/sprites/towers/bullets/cristal_bullet2.png")
cristal_bullet_img3 = pygame.image.load("textures/sprites/towers/bullets/cristal_bullet3.png")

volcan_bullet_img1 = pygame.image.load("textures/sprites/towers/bullets/volcan_bullet1.png")
volcan_bullet_img2 = pygame.image.load("textures/sprites/towers/bullets/volcan_bullet2.png")
volcan_bullet_img3 = pygame.image.load("textures/sprites/towers/bullets/volcan_bullet3.png")

radio_bullet_img1 = pygame.image.load("textures/sprites/towers/bullets/radio_bullet1.png")

class rock1:
    def __init__(self,positionDepart, objectif):
        self.sprite = rock_bullet_img1
        self.position = copy(positionDepart)
        self.objectif = objectif
        self.type = 'physique'
        self.vitesse = 20
        self.degat = 15

        self.distance = self.calcule_Distance()

    def update(self, CanvasParent, ennemis, timer):
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
    
class rock2:
    def __init__(self,positionDepart, objectif):
        self.sprite = rock_bullet_img2
        self.position = copy(positionDepart)
        self.objectif = objectif
        self.type = 'physique'
        self.vitesse = 20
        self.degat = 20

        self.distance = self.calcule_Distance()

    def update(self, CanvasParent, ennemis, timer):
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
    
class rock3:
    def __init__(self,positionDepart, objectif):
        self.sprite = rock_bullet_img3
        self.position = copy(positionDepart)
        self.objectif = objectif
        self.type = 'physique'
        self.vitesse = 30
        self.degat = 40

        self.distance = self.calcule_Distance()

    def update(self, CanvasParent, ennemis, timer):
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
    
class radio1:
    def __init__(self,pos, realpos):
        print("init")
        self.sprite = radio_bullet_img1
        self.position = copy(pos)
        self.realpos = copy(realpos)
        self.type = 'magique'
        self.timer = 100
        self.cooldown = 30
        self.degat = 10
        self.range = 200

    def update(self, CanvasParent, ennemis, timer):
        res = False

        if self.timer == 0:
            res = True
        
        self.timer -= 1

        ennemis_proche = self.est_toucher(ennemis, timer)
        self.toucher(ennemis_proche)

        if not res:
            CanvasParent.blit(self.sprite, (self.position[0]-self.range, self.position[1]-self.range))
        
        return res


    def est_toucher(self, ennemies_tab, timer):
        res = []

        if timer % self.cooldown == 0:
            for e in ennemies_tab:
                difx = abs(self.position[0] - e.position[0])
                dify = abs(self.position[1] - e.position[1])
                dist = difx + dify
                if self.range >= dist:
                    res.append(e)
        return res

    def toucher(self, ennemies_proche):
        if ennemies_proche != None:
            for e in ennemies_proche:
                e.degat_inflige(self.degat, self.type)

class cristal1:
    def __init__(self,positionDepart, objectif):
        self.sprite = cristal_bullet_img1
        self.position = copy(positionDepart)
        self.objectif = objectif
        self.type = 'magique'
        self.vitesse = 20
        self.degat = 25

        self.distance = self.calcule_Distance()

    def update(self, CanvasParent, ennemis, timer):
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
    
class cristal2:
    def __init__(self,positionDepart, objectif):
        self.sprite = cristal_bullet_img2
        self.position = copy(positionDepart)
        self.objectif = objectif
        self.type = 'magique'
        self.vitesse = 40
        self.degat = 40

        self.distance = self.calcule_Distance()

    def update(self, CanvasParent, ennemis, timer):
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
    
class cristal3:
    def __init__(self,positionDepart, objectif):
        self.sprite = cristal_bullet_img3
        self.position = copy(positionDepart)
        self.objectif = objectif
        self.type = 'magique'
        self.vitesse = 40
        self.degat = 60

        self.distance = self.calcule_Distance()

    def update(self, CanvasParent, ennemis, timer):
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
    
class volcan1:
    def __init__(self,positionDepart, objectif):
        self.sprite = volcan_bullet_img3
        self.position = copy(positionDepart)
        self.objectif = objectif
        self.type = 'physique'
        self.vitesse = 20
        self.degat = 15
        self.range = 100
        self.explose = False
        self.explose_timer = 0
        self.distance = self.calcule_Distance()

    def update(self, CanvasParent, ennemis, timer):
        
        pos = self.position
        obj = self.objectif

        dif_x = m.sqrt((pos[0] - obj[0])**2)
        dif_y = m.sqrt((pos[1] - obj[1])**2)

        dist = dif_x + dif_y

        if not self.explose:

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

        self.explose = self.est_toucher(dist) or self.explose

        if self.explose:
            self.explose_timer+=1

        if self.explose_timer==1:
            self.toucher(ennemis)

        if not self.explose:
            CanvasParent.blit(self.sprite, self.position)
        if self.explose:
            pygame.draw.circle(CanvasParent, (255, 0, 0), self.position, self.range, 2)
        
        return self.explose_timer>20


    def est_toucher(self, distance):
        if distance < 20:
            return True
        return False


    def toucher(self, ennemies_tab):
        for e in ennemies_tab:
            difx = abs(self.position[0] - e.position[0])
            dify = abs(self.position[1] - e.position[1])
            dist = difx + dify
            if self.range >= dist:
                e.degat_inflige(self.degat, self.type)



    def calcule_Distance(self):

        pos = self.position
        obj = self.objectif

        dif_x = m.sqrt((pos[0] - obj[0])**2) #Il faut importer math as m au debut
        dif_y = m.sqrt((pos[1] - obj[1])**2)

        dist = dif_x + dif_y

        return dist
    
class volcan2:
    def __init__(self,positionDepart, objectif):
        self.sprite = rock_bullet_img2
        self.position = copy(positionDepart)
        self.objectif = objectif
        self.type = 'physique'
        self.vitesse = 20
        self.degat = 20


        self.distance = self.calcule_Distance()

    def update(self, CanvasParent, ennemis, timer):
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
        elif not self.explose:
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
    
class volcan3:
    def __init__(self,positionDepart, objectif):
        self.sprite = rock_bullet_img3
        self.position = copy(positionDepart)
        self.objectif = objectif
        self.type = 'physique'
        self.vitesse = 30
        self.degat = 40

        self.distance = self.calcule_Distance()

    def update(self, CanvasParent, ennemis, timer):
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
    