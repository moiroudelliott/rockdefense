import pygame

bg_img = pygame.image.load("textures/bg/map1.png")

menu_img = pygame.image.load("textures/bg/menu_1.png")
menu_img_clicked = pygame.image.load("textures/bg/menu_1_clicked.png")

obj_img = pygame.image.load("textures/sprites/towers/cristal.png")
obj_img = pygame.transform.scale(obj_img,(200, 210))



rock_img = pygame.image.load("textures/sprites/towers/rock_lvl1.png")
rock_bullet_img = pygame.image.load("textures/sprites/towers/bullets/rock_bullet1.png")