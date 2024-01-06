import classes.bullet as bullet
import classes.button as button
import classes.emplacement as emplacement
import classes.statTD as stats
# import classes.ennemies as ennemies
import classes.tours as tours
import classes.niveau as niveau
import classes.vague as vague
from classes.importation.import_textures import *
import pygame
import math as m

## Ajout ( Déplacmeent dans fonctions ? )

import random as r
import classes.Jennemies as ennemies
import json
import copy as c
import time as t

# actual_level = niveau.Niveau1() # A enlever

## Importation des données ennemies
PATH_DATA_ENNEMIES = "./Data/ennemies.json"

with open( PATH_DATA_ENNEMIES ) as data_file:
  file_contents = data_file.read()

parsed_json = json.loads(file_contents)

def generateEnemie (data, actual_level, cos, dictComportement = ennemies.Dict_Comportement): #actual_level -> Niveau

    # listeCoordonneAleatoire = [0, r.randint(500, 670)]
    # res = classe(listeCoordonneAleatoire, actual_level)

    # print(data)
    comportement = data['comportement']
    # classe = ennemies.EnnemieModel()
    classe = dictComportement.get(
        comportement,
        dictComportement['standart']
    )

    classe = classe()
    classe.importationJSON( data )

    listeCoordonneAleatoire = [r.randint(cos[0][0], cos[0][1]), r.randint(cos[1][0], cos[1][1])]

    classe.create( listeCoordonneAleatoire , actual_level )

    return classe

# Liste_ennemies = [ennemies.classique, ennemies.tank, ennemies.rapide]
#
# Liste_ennemies[0] = ennemies.EnnemieModel().importationJSON(parsed_json[0])

Liste_ennemies = []

for data in parsed_json:

    # comportement = data['comportement']

    # enn = ennemies.EnnemieModel()
    # enn.importationJSON( data )
    Liste_ennemies.append( data )

## Fonction pour écran statistique
def STATS_SCREEN_1(SCREEN,WIDTH,HEIGHT, STAT, FONT,LIST_ENN ,COLOR):
    decalageWidth = 40
    decalageHeight = 75

    Text = FONT.render("Argent Totale: " + str(STAT.get_argentTotale()), True, COLOR )
    SCREEN.blit(Text, (decalageWidth,decalageHeight))

    Text = FONT.render("Nombre totale d'ennemis éliminés: " + str(STAT.get_nombreTotalEnnemieTuer()), True, COLOR )
    SCREEN.blit(Text, (decalageWidth,decalageHeight*3))

    Text = FONT.render("Nombre de victoire: " + str(STAT.get_nombreVictoire()), True, COLOR )
    SCREEN.blit(Text, (decalageWidth,decalageHeight*5))

    Text = FONT.render("Nombre de défaite: " + str(STAT.get_nombreDefaite()), True, COLOR )
    SCREEN.blit(Text, (decalageWidth,decalageHeight*7))

    # deuxieme colonne

    Text = FONT.render("Vie perdu totale: " + str(STAT.get_viePerdu()), True, COLOR )
    SCREEN.blit(Text, (decalageWidth + WIDTH//2,decalageHeight*1))

    Text = FONT.render("Nombre de tour construite/améliorée: " + str(STAT.get_nombreTourConstruite()), True, COLOR )
    SCREEN.blit(Text, (decalageWidth + WIDTH//2,decalageHeight*3))

    if (STAT.get_tempslvl1() != -1):
        Text = FONT.render("Temps level 1: " + str(STAT.get_tempslvl1()), True, COLOR )
    else:
        Text = FONT.render("Temps level 1: " + "Pas de temps renseigné", True, COLOR )
    SCREEN.blit(Text, (decalageWidth + WIDTH//2,decalageHeight*5))

    if (STAT.get_tempslvl2() != -1):
        Text = FONT.render("Temps level 2: " + str(STAT.get_tempslvl2()), True, COLOR )
    else:
        Text = FONT.render("Temps level 2: " + "Pas de temps renseigné", True, COLOR )
    SCREEN.blit(Text, (decalageWidth + WIDTH//2,decalageHeight*7))

def STATS_SCREEN_2(SCREEN,WIDTH,HEIGHT, STAT, FONT,LIST_ENN , COLOR):

    decalageWidth = 40
    decalageHeight = 75

    dict_ennemie = STAT.get_detailNombreTotalEnnemieTuer()
    liste_ennemie = list(dict_ennemie.items())

    dictEnn = {item['nom']: item for item in LIST_ENN}

    longueur = len(liste_ennemie)
    moitie = m.ceil(longueur / 2)

    suite = 1

    # première moitié
    for i in range(moitie):
        Text = FONT.render(liste_ennemie[i][0]+ ': ' + str(liste_ennemie[i][1]), True, COLOR )
        SCREEN.blit(Text, (decalageWidth   ,decalageHeight*suite))

        PATH_IMG = dictEnn[liste_ennemie[i][0]]['cheminSprite']
        IMG = pygame.image.load(PATH_IMG)
        IMG_CENTER = (IMG.get_size()[0]//2,IMG.get_size()[1]//2)

        SCREEN.blit(IMG, (decalageWidth +Text.get_size()[0] +decalageWidth   ,decalageHeight*suite +Text.get_size()[1]//2 -IMG_CENTER[1] ) )

        suite +=2

    suite = 1

    # deuxième moitié
    for i in range(moitie, longueur):
        Text = FONT.render(liste_ennemie[i][0]+ ': ' + str(liste_ennemie[i][1]), True, COLOR )
        SCREEN.blit(Text, (decalageWidth  + WIDTH//2 ,decalageHeight*suite))

        PATH_IMG = dictEnn[liste_ennemie[i][0]]['cheminSprite']
        IMG = pygame.image.load(PATH_IMG)
        IMG_CENTER = (IMG.get_size()[0]//2,IMG.get_size()[1]//2)

        SCREEN.blit(IMG, (decalageWidth +Text.get_size()[0] +decalageWidth   + WIDTH//2 ,decalageHeight*suite +Text.get_size()[1]//2 -IMG_CENTER[1] ) )

        suite +=2

## Rammasse miette
miette = True

if miette:
    del PATH_DATA_ENNEMIES
    del parsed_json
    del file_contents
    del data_file
    del data
    del miette