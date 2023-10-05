class classique:
    def __init__(self, positionDepart):
        """
            positionDepart un tuple (x,y)
        """

        self.position = positionDepart
        self.vie = 10
        self.sprite = pygame.image.load(*---*).convert() #Url ici
        self.degat = 10
        self.vitesse = 1
        self.resistance = {'physique': 1, 'magique': 1} #resistance naturelle
        self.etat = {'buff': {'vitesse':1,'degat':1,'magique':1,'physique':1,},'debuff': {'vitesse':1,'magique':1,'physique':1,'degat':1,}}
        self.valeur = 10

    def coefficientEtat(self, type):
        return 1 * (self.etat['buff'][type] * self.etat['debuff'][type])

    def update(self):
        """
            Mets à jour la position du sprite
        """#ainsi que sa vitesse + etat ? => Je ne pense pas mais pon reviendra dessus plus tard si besoin quand on implémentera les buff/debuff
        # coefficient_vitesse = self.coefficientEtat('vitesse')
        # vitesse = self.vitesse * coefficient_vitesse
        pass

    def degat_inflige(self, degat, type):

        valeur_degat = degat
        type_degat = type

        coefficient_resistance = self.resistance[type_degat] * (self.coefficientEtat(type_degat) + self.coefficientEtat(type_degat))
        valeur_degat = valeur_degat * coefficient_resistance

        self.vie = self.vie - valeur_degat

    def degat_attaque(self):

        coefficient_degat = self.coefficientEtat('degat')
        return self.degat * coefficient_degat

    def afficher(self, CanvasParent):
        CanvasParent.blit(slef.sprite, self.position)