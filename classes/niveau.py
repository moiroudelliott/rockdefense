import classes.vague as vague
import random as r
import classes.emplacement as emplacement
import classes.Jennemies as ennemies
import classes.button as button
import classes.tours as tours
import pygame
from classes.importation.import_textures import *
import math as m

button_texture = pygame.image.load("textures/sprites/button/next.png")
button_push_texture = pygame.image.load("textures/sprites/button/next_push.png")

class Niveau:

    def __init__(self):

        self.money_init = 250
        self.money = self.money_init

        self.vie_init = 500
        self.vie = self.vie_init

        self.next_button_state = False

        self.actual_wave = 0
        self.ennemies = []
        self.bullets = []

        self.pos_life = (1090,660)

        self.f_counter = 0

        def f():
            self.next_button_state = True

        self.next_button = button.Button((10, 450), (84, 51), button_texture, button_push_texture, f)

        self.rock_clicked = False
        self.rock_cooldown_default = 300
        self.rock_cooldown = 0
        self.rock_fall_default_pos = (10, 668)
        self.rock_fall_small_img = rock_fall_img_small
        self.rock_fall_small_img_op = rock_fall_img_small_op
        self.rock_fall_img = rock_fall_img
        

class Niveau1(Niveau):

    def __init__(self):

        Niveau.__init__(self)

        self.pts = [(90, 200), (0, 90), (310, 430), (520, 660), (570, 705), (0, 140), (1000, 1080)]

        # self.vagues = [
        # vague.Vague([1,2, 3,50], [1,1,1,6]),
        # vague.Vague([1,2, 3, 4, 5, 35, 36, 37, 38, 39, 40], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),
        # vague.Vague([1,2,3, 33, 34], [1,1,1, 2, 2]),
        # vague.Vague([1, 61, 62, 122, 123, 124], [3, 1, 1, 2, 2, 2]),
        # vague.Vague([1, 2, 3, 4, 5, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104], [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]),
        # vague.Vague([1, 2, 3, 33, 63, 64, 65, 155, 156, 157, 158, 159], [3, 3, 3, 4, 3, 3, 3, 2, 2, 2, 2, 2]),
        # vague.Vague([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 120, 121, 180, 181, 182], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4, 3, 3, 3]),
        # vague.Vague([1, 2, 3, 4, 5, 6, 7, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36], [3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 5, 5, 4, 4, 2, 2, 2, 2, 2, 2, 2, 2,2, 2]) ,
        # vague.Vague([1,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 60, 70, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138], [3,3,3, 3,3,3, 3,3,3, 3,3,3, 4, 4, 4, 1, 1, 1, 1, 1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4, 4, 5, 5, 5, 5, 4, 4, 4])
        # ]

        self.vagues = [

vague.Vague([1, 15, 30, ], [1, 1, 1, ]),

vague.Vague([1, 5, 30, 45, 90, 91, 92, ], [1, 1, 1, 1, 2, 2, 2, ]),

vague.Vague([1, 5, 9], [3, 3, 3]),

vague.Vague([1, 5, 9], [1, 5, 1]),

vague.Vague([1], [4]),

#vague.Vague([10, 15, 30, 35, ], [1, 2, 1, 2, ]),

#vague.Vague([1, 2, 3 ,7, 30, 40, 120, 125, 126, 127, ], [2, 2, 2, 2, 1, 1, 2, 2, 2, 2, ]),

#vague.Vague([1, 5, 7, 8, 15, 17, 20, 25, 60, 65, 72, 75, 90, 95, 100, 120, 121, 122, 135, ], [1, 1, 1, 2, 1, 2, 2, 1, 1, 1, 2, 2, 1, 1, 1, 2, 1, 1, 2, ]),



vague.Vague([1, 2, 5, 7, 9, 10, ], [1, 3, 2, 3, 2, 1, ]),

#vague.Vague([1, 2, 5, 7, 9, 10, ], [1, 3, 1, 3, 3, 3, ]),

#vague.Vague([2, 3, 7, 9, 30, 45, 120, 125, 130, 360, 361, 365, 370, 372, 375, 379, 600, 601, 612, 615, 620, ], [3, 3, 2, 1, 1, 3, 5, 3, 1, 2, 2, 2, 1, 1, 1, 1, 1, 5, 1, 3, 3, ]),

#vague.Vague([2, 3, 7, 9, 30, 45, 120, 125, 130, 360, 361, 365, 370, 372, 375, 379, 600, 601, 612, 615, 620, ], [2, 2, 2, 3, 5, 3, 5, 3, 1, 2, 2, 2, 1, 1, 1, 1, 1, 5, 5, 4, 3, ]),

vague.Vague([2, 3, 7, 9, 30, 45, 120, 125, 130, 360, 361, 365, 370, 372, 375, 379, 600, 601, 612, 615, 620, ], [2, 2, 2, 2, 1, 3, 5, 3, 1, 4, 4, 2, 1, 1, 3, 3, 1, 5, 4, 3, 3, ]),

vague.Vague([2, 3, 7, 9, 30, 45, 120, 125, 130, 360, 361, 365, 370, 372, 375, 379, 600, 601, 612, 615, 620, 900, ], [3, 3, 2, 1, 1, 3, 5, 3, 1, 2, 2, 2, 1, 1, 1, 1, 1, 5, 1, 3, 3, 6, ])

#,vague.Vague([1, 2, 3, 4, 5, ], [6, 6, 6, 6, 6,  ])

        ]

        #self.vagues=[vague.Vague([1], [1])]


        ## self.recompense = [100, 100, 200, 300, 400, 400, 400, 300, 500, 100, 0]
        self.recompense = [500, 500, 500, 500, 500, 500, 500]
        # self.recompense = [150, 150, 150, 200, 300, 300, 400, 500, 500,  0]

        self.emplacements = [emplacement.emplacement([220, 142]), emplacement.emplacement([220, 346]), emplacement.emplacement([220, 540]), emplacement.emplacement([460, 62]), emplacement.emplacement([460, 262]), emplacement.emplacement([460, 420]), emplacement.emplacement([730, 300]), emplacement.emplacement([730, 500]), emplacement.emplacement([826, 20]), emplacement.emplacement([976, 156])]



        self.next_button_state = False

        self.game_music = 'effects/tests/bg_music1.mp3'

        self.obj = tours.obj([1050,450])

        self.bg = bg_img

        self.start = [[0, 0], [500, 670]]

        def f():
            self.next_button_state = True

        self.next_button = button.Button((10, 450), (84, 51), button_texture, button_push_texture, f)

    def update(self, timer, vitesse, position, deg, actualPt, pts, cooldown, choix):
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


    def plus_proche(self, range, pos):
        proche = None
        proche_dist = 10000
        for e in self.ennemies:
            e_pos = e.get_real_pos()
            dif_x = (pos[0] - e_pos[0])**2
            dif_y = (pos[1] - e_pos[1])**2
            dist = m.sqrt(dif_x + dif_y)
            if range >= dist:
                if proche_dist > dist:
                    proche = e
                    proche_dist = dist

        return proche

    def plus_loins(self, range, pos):

        loins = None
        if self.ennemies != []:
            loins = self.ennemies[0]

            for e in self.ennemies:
                e_pos = e.get_real_pos()
                e_pt = e.actualPt
                loins_pos = loins.get_real_pos()
                loins_pt = loins.actualPt
                dif_x = (pos[0] - e_pos[0])**2
                dif_y = (pos[1] - e_pos[1])**2
                dist = m.sqrt(dif_x + dif_y)
                if range >= dist:
                    if e_pt>loins_pt:
                        loins = e
                    elif e_pt == loins_pt:
                        if loins_pt in [1, 3, 5, 7, 8]:
                            if e_pos[0]>loins_pos[0]:
                                loins = e

                        elif loins_pt in [2, 6]:
                            if e_pos[1]<loins_pos[1]:
                                loins = e

                        elif loins_pt == 4:
                            if e_pos[1]>loins_pos[1]:
                                loins = e

            dif_x = (pos[0] - loins.get_real_pos()[0])**2
            dif_y = (pos[1] - loins.get_real_pos()[1])**2
            dist = m.sqrt(dif_x + dif_y)
            if dist > range:
                loins = None

        return loins

