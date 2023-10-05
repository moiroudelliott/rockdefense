
class Pierre:
    def __init__(self, pos):
        self.sprite = "sprite.png"
        self.length = 120
        self.width = 120
        self.bullet = ["bullet.Rock", "bullet.Rock", "bullet.Rock", "bullet.Rock"]
        self.type_degat = "physique"
        self.niveau = 1
        self.hover = False
        self.hover_sprite = "hover_sprite.png"
        self.hover_sprite = "hover_sprite_alt.png" #Sprite quand upgrade pas dispo
        self.pos = pos
        self.prix = 70
        self.lvl_max = 4


    def display(self, canvas, money):

        canvas.blit(self.sprite, self.pos)
        if self.hover:
            if money < self.prix:
                canvas.blit(self.hover_sprite_alt, self.pos)
            else:
                canvas.blit(self.hover_sprite, self.pos)

    def hover_check(self, mouse):
        if mouse[0] < self.pos[0] < mouse[0]+self.length and mouse[1] < self.pos[1] < mouse[1]+self.width:
            self.hover = True
        else:
            self.hover = False

    def click(self):
        ### A FAIRE QUAND ON AURA LES TEXTURES
        pass

    def upgrade(self):
        self.niveau+=1
        if self.niveau ==2:
            self.sprite = "sprite_lvl2.png"
            self.prix += 20
        elif self.niveau == 3:
            self.sprite = "sprite_lvl3.png"
            self.prix += 50
        elif self.niveau ==4:
            self.sprite = "sprite_lvl4.png"
            self.hover_sprite = "hover_sprite_alt.png"
            self.prix += 70

    def sell(self):
        return self.prix

    def attack(self, obj, timer):
        res = -1
        if timer%self.cooldown:
            bullet = self.bullet[self.niveau-1](self.pos, obj)
            res =  bullet

        return res


