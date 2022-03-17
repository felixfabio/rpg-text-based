from DataBase import *

class Enemy:
    def __init__(self,nome_criatura):
        self.nome_criatura = nome_criatura
        self.maxHP = []
        self.HP = []
        self.ATK = []
        self.DF = []
        self.XP = []
        self.gold = []
        self.loot = []
