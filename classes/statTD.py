# nb ennemi tuer
#     détail
#
# stat tour -> ennemie tué
#
# nb de tour créer
# or accumulé
# vir perdue
# nombre victoire / defaite

import json

class statistique():
    def __init__( self ):

        self.PATH = 'score.json'

        self.argentTotale = 0

        self.nombreTotalEnnemieTuer = 0
        self.detailNombreTotalEnnemieTuer = {}

        self.viePerdu = 0

        self.nombreVictoire = 0
        self.nombreDefaite = 0

        self.nombreTourConstruite = 0

        self.victoirelvl1 = False
        self.tempslvl1 = -1
        self.victoirelvl2 = False
        self.tempslvl2 = -1

    def exportToJSON( self ):

        data = {
            'argentTotale': self.argentTotale,
            'nombreTotalEnnemieTuer': self.nombreTotalEnnemieTuer,
            'detailNombreTotalEnnemieTuer': self.detailNombreTotalEnnemieTuer,
            'viePerdu': self.viePerdu,
            'nombreVictoire': self.nombreVictoire,
            'nombreDefaite': self.nombreDefaite,
            'nombreTourConstruite': self.nombreTourConstruite,
            'victoirelvl1': self.victoirelvl1,
            'timelvl1': self.tempslvl1,
            'victoirelvl2': self.victoirelvl2,
            'timelvl2': self.tempslvl2,

        }

        json_data = json.dumps( data )

        with open( self.PATH, "w" ) as outfile:
            outfile.write( json_data )

    def importToJson( self ):

        try:
            with open( self.PATH, 'r' ) as openfile:
                data = json.load( openfile )

            self.argentTotale = data['argentTotale']

            self.nombreTotalEnnemieTuer = data['nombreTotalEnnemieTuer']
            self.detailNombreTotalEnnemieTuer = data['detailNombreTotalEnnemieTuer']

            self.viePerdu = data['viePerdu']

            self.nombreVictoire = data['nombreVictoire']
            self.nombreDefaite = data['nombreDefaite']

            self.nombreTourConstruite = data['nombreTourConstruite']

            self.victoirelvl1 = data['victoirelvl1']
            self.tempslvl1 = data['timelvl1']
            self.victoirelvl2 = data['victoirelvl2']
            self.tempslvl2 = data['timelvl2']


        except( FileNotFoundError ):
            pass

    # Getters
    def get_argentTotale(self):
        return self.argentTotale

    def get_nombreTotalEnnemieTuer(self):
        return self.nombreTotalEnnemieTuer

    def get_detailNombreTotalEnnemieTuer(self):
        return self.detailNombreTotalEnnemieTuer

    def get_viePerdu(self):
        return self.viePerdu

    def get_nombreVictoire(self):
        return self.nombreVictoire

    def get_nombreDefaite(self):
        return self.nombreDefaite

    def get_nombreTourConstruite(self):
        return self.nombreTourConstruite

    # Setters
    def set_argentTotale(self, argent):
        self.argentTotale = argent

    def set_nombreTotalEnnemieTuer(self, nombre):
        self.nombreTotalEnnemieTuer = nombre

    def set_detailNombreTotalEnnemieTuer(self, detail):
        self.detailNombreTotalEnnemieTuer = detail

    def set_viePerdu(self, vie):
        self.viePerdu = vie

    def set_nombreVictoire(self, victoire):
        self.nombreVictoire = victoire

    def set_nombreDefaite(self, defaite):
        self.nombreDefaite = defaite

    def set_nombreTourConstruite(self, tour):
        self.nombreTourConstruite = tour

# t = statistique()