class Button:
    def __init__(self, pos, taille, sprite, sprite_hover, action):
        self.sprite = sprite
        self.length = taille[0]
        self.width = taille[1]
        self.pos = pos
        self.hover = False
        self.hover_sprite =sprite_hover
        self.action = action


    def display(self, mouse, canvas):

        self.hover(mouse)

        if self.hover:
            canvas.blit(self.hover_sprite, self.pos)
        else:
            canvas.blit(self.sprite, self.pos)

    def hover(self, mouse):
        if mouse[0] < self.pos[0] < mouse[0]+self.length and mouse[1] < self.pos[1] < mouse[1]+self.width:
            self.hover = True
        else:
            self.hover = False

    def click(self):
        self.action()
