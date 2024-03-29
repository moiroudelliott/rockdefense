import pygame
import random as r

## §§§ Bibliothèque supplémentaire voir coefficient etat
## from functools import reduce
## import operator

import classes.bullet as b
# import classes.niveau as niveau
import math as m

class EnnemieModel():
    """
        Sert à définir le model d'un ennemie -> base pour transformation spécifique
    """
    def __init__(self):
        """
            rien
        """

        self.nom = None
        self.position = None
        self.vie = None
        self.sprite = None
        self.degat = None
        self.vitesse = None
        self.choix = r.randint(0, 1)
        self.resistance = None
        self.etat = {
                        "vitesse": [],
                        "degat": [],
                        "magique": [],
                        "physique": [],
                        "vie": [],
                    }
        self.valeur = None
        self.pts = []
        # for pt in niveau.pts:
        #     self.pts.append(r.randint(pt[0], pt[1]))
        self.niveau = None
        self.actualPt = None

        self.cooldown = None

        self.MaxVie = None

    def importationJSON(self, Data):

        self.nom = Data['nom']
        self.vie = Data['vie']
        self.sprite = pygame.image.load(Data['cheminSprite'])
        self.degat = Data['degat']
        self.vitesse = Data['vitesse']
        self.resistance = Data['resistance']
        # self.etat = Data['etat']
        self.valeur = Data['valeur']
        self.actualPt = 1 # A voir si modification

        self.cooldown = Data['cooldown']

        self.choix = r.randint(0, 1)

        self.taille = Data['taille']

        self.MaxVie = Data['maxVie']

    def create(self, positionDepart, niveau):
        self.position = positionDepart
        for pt in niveau.pts:
            self.pts.append(r.randint(pt[0], pt[1]))
        self.niveau = niveau

    def copy(self):
        return self

    def get_real_pos(self):
        return [self.position[0] + int(self.taille[0]/2), self.position[1] + int(self.taille[1]/2)]

    def coefficientEtat(self, type):
        """
            Retourne un coeff du type selectionner
        """
        # return 1 * (1/self.etat['buff'][type] * (self.etat['debuff'][type]) ) # ancienne version

        # return reduce( operator.mul, self.etat[ type ], 1 ) # nouvelle version avec reduce
        mul = 1
        for elt in self.etat[type]:
            if elt[1]%elt[2] == 0: # gestion du cooldown de l'effet
                mul = mul * elt[0]
        return mul

    def updateEtat(self):
        # print( self.etat )
        for key in self.etat.keys():
            for elt in self.etat[ key ]:
                elt[1] -=1

            for i in range ( len(self.etat[ key ])-1, -1, -1 ):
                if elt[1] == 0:
                    self.etat[ key ].pop( i )

            max_dict = {}

            for sublist in self.etat[ key ]:
                # Si la valeur unique n'est pas encore dans le dictionnaire ou si le deuxième élément est plus grand
                if sublist[-1] not in max_dict or sublist[1] > max_dict[sublist[-1]][1]:
                    max_dict[sublist[-1]] = sublist

            # Obtenir toutes les listes maximales
            max_lists = list(max_dict.values())

            # print(max_lists)

            self.etat[ key ] = max_lists
        # print( self.etat )

    def degat_sur_duree(self):
        return self.coefficientEtat( 'vie' ) -1

    def degat_inflige(self, degat, type):

        valeur_degat = degat
        type_degat = type

        coefficient_resistance = (1/self.resistance[type_degat]) * self.coefficientEtat(type_degat)
        valeur_degat = valeur_degat * coefficient_resistance

        self.vie = self.vie - valeur_degat

    def degat_attaque(self):

        coefficient_degat = self.coefficientEtat('degat')
        return self.degat * coefficient_degat

    def resetEtat(self):
        # Permet de remettre à zero les états
        for buffDebuff in self.etat.keys():
            self.etat[ buffDebuff ] = []

    def insertNewEtat(self, buffDebuff):
        # buffBeduff de forme   => ( 'vitesse' , 0.7 )
        #                       => ( 'type' , coefficient )
        type = buffDebuff[ 0 ]
        coefficient = buffDebuff[ 1 ]
        time = buffDebuff[ 2 ]
        cooldownBuffBeduff = buffDebuff[ 3 ]
        id = buffDebuff[ 4 ]

        caracteristique = [ coefficient, time, cooldownBuffBeduff, id, ]

        self.etat[ type ].append( caracteristique )

class ComportementStandart(EnnemieModel):
    def __init__(self):
        EnnemieModel.__init__(self)

    def display(self, CanvasParent, font, timer, *args):

        if(self.MaxVie < self.vie):
            self.vie = self.MaxVie

        self.updateEtat()

        degatDuree = self.degat_sur_duree()
        self.vie -= degatDuree

        array = self.niveau.update( timer,
                                    self.vitesse * self.coefficientEtat( 'vitesse' ),
                                    self.position, self.degat_attaque() * self.coefficientEtat( 'degat' ),
                                     self.actualPt,
                                     self.pts,
                                     self.cooldown,
                                     self.choix) # calcul pos + degat + point d'emplacement actuel (!important)


        self.position = array[1]
        self.actualPt = array[2]

        CanvasParent.blit(self.sprite, self.position)
        vie = font.render(str(int(self.vie)), True, "red")
        CanvasParent.blit(vie, (self.position[0],self.position[1]-10))



        return array[0] # renvoie les degats

