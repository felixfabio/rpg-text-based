import os
import sys
import random
                  #[0,   1  ,  2 ,   3  ]
#### Armas {"Nome":[ID, Dano, Def, Venda]}
armas = {"Espada de Madeira":[1, 5, 0, 10,
                              "Espada de Madeira","(Ataque Físico + 5)"],
         "Arco de Madeira":[2, 6, 0, 10,
                              "Arco de Madeira","(Ataque Físico + 6)"],
         "Cajado de Madeira":[3, 7, 0, 10,
                              "Cajado de Madeira","(Ataque Mágico + 7)"]}

offhand = {"Escudo de Madeira":[1, 0, 3, 10,
                              "Escudo de Madeira","(Defesa + 5)"],
           "Livro de Encantamentos Básico":[2, 3, 2, 10,
                              "Livro de Encantamentos Básico","(Ataque Mágico +3 | Defesa + 2)"]}

##### Equipamentos {"Nome":[ID,Dano,Def,Venda]}

peitoral = {'Peitoral de Pano (DF+3)':[1,0,3,5]}

calca = {'Calça de Pano (DF+2)':[1,0,2,5]}

elmo = {'Elmo de Pano (DF+2)':[1,0,2,5]}

bota = {'Bota de Pano (DF+1)':[1,0,1,5]}


###### CRIATURAS {"Nome":[ID, HP, ATK, DF, XP, Gold, Loot]}
criaturas = {'1':['Lobo Tropical', 85, 75, 30, 30, random.randint(3,12)],
             '2':['Urso da Floresta', 120, 60, 45, 30, random.randint(4,10)],
             '3':['Falcão Pequeno', 110, 70, 35, 30, random.randint(1,15)],
             '4':['Javali Selvagem', 115, 65, 40, 30, random.randint(4,8)]}

################{"Nome":[dano, mana, nome, lvl_min]}
habilidades_g = {"Mortal Strike":[1.2, 0.2, "Mortal Strike", 1],
                 "Rend":[1.4, 0.3, "Rend", 3],
                 "Bladestorm": [1.6, 0.5, "Bladestorm", 5],
                 "Crusader Strike":[1.8, 0.8, "Crusader Strike", 7]}

habilidades_m = {"Fireball":[1.5, 0.3, "Fireball", 1],
                 "Rain of Fire":[1.7, 0.4, "Rain of Fire", 3],
                 "Corruption":[1.8, 0.3, "Corruption",5],
                 "Pyroblast":[2.2, 0.5, "Pyroblast", 7]}

habilidades_c = {"Scorpid Sting":[1.6, 0.3, "Scorpid Sting", 1],
                 "Black Arrow":[1.7, 0.2, "Black Arrow", 3],
                 "Arcane Shot":[1.8, 0.4, "Arcane Shot", 5],
                 "Kill Shot":[2.0, 0.45, "Kill Shot", 7]}

habilidades_d = {"Wrath":[1.3, 0.3, "Wrath", 1],
                 "Starfire":[1.5, 0.4, "Starfire", 3],
                 "Hurricane":[1.8,0.5, "Hurricane", 5],
                 "Starfall":[2.5, 0.5, "Starfall", 7]}