import classes.bullet as bullet
import classes.button as button
import classes.emplacement as emplacement
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

## Rammasse miette
miette = True

if miette:
    del PATH_DATA_ENNEMIES
    del parsed_json
    del file_contents
    del data_file
    del data
    del miette