import pygame
pygame.mixer.init()

bg_img = pygame.image.load("textures/bg/map1.png")
bg_img2 = pygame.image.load("textures/bg/map2.png")
pause_bg = pygame.image.load("textures/bg/pause.png")
game_over = pygame.image.load("textures/bg/game_over.png")
win_text = pygame.image.load("textures/bg/win.png")

map = pygame.image.load("textures/bg/map.png")
label1 = pygame.image.load("textures/bg/label_lvl1.png")
label2 = pygame.image.load("textures/bg/label_lvl2.png")
quit = pygame.image.load("textures/bg/quit.png")


menu_img = pygame.image.load("textures/bg/menu_1.png")
menu_img_clicked = pygame.image.load("textures/bg/menu_1_clicked.png")

obj_img = pygame.image.load("textures/sprites/towers/cristal.png")
obj_img = pygame.transform.scale(obj_img,(200, 210))

new_wave_sound = pygame.mixer.Sound("effects/game/new_wave.mp3")
new_wave_sound.set_volume(0.3)
explosion1_sound = pygame.mixer.Sound("effects/tests/explosion.wav")
explosion1_sound.set_volume(0.3)
hover_button_sound = pygame.mixer.Sound("effects/tests/hover_boutton.wav")
magie_touche_sound = pygame.mixer.Sound("effects/tests/magie.wav")
magie_touche_sound.set_volume(0.3)
pierre_touche_sound = pygame.mixer.Sound("effects/tests/pierre_touche.wav")
pierre_touche_sound.set_volume(0.2)
radio_sound = pygame.mixer.Sound("effects/tests/radio.wav")
radio_sound.set_volume(0.2)
start_sound = pygame.mixer.Sound("effects/tests/start.wav")
start_sound.set_volume(0.2)
tir_magie_sound = pygame.mixer.Sound("effects/tests/tir_magie.wav")
tir_magie_sound.set_volume(0.1)
tir_pierre_sound = pygame.mixer.Sound("effects/tests/tir_pierre.wav")
tir_pierre_sound.set_volume(0.3)
tir_volcan_sound = pygame.mixer.Sound("effects/tests/tir_volcan.wav")
tir_volcan_sound.set_volume(0.3)
victory_sound = pygame.mixer.Sound("effects/tests/victory.wav")