class ComportementInvocateur(EnnemieModel):
    def __init__(self):
        EnnemieModel.__init__(self)

    def display(self, CanvasParent, font, timer, *args):

        if(self.MaxVie < self.vie):
            self.vie = self.MaxVie

        self.updateEtat()

        array = self.niveau.update(timer, self.vitesse * self.coefficientEtat( 'vitesse' ), self.position, self.degat_attaque() * self.coefficientEtat( 'degat' ), self.actualPt, self.pts, self.cooldown, self.choix) # calcul pos + degat + point d'emplacement actuel (!important)

        self.position = array[1]
        self.actualPt = array[2]

        nombreSbire = 5 # définie le nombre de sbire à invoquer



        if timer % self.cooldown == 0:
            # print(args[1])
            data = args[0][ r.randint(0,4) ] # pour des 1-3
            actual_level = args[1]
            liste_enn = args[2]

            rayonPixel = 75

            angle = [i*(2*m.pi)/nombreSbire for i in range(nombreSbire)]

            for elt in angle:
                data = args[0][ r.randint(0,2) ] # pour des 1-3

                classe = ComportementStandart() # ! si ComportementInvocateur
                classe.importationJSON( data )

                x = self.position[0] + rayonPixel * m.cos( elt ) + r.randint(-10,10)
                y = self.position[1] + rayonPixel * m.sin( elt ) + r.randint(-10,10)

                listeCoordonneAleatoire = [x,y]

                classe.create( listeCoordonneAleatoire , actual_level )

                classe.actualPt = self.actualPt

                liste_enn.append(classe)

        CanvasParent.blit(self.sprite, self.position)
        vie = font.render(str(int(self.vie)), True, "red")
        CanvasParent.blit(vie, (self.position[0],self.position[1]-10))



        return array[0] # renvoie les degats

class ComportementMagicien(EnnemieModel):
    def __init__(self):
        EnnemieModel.__init__(self)

        self.bullet = [b.heal,]

    def display(self, CanvasParent, font, timer, *args):

        if(self.MaxVie < self.vie):
            self.vie = self.MaxVie

        self.updateEtat()

        array = self.niveau.update( timer,
                                    self.vitesse * self.coefficientEtat( 'vitesse' ),
                                    self.position, self.degat_attaque() * self.coefficientEtat( 'degat' ),
                                     self.actualPt,
                                     self.pts,
                                     self.cooldown,
                                     self.choix) # calcul pos + degat + point d'emplacement actuel (!important)


        self.position = array[1]
        self.actualPt = array[2]

        if timer % self.cooldown == 0:
            liste_bullet = args[3]
            # print( liste_bullet )
            bullet = self.bullet[0](self.position,self.position)
            bullet.setParent( self )
            liste_bullet.append( bullet )

        CanvasParent.blit(self.sprite, self.position)
        vie = font.render(str(int(self.vie)), True, "red")
        CanvasParent.blit(vie, (self.position[0],self.position[1]-10))



        return array[0] # renvoie les degats

class ComportementBossNeige(EnnemieModel):
    def __init__(self):
        EnnemieModel.__init__(self)

    def display(self, CanvasParent, font, timer, *args):

        if(self.MaxVie < self.vie):
            self.vie = self.MaxVie

        self.updateEtat()

        array = self.niveau.update(timer, self.vitesse * self.coefficientEtat( 'vitesse' ), self.position, self.degat_attaque() * self.coefficientEtat( 'degat' ), self.actualPt, self.pts, self.cooldown, self.choix) # calcul pos + degat + point d'emplacement actuel (!important)

        self.position = array[1]
        self.actualPt = array[2]

        nombreSbire = 8 # définie le nombre de sbire à invoquer



        if timer % self.cooldown == 0:
            # print(args[1])
            # data = args[0][ r.randint(0,6) ] # pour des 1-5
            actual_level = args[1]
            liste_enn = args[2]
            generateEnemie = args[4]

            rayonPixel = 50

            angle = [i*(2*m.pi)/nombreSbire for i in range(nombreSbire)]

            for elt in angle:
                data = args[0][ r.randint(0,4) ]

                # classe = ComportementStandart() # ! si ComportementInvocateur
                # classe.importationJSON( data )

                classe = generateEnemie(data,actual_level, [(0,0),(1,1)])

                x = self.position[0] + rayonPixel * m.cos( elt ) + r.randint(-10,10)
                y = self.position[1] + rayonPixel * m.sin( elt ) + r.randint(-10,10)

                listeCoordonneAleatoire = [x,y]

                classe.create( listeCoordonneAleatoire , actual_level )

                classe.actualPt = self.actualPt

                liste_enn.append(classe)

        CanvasParent.blit(self.sprite, self.position)
        vie = font.render(str(int(self.vie)), True, "red")
        CanvasParent.blit(vie, (self.position[0],self.position[1]-10))



        return array[0] # renvoie les degats

Dict_Comportement = {
    "standart" : ComportementStandart,
    "invocateur" : ComportementInvocateur,
    "magicien" : ComportementMagicien,
    "bossNeige" : ComportementBossNeige,
}

## Workspace
# t = EnnemieModel()
# t.etat = {"vitesse": [0.5]}
# t.resetEtat()
# t.insertNewEtat( ('vitesse',[0.7,2,2,'brulure']) )
# t.insertNewEtat( ('vitesse',[0.7,2,2,'ralentissement']) )
# t.insertNewEtat( ('vitesse',[0.7,7,2,'brulure']) )

# hex(id(t)) => str