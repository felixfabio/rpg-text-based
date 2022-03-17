import os
import sys
from DataBase import *

class Player:
    def __init__(self,nome):
        self.nome = nome
        self.classe = []
        self.lvl = 1
        self.xp = 0
        self.nxtxp = 100
        self.atri = ['','','','','']
        self.maxHP =[]
        self.HP = []
        self.maxMP = []
        self.MP = []
        self.baseAP = []
        self.baseAM = []
        self.baseDF = []
        self.reg = []
        self.arma_equipada = ''
        self.peito_equipado = ''
        self.elmo_equipado = ''
        self.calca_equipada = ''
        self.bota_equipada = ''
        self.offhand_equipada = ''
        self.hab1 = ['','']
        self.hab2 = ['','']
        self.hab3 = ['','']
        self.hab4 = ['','']
        self.bag = ['', '', '', '',
                    '', '', '', '',
                    '', '', '', '']

    @property
    def AP(self):
        AP = self.baseAP
        if self.arma_equipada == "Espada de Madeira":
            AP += armas["Espada de Madeira"][1]
        if self.arma_equipada == "Arco de Madeira":
            AP += armas["Arco de Madeira"][1]
        return AP

    @property
    def AM(self):
        AM = self.baseAM
        if self.arma_equipada == "Cajado de Madeira":
            AM += armas["Cajado de Madeira"][1]
        if self.offhand_equipada == "Livro de Encantamentos Básico":
            AM += offhand["Livro de Encantamentos Básico"][1]
        return AM

    @property
    def DF(self):
        DF = self.baseDF
        if self.offhand_equipada == "Escudo de Madeira":
            DF += offhand["Escudo de Madeira"][2]
        if self.offhand_equipada == "Livro de Encantamentos Básico":
            DF += offhand["Livro de Encantamentos Básico"][2]
        return DF