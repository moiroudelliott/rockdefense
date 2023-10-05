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

    def reset(self):
        self.suivant = 0
        self.timecode = 0


        
