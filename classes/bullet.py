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

heal_bullet_img1 = pygame.image.load("textures/sprites/towers/bullets/healer_zone.png")

rock_fall_bullet_img = pygame.image.load("textures/sprites/towers/bullets/rock_fall.png")

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
        obj = self.objectif.get_real_pos()

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

        dif_x = m.sqrt((pos[0] - obj[0])**2) 
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
        obj = self.objectif.get_real_pos()

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
        obj = self.objectif.get_real_pos()

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
                pos = e.get_real_pos()
                dif_x = m.sqrt((pos[0] - self.realpos[0])**2)
                dif_y = m.sqrt((pos[1] - self.realpos[1])**2)
                dist = dif_x + dif_y
                if self.range >= dist:
                    res.append(e)
        return res

    def toucher(self, ennemies_proche):
        if ennemies_proche != None:
            for e in ennemies_proche:
                e.degat_inflige(self.degat, self.type)

class radio2:
    def __init__(self,pos, realpos):
        self.sprite = radio_bullet_img1
        self.position = copy(pos)
        self.realpos = copy(realpos)
        self.type = 'magique'
        self.timer = 100
        self.cooldown = 20
        self.degat = 20
        self.range = 200

    def update(self, CanvasParent, ennemis, timer):
        res = False

        if self.timer == 0:
            res = True
        
        self.timer -= 1

        ennemis_proche = self.est_toucher(ennemis)
        self.toucher(ennemis_proche, timer)

        if not res:
            CanvasParent.blit(self.sprite, (self.position[0]-self.range, self.position[1]-self.range))
        
        return res
             
    def est_toucher(self, ennemies_tab):
        res = []

        for e in ennemies_tab:
            pos = e.get_real_pos()
            dif_x = m.sqrt((pos[0] - self.realpos[0])**2)
            dif_y = m.sqrt((pos[1] - self.realpos[1])**2)
            dist = dif_x + dif_y
            if self.range >= dist:
                res.append(e)
        
        for ennemie in res:
            ennemie.insertNewEtat( ('vitesse' , 0.5, 2, 2, hex(id(self)) ) )
        
        return res

    def toucher(self, ennemies_proche, timer):
        if ennemies_proche != None and timer % self.cooldown == 0:
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
        obj = self.objectif.get_real_pos()

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
        obj = self.objectif.get_real_pos()

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
        obj = self.objectif.get_real_pos()

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
        self.taille = 128
        self.position = copy(positionDepart)
        self.objectif = objectif.get_real_pos()
        self.type = 'physique'
        self.vitesse = 10
        self.degat = 15
        self.range = 50
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
            CanvasParent.blit(self.sprite, (self.position[0]-self.taille/2, self.position[1]-self.taille/2))
        if self.explose:
            pygame.draw.circle(CanvasParent, (255, 0, 0), self.position, self.range, 2)
        
        return self.explose_timer>20


    def est_toucher(self, distance):
        if distance < 20:
            return True
        return False


    def toucher(self, ennemies_tab):
        for e in ennemies_tab:
            pos = e.get_real_pos()
            dif_x = m.sqrt((pos[0] - self.position[0])**2)
            dif_y = m.sqrt((pos[1] - self.position[1])**2)
            dist = dif_x + dif_y
            if self.range >= dist:
                e.degat_inflige(self.degat, self.type)
                
            # application de debuff
            
            
                e.insertNewEtat( ('vie' , 10, 30*10+29, 30*2, hex(id(self)) ) )
                ## ! à faire l'explication
                # print("Hello")



    def calcule_Distance(self):

        pos = self.position
        obj = self.objectif

        dif_x = m.sqrt((pos[0] - obj[0])**2) #Il faut importer math as m au debut
        dif_y = m.sqrt((pos[1] - obj[1])**2)

        dist = dif_x + dif_y

        return dist
class volcan2:

    def __init__(self,positionDepart, objectif):
        self.sprite = volcan_bullet_img3
        self.position = copy(positionDepart)
        self.objectif = objectif.get_real_pos()
        self.type = 'physique'
        self.vitesse = 20
        self.degat = 25
        self.range = 100
        self.explose = False
        self.explose_timer = 0
        self.distance = self.calcule_Distance()
        self.taille = 128

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
            CanvasParent.blit(self.sprite, (self.position[0]-self.taille/2, self.position[1]-self.taille/2))
        if self.explose:
            pygame.draw.circle(CanvasParent, (255, 0, 0), self.position, self.range, 2)
        
        return self.explose_timer>20


    def est_toucher(self, distance):
        if distance < 20:
            return True
        return False


    def toucher(self, ennemies_tab):
        for e in ennemies_tab:
            pos = e.get_real_pos()
            dif_x = m.sqrt((pos[0] - self.position[0])**2)
            dif_y = m.sqrt((pos[1] - self.position[1])**2)
            dist = dif_x + dif_y
            if self.range >= dist:
                e.degat_inflige(self.degat, self.type)
                e.insertNewEtat( ('vie' , 10, 30*10+29, 30*2, hex(id(self)) ) )



    def calcule_Distance(self):

        pos = self.position
        obj = self.objectif

        dif_x = m.sqrt((pos[0] - obj[0])**2) #Il faut importer math as m au debut
        dif_y = m.sqrt((pos[1] - obj[1])**2)

        dist = dif_x + dif_y

        return dist
