import classes.vague as vague
import classes.emplacement as emplacement

class Niveau1:
    def __init__(self):
        self.pts = [(90, 200), (0, 90), (310, 430), (520, 660), (570, 705), (25, 162), (900, 1080)]
        self.money_init = 500
        self.vie_init = 500
        classique_timer = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230]
        classique_enn = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.vagues = [vague.Vague(classique_timer, classique_enn), vague.Vague(classique_timer, classique_enn), vague.Vague(classique_timer, classique_enn), vague.Vague(classique_timer, classique_enn), vague.Vague(classique_timer, classique_enn), vague.Vague(classique_timer, classique_enn), vague.Vague(classique_timer, classique_enn)]
        self.emplacements = [emplacement.emplacement([220, 142]), emplacement.emplacement([220, 346]), emplacement.emplacement([220, 540]), emplacement.emplacement([460, 62]), emplacement.emplacement([460, 262]), emplacement.emplacement([460, 420]), emplacement.emplacement([730, 300]), emplacement.emplacement([730, 500]), emplacement.emplacement([826, 20]), emplacement.emplacement([976, 156])]


    def update(self, timer, vitesse, position, deg, actualPt, pts, cooldown):
        vit = vitesse
        pos = position

        degats = 0

        if actualPt==1:
            pos[0] += vit
            if pos[0]>pts[0]:
                actualPt+=1

        elif actualPt==2:
            pos[1] -= vit
            if pos[1] < pts[1]:
                actualPt+=1

        elif actualPt==3:
            pos[0] += vit
            if pos[0]>pts[2]:
                actualPt+=1

        elif actualPt==4:
            pos[1] += vit
            if pos[1] > pts[3]:
                actualPt+=1

        elif actualPt==5:
            pos[0] += vit
            if pos[0] > pts[4]:
                actualPt+=1

        elif actualPt==6:
            pos[1] -= vit
            if pos[1] < pts[5]:
                actualPt+=1
        elif actualPt==7:
            pos[0] +=vit
            pos[1] +=vit
            if pos[0] > pts[6]:
                actualPt +=1

        else :
            if timer % cooldown == 0:
                degats = deg

        return (degats, pos, actualPt)