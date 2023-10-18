import pygame
import random as r
ennemis_img = pygame.image.load("textures/sprites/ennemies/ennemy_tank.png") #simple
ennemis2_img = pygame.image.load("textures/sprites/ennemies/ennemy_fast.png")
ennemis3_img = pygame.transform.scale(ennemis_img,(90, 90)) # meme texture pour l'instant

class classique:
    def __init__(self, positionDepart):
        """
            positionDepart un tuple (x,y)
        """

        self.position = positionDepart
        self.vie = 100
        self.sprite = ennemis_img
        self.degat = 10
        self.vitesse = 2
        self.resistance = {'physique': 1, 'magique': 1} #resistance naturelle
        self.etat = {'buff': {'vitesse':1,'degat':1,'magique':1,'physique':1,},'debuff': {'vitesse':1,'magique':1,'physique':1,'degat':1,}}
        self.valeur = 10
        self.pts = [r.randint(90, 220), r.randint(0, 90), r.randint(310, 430), r.randint(520, 660), r.randint(570, 705), r.randint(25, 162), r.randint(900, 1080)]
        self.actualPt = 1

    def coefficientEtat(self, type):
        return 1 * (self.etat['buff'][type] * self.etat['debuff'][type])

    def update(self):
        vit = self.vitesse
        pos = self.position

        deg = 0

        if self.actualPt==1:
            pos[0] += vit
            if pos[0]>self.pts[0]:
                self.actualPt+=1

        elif self.actualPt==2:
            pos[1] -= vit
            if pos[1] < self.pts[1]:
                self.actualPt+=1

        elif self.actualPt==3:
            pos[0] += vit
            if pos[0]>self.pts[2]:
                self.actualPt+=1

        elif self.actualPt==4:
            pos[1] += vit
            if pos[1] > self.pts[3] and pos[0] < 570:
                self.actualPt+=1

        elif self.actualPt==5:
            pos[0] += vit
            if pos[0] > self.pts[4]:
                self.actualPt+=1

        elif self.actualPt==6:
            pos[1] -= vit
            if pos[1] < self.pts[5] and  pos[0] < 750:
                self.actualPt+=1
        elif self.actualPt==7:
            pos[0] +=vit
            pos[1] +=vit
            if pos[0] > self.pts[6]:
                self.actualPt +=1

        else : 
            deg = self.degat_attaque()

        self.position = pos
        return deg

    def degat_inflige(self, degat, type):

        valeur_degat = degat
        type_degat = type

        coefficient_resistance = self.resistance[type_degat] * (self.coefficientEtat(type_degat) + self.coefficientEtat(type_degat))
        valeur_degat = valeur_degat * coefficient_resistance

        self.vie = self.vie - valeur_degat

    def degat_attaque(self):

        coefficient_degat = self.coefficientEtat('degat')
        return self.degat * coefficient_degat


    def display(self, CanvasParent, font):

        self.update()

        CanvasParent.blit(self.sprite, self.position)
        vie = font.render(str(self.vie), True, "red")
        CanvasParent.blit(vie, (self.position[0],self.position[1]-10))


class rapide:
    def __init__(self, positionDepart):
        """
            positionDepart un tuple (x,y)
        """

        self.position = positionDepart
        self.vie = 50
        self.sprite = ennemis2_img
        self.degat = 15
        self.vitesse = 3
        self.resistance = {'physique': 0.75, 'magique': 0.75} #resistance naturelle
        self.etat = {'buff': {'vitesse':1,'degat':1,'magique':1,'physique':1,},'debuff': {'vitesse':1,'magique':1,'physique':1,'degat':1,}}
        self.valeur = 10

    def coefficientEtat(self, type):
        return 1 * (self.etat['buff'][type] * self.etat['debuff'][type])

    def update(self):
        vit = self.vitesse
        pos = self.position

        deg = 0

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
            deg = self.degat_attaque()

        self.position = pos
        return deg

    def degat_inflige(self, degat, type):

        valeur_degat = degat
        type_degat = type

        coefficient_resistance = self.resistance[type_degat] * (self.coefficientEtat(type_degat) + self.coefficientEtat(type_degat))
        valeur_degat = valeur_degat * coefficient_resistance

        self.vie = self.vie - valeur_degat

    def degat_attaque(self):

        coefficient_degat = self.coefficientEtat('degat')
        return self.degat * coefficient_degat


    def display(self, CanvasParent, font):

        self.update()

        CanvasParent.blit(self.sprite, self.position)
        vie = font.render(str(self.vie), True, "red")
        CanvasParent.blit(vie, (self.position[0],self.position[1]-10))

class tank:
    def __init__(self, positionDepart):
        """
            positionDepart un tuple (x,y)
        """

        self.position = positionDepart
        self.vie = 1000
        self.sprite = ennemis3_img
        self.degat = 10
        self.vitesse = 0.5
        self.resistance = {'physique': 2, 'magique': 1.5} #resistance naturelle
        self.etat = {'buff': {'vitesse':1,'degat':1,'magique':1,'physique':1,},'debuff': {'vitesse':1,'magique':1,'physique':1,'degat':1,}}
        self.valeur = 10

    def coefficientEtat(self, type):
        return 1 * (self.etat['buff'][type] * self.etat['debuff'][type])

    def update(self):
        vit = self.vitesse
        pos = self.position

        deg = 0

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
            deg = self.degat_attaque()

        self.position = pos
        return deg

    def degat_inflige(self, degat, type):

        valeur_degat = degat
        type_degat = type

        coefficient_resistance = self.resistance[type_degat] * (self.coefficientEtat(type_degat) + self.coefficientEtat(type_degat))
        valeur_degat = valeur_degat * coefficient_resistance

        self.vie = self.vie - valeur_degat

    def degat_attaque(self):

        coefficient_degat = self.coefficientEtat('degat')
        return self.degat * coefficient_degat


    def display(self, CanvasParent, font):

        self.update()

        CanvasParent.blit(self.sprite, self.position)
        vie = font.render(str(self.vie), True, "red")
        CanvasParent.blit(vie, (self.position[0],self.position[1]-10))
