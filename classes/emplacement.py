class emplacement:

    def __init__(self, position): #Le contient en parametre ne sers à rien
        self.contient = None #Doit être toujours initialiser à None, un nouvel emplacement ne contiens jamais rien
        self.position = position
        self.sprite = pygame.image.load(*---*).convert() #Url ici
        self.spriteHover = pygame.image.load(*---*).convert() #Url ici
        self.hover = False

    def afficher(self, CanvasParent):
        sprite = self.sprite
        if self.hover:
            sprite = self.spriteHover

        CanvasParent.blit(sprite, self.position)

    def hover(self):
        if self.hover:
            self.hover = False
        else:
            self.hover = True

    def click(self, tour):
        # Enlever de l'or ?
        # pour enlever l'or je pense que le plus simple serais de mettre l'or en entrée et quand on modifiera dans la fonction ça modifiera aussi en dehors
        # Comment savoir quelle tour acheter ?
        #On vérifie la tour qu'on achète selon l'emplacement du clic, il faut donc mettre en entrée la position de mouse


        # mouse = pygame.mouse.get_pos()
        #
        # if mouseX == (x,y):
        #     self.contient = tourClassique