class volcan3:

    def __init__(self,positionDepart, objectif):
        self.sprite = volcan_bullet_img3
        self.position = copy(positionDepart)
        self.objectif = objectif.get_real_pos()
        self.type = 'physique'
        self.vitesse = 30
        self.degat = 40
        self.range = 125
        self.explose = False
        self.explose_timer = 0
        self.distance = self.calcule_Distance()
        self.taille = 128

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
            CanvasParent.blit(self.sprite, (self.position[0]-self.taille/2, self.position[1]-self.taille/2))
        if self.explose:
            pygame.draw.circle(CanvasParent, (255, 0, 0), self.position, self.range, 2)
        
        return self.explose_timer>20


    def est_toucher(self, distance):
        if distance < 20:
            return True
        return False


    def toucher(self, ennemies_tab):
        for e in ennemies_tab:
            pos = e.get_real_pos()
            dif_x = m.sqrt((pos[0] - self.position[0])**2)
            dif_y = m.sqrt((pos[1] - self.position[1])**2)
            dist = dif_x + dif_y
            if self.range >= dist:
                e.degat_inflige(self.degat, self.type)
                e.insertNewEtat( ('vie' , 5, 30*10+29, 30*2, hex(id(self)) ) ) # 10



    def calcule_Distance(self):

        pos = self.position
        obj = self.objectif

        dif_x = m.sqrt((pos[0] - obj[0])**2) #Il faut importer math as m au debut
        dif_y = m.sqrt((pos[1] - obj[1])**2)

        dist = dif_x + dif_y

        return dist
    
class heal:
    def __init__(self,pos, realpos):
        self.sprite = heal_bullet_img1
        self.position = copy(pos)
        self.realpos = copy(realpos)
        self.type = 'magique'
        self.timer = 90 # durée de l'effet ici 2 secondes
        self.cooldown = 20
        self.degat = -10 # ajout en santé => vie + self.degat
        self.range = 200
        
        self.parent = None

    def setParent(self,parent):
        self.parent = parent
        
    def update(self, CanvasParent, ennemis, timer):
        
        self.position = self.parent.position
        
        res = False

        if self.timer == 0:
            res = True
        
        self.timer -= 1

        ennemis_proche = self.est_toucher(ennemis)
        self.toucher(ennemis_proche, timer)

        if not res:
            CanvasParent.blit(self.sprite, (self.position[0]-self.range, self.position[1]-self.range))
        
        return res
                
    def est_toucher(self, ennemies_tab):
        res = []

        for e in ennemies_tab: # si dans cercle d'interaction
            pos = e.get_real_pos()
            dif_x = m.sqrt((pos[0] - self.realpos[0])**2)
            dif_y = m.sqrt((pos[1] - self.realpos[1])**2)
            dist = dif_x + dif_y
            if self.range >= dist:
                res.append(e) # ajout dans liste ennemi de self
                
        return res

    def toucher(self, ennemies_proche, timer):
#         if timer % self.cooldown == 0:
        if ennemies_proche != None and timer % self.cooldown == 0:
            for e in ennemies_proche:
                # e.insertNewEtat( ('vitesse' , 0.5 ) )
                e.degat_inflige(self.degat, self.type)

class rock_fall:
    def __init__(self,pos, realpos):
        self.sprite = rock_fall_bullet_img
        self.position = copy(pos)
        self.realpos = copy(realpos)
        self.type = 'physique'
        self.timer = 50
        self.degat = 250
        self.range = 50

    def update(self, CanvasParent, ennemis, timer):
        res = False

        if self.timer == 1:
            res = True
        else:
        
            self.timer -= 1
            ennemis_proche = self.est_toucher(ennemis, timer)
            self.toucher(ennemis_proche)

            CanvasParent.blit(self.sprite, (self.position[0]-100, self.position[1]-100))
        
        return res


    def est_toucher(self, ennemies_tab, timer):
        res = []

        if self.timer == 49:
            for e in ennemies_tab:
                pos = e.get_real_pos()
                dif_x = m.sqrt((pos[0] - self.realpos[0])**2)
                dif_y = m.sqrt((pos[1] - self.realpos[1])**2)
                dist = dif_x + dif_y
                if self.range >= dist:
                    res.append(e)
        return res

    def toucher(self, ennemies_proche):
        if ennemies_proche != None:
            for e in ennemies_proche:
                e.degat_inflige(self.degat, self.type)

