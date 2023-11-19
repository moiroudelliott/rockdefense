import classes.vague as vague
import classes.emplacement as emplacement
import classes.Jennemies as ennemies

class Niveau1:
    def __init__(self):
        self.pts = [(90, 200), (0, 90), (310, 430), (520, 660), (570, 705), (0, 140), (1000, 1080)]
        self.money_init = 500
        self.vie_init = 400

        self.vagues = [vague.Vague([1,2, 3], [1,1,1]), vague.Vague([1,2, 3, 4, 5, 35, 36, 37, 38, 39, 40], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), vague.Vague([1,2,3, 33, 34], [1,1,1, 2, 2]), vague.Vague([1, 61, 62, 122, 123, 124], [3, 1, 1, 2, 2, 2]), vague.Vague([1, 2, 3, 4, 5, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104], [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]), vague.Vague([1, 2, 3, 33, 63, 64, 65, 155, 156, 157, 158, 159], [3, 3, 3, 4, 3, 3, 3, 2, 2, 2, 2, 2]), vague.Vague([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 120, 121, 180, 181, 182], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4, 3, 3, 3]), vague.Vague([1,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 60, 70, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134], [3,3,3, 3,3,3, 3,3,3, 3,3,3, 4, 4, 4, 1, 1, 1, 1, 1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4, 4, 4, 4, 4])]

        # self.vagues = [ vague.Vague([1,], [1,]) ]

        self.emplacements = [emplacement.emplacement([220, 142]), emplacement.emplacement([220, 346]), emplacement.emplacement([220, 540]), emplacement.emplacement([460, 62]), emplacement.emplacement([460, 262]), emplacement.emplacement([460, 420]), emplacement.emplacement([730, 300]), emplacement.emplacement([730, 500]), emplacement.emplacement([826, 20]), emplacement.emplacement([976, 156])]

        self.recompense = [150, 150, 150, 200, 300, 300, 400, 500, 0]

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

    def tri_ennemis(self, tab):
        res = []
        for _ in range(len(tab)):
            min = None
            min_position = (4000, 4000)
            min_actualPt = -1
            for e in tab:
                if e.actualPt > min_actualPt and e not in res:
                    min = e
                    min_pos = e.position
                    min_actualPt = e.actualPt
                elif e.actualPt == min_actualPt and e not in res:
                    if e.actualPt in [1, 3, 5, 7]:
                        if e.position[0]>min_position[0]:
                            min = e
                            min_pos = e.position
                            min_actualPt = e.actualPt
                    elif e.actualPt == 2:
                        if e.position[1]>min_position[1]:
                            min = e
                            min_pos = e.position
                            min_actualPt = e.actualPt
                    elif e.actualPt == 4:
                        if e.position[1]<min_position[1]:
                            min = e
                            min_pos = e.position
                            min_actualPt = e.actualPt
            res.append(min)
        return res