class Niveau2(Niveau):

    def __init__(self):

        Niveau.__init__(self)

        self.pts = [(605, 678), (0, 63), (291, 390), (342, 405), (30, 143), (748, 827), (34, 128), (1090, 1172), (531, 616), (703, 916)]

        # self.vagues = [vague.Vague([1,2, 3], [1,1,1]), vague.Vague([1,2, 3, 4, 5, 35, 36, 37, 38, 39, 40], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), vague.Vague([1,2,3, 33, 34], [1,1,1, 2, 2]), vague.Vague([1, 61, 62, 122, 123, 124], [3, 1, 1, 2, 2, 2]), vague.Vague([1, 2, 3, 4, 5, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104], [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]), vague.Vague([1, 2, 3, 33, 63, 64, 65, 155, 156, 157, 158, 159], [3, 3, 3, 4, 3, 3, 3, 2, 2, 2, 2, 2]), vague.Vague([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 120, 121, 180, 181, 182], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4, 3, 3, 3]),vague.Vague([1, 2, 3, 4, 5, 6, 7, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36], [3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 5, 5, 4, 4, 2, 2, 2, 2, 2, 2, 2, 2,2, 2]) , vague.Vague([1,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 60, 70, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138], [3,3,3, 3,3,3, 3,3,3, 3,3,3, 4, 4, 4, 1, 1, 1, 1, 1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4, 4, 5, 5, 5, 5, 4, 4, 4])]
        #self.vagues = [vague.Vague([1], [2])]
        self.vagues = [

vague.Vague([1, 15, 30, 31, ], [1, 1, 2, 1, ]),

vague.Vague([1, 5, 30, 45, 90, 91, 92, 105, 132, ], [2, 2, 2, 2, 2, 2, 2, 2, 2, ]),

vague.Vague([10, 15, 30, 35, ], [3, 3, 5, 3, ]),

vague.Vague([1, 2, 3, 7, 30, 40, 120, 125, 126, 127, 131, 132, 133, 137, 160, 170, 250, 255, 256, 257], [2, 2, 2, 2, 1, 1, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 3, 2, 2, 2]),

vague.Vague([1, 5, 7, 8, 15, 17, 20, 25, 60, 65, 72, 75, 90, 95, 100, 120, 121, 122, 135, 201, 205, 207, 208, 215, 217, 220, 225, 260, 265, 272, 275, 290, 295, 300, 320, 321, 322, 335], [1, 1, 1, 2, 1, 2, 2, 1, 1, 1, 2, 2, 1, 3, 3, 3, 5, 1, 2, 1, 3, 3, 2, 1, 2, 2, 4, 1, 1, 2, 2, 1, 1, 4, 2, 4, 1, 2]),





vague.Vague([1, 2, 5, 7, 9, 10, 61, 62, 65, 67, 69, 70], [1, 2, 1, 2, 2, 3, 2, 3, 1, 2, 3, 3]),

vague.Vague([2, 3, 7, 9, 30, 45, 120, 125, 130, 360, 361, 365, 370, 372, 375, 379, 600, 601, 612, 615, 620, 702, 703, 707, 709, 730, 745, 820, 825, 830, 1060, 1061, 1065, 1070, 1072, 1075, 1079, 1300, 1301, 1312, 1315, 1320], [3, 3, 2, 1, 1, 3, 5, 3, 1, 2, 2, 2, 1, 1, 1, 1, 1, 5, 1, 3, 4, 3, 3, 2, 1, 1, 3, 5, 3, 1, 2, 2, 2, 1, 1, 1, 1, 1, 5, 4, 3, 3]),

vague.Vague([2, 3, 7, 9, 30, 45, 120, 125, 130, 360, 361, 365, 370, 372, ], [6, 2, 2, 3, 5, 3, 5, 3, 1, 2, 2, 2, 1, 1, 3, ]),

vague.Vague([2, 3, 7, 9, 30, 45, 120, 125, 130, 360, 361, 365, 370, 372, 375, 379, 600, 601, 612, 615, 620, 900, ], [3, 3, 2, 1, 1, 3, 5, 3, 1, 2, 2, 2, 1, 1, 1, 1, 1, 5, 1, 3, 3, 7, ])

,vague.Vague([1, 2, 3, 4, 5, ], [7, 7, 7, 7, 7,  ])

        ]

        self.emplacements = [emplacement.emplacement([20, 144]), emplacement.emplacement([77, 420]), emplacement.emplacement([327, 427]), emplacement.emplacement([428, 168]), emplacement.emplacement([625, 168]), emplacement.emplacement([855, 154]), emplacement.emplacement([991, 154]), emplacement.emplacement([857, 402]), emplacement.emplacement([990, 402])]

        self.recompense = [300, 300, 300, 400, 600, 600, 800, 1000, 1400, 1000, 0]

        self.next_button_state = False

        self.game_music = 'effects/tests/bg_music1.mp3'

        self.obj = tours.obj([520,440])
        #self.obj = tours.obj([7888,440])

        self.pos_life = (560, 655)

        self.bg = bg_img2

        self.start = [[205, 250], [0, 0]]

        def f():
            self.next_button_state = True

        self.next_button = button.Button((291, 5), (84, 51), button_texture, button_push_texture, f)

    def update(self, timer, vitesse, position, deg, actualPt, pts, cooldown, choix):
        vit = vitesse
        pos = position

        degats = 0

        if actualPt==1:
            pos[1] += vit
            if pos[1]>pts[0]:
                actualPt+=1

        elif actualPt==2:
            pos[0] -= vit
            if pos[0] < pts[1]:
                actualPt+=1

        elif actualPt==3:
            pos[1] -= vit
            if pos[1]<pts[2]:
                actualPt+=1

        elif actualPt==4:
            pos[0] += vit
            if pos[0] > pts[3] + 430:
                actualPt+=1
            if pos[0] > pts[3] and choix == 1:
                actualPt+=1

        elif actualPt==5:
            pos[1] -= vit
            if pos[1] < pts[4]:
                actualPt+=1

        elif actualPt==6:
            pos[0] += vit
            if pos[0] > pts[5]:
                actualPt+=1

        elif actualPt==7:
            pos[0] += vit
            actualPt+=1

        elif actualPt==8:
            pos[0] += vit
            if pos[0] > pts[7]:
                actualPt+=1

        elif actualPt==9:
            pos[1] += vit
            if pos[1] > pts[8]:
                actualPt+=1

        elif actualPt==10:
            pos[0] -=vit
            if pos[0] < pts[9]:
                actualPt +=1

        else :
            if timer % cooldown == 0:
                degats = deg

        return (degats, pos, actualPt)


    def plus_proche(self, range, pos):
        proche = None
        proche_dist = 10000
        for e in self.ennemies:
            e_pos = e.get_real_pos()
            dif_x = (pos[0] - e_pos[0])**2
            dif_y = (pos[1] - e_pos[1])**2
            dist = m.sqrt(dif_x + dif_y)
            if range >= dist:
                if proche_dist > dist:
                    proche = e
                    proche_dist = dist

        return proche

    def plus_loins(self, range, pos):

        loins = None
        if self.ennemies != []:
            loins = self.ennemies[0]

            for e in self.ennemies:
                e_pos = e.get_real_pos()
                e_pt = e.actualPt
                loins_pos = loins.get_real_pos()
                loins_pt = loins.actualPt
                dif_x = (pos[0] - e_pos[0])**2
                dif_y = (pos[1] - e_pos[1])**2
                dist = m.sqrt(dif_x + dif_y)
                if range >= dist:
                    if e_pt>loins_pt:
                        loins = e
                    elif e_pt == loins_pt:
                        if loins_pt in [4, 6]:
                            if e_pos[0]>loins_pos[0]:
                                loins = e

                        elif loins_pt in [2, 8, 9]:
                            if e_pos[0]<loins_pos[0]:
                                loins = e

                        elif loins_pt in [3, 5]:
                            if e_pos[1]<loins_pos[1]:
                                loins = e

                        elif loins_pt in [1, 7]:
                            if e_pos[1]>loins_pos[1]:
                                loins = e

            dif_x = (pos[0] - loins.get_real_pos()[0])**2
            dif_y = (pos[1] - loins.get_real_pos()[1])**2
            dist = m.sqrt(dif_x + dif_y)
            if dist > range:
                loins = None

        return loins
