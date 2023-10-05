import math as m

class rock:
    def __init__(self,positionDepart, objectif):
        self.sprite = pygame.image.load("sprite.png").convert() #Url ici
        self.position = positionDepart
        self.objectif = objectif
        self.type = 'physique'
        self.vitesse = 20
        self.degat = 10

        self.distance = self.calcule_Distance()

    def update(self, CanvasParent):
        self.distance = self.calcule_Distance()
        if est_toucher():
            self.toucher()
        else:
            self.afficher(CanvasParent) ##comment insérer CanvasParent ?


    def est_toucher(self):
        if self.distance < 20:
            return True
        return False

    def toucher():
        self.objectif.degat_inflige(self.degat, self.type)

    def afficher(self, CanvasParent):
        CanvasParent.blit(slef.sprite, self.position)

    def calcule_Distance(self):

        pos = self.position
        obj = self.objectif.position

        dif_x = m.sqrt((pos[0] - obj[0])**2) #Il faut importer math as m au debut
        dif_y = m.sqrt((pos[1] - obj[1])**2)

        dist = dif_x + dif_y

        return dist