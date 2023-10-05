class Vague:
    def __init__(self, timer_tab, enn_tab):
        self.ennemis = enn_tab
        self.timers = timer_tab
        self.suivant = 0
        self.timecode = 0

    def nextFrame(self):
        res = 0
        self.timecode+=1

        if self.suivant < len(self.timers):
            if self.timecode == self.timers[self.suivant]:
                res = self.ennemis[self.suivant]
                self.suivant += 1
        else: res = -1

        return res


V = Vague([1, 5, 10], [3, 2, 10])

enn = V.nextFrame()

while enn != -1:
    print(V.timecode, enn)
    enn = V.nextFrame()

print(enn)
    

        
