import os
import sys
from player import *
from enemy import *
from DataBase import *
import pickle

def define_classe():
    print('>> Digite o número referente a classe do seu herói: ')
    num_classe = input('>> ')
    if num_classe == '1':
        Personagem.classe = "Guerreiro"
        Personagem.atri = [8, 2, 3, 6, 2]
        Personagem.maxHP = 100 + round(2*Personagem.atri[3])
        Personagem.HP = Personagem.maxHP
        Personagem.maxMP = 30 + round(1.3*Personagem.atri[1])
        Personagem.MP = Personagem.maxMP
        Personagem.baseAP = 25 + round(2*Personagem.atri[0]+1.5*Personagem.atri[2])
        Personagem.baseAM = 10 + round(1.2*Personagem.atri[1]+1.2*Personagem.atri[4])
        Personagem.baseDF = 20 + round(1.5*Personagem.atri[0]+1.8*Personagem.atri[3])
        Personagem.bag[0] = armas["Espada de Madeira"][4]
        Personagem.bag[1] = offhand["Escudo de Madeira"][4]
        Personagem.hab1[0] = habilidades_g["Mortal Strike"][2]
        Personagem.hab1[1] = habilidades_g["Mortal Strike"][3]
        Personagem.hab2[0] = habilidades_g["Rend"][2]
        Personagem.hab2[1] = habilidades_g["Rend"][3]
        Personagem.hab3[0] = habilidades_g["Bladestorm"][2]
        Personagem.hab3[1] = habilidades_g["Bladestorm"][3]
        Personagem.hab4[0] = habilidades_g["Crusader Strike"][2]
        Personagem.hab4[1] = habilidades_g["Crusader Strike"][3]
        print('>> Personagem {}, {} criado com sucesso!'.format(Personagem.nome, Personagem.classe))
        print('>> Pressione qualquer tecla para continuar...')
        continuar = input('>> ')
        menu()
    elif num_classe == '2':
        Personagem.classe = "Mago"
        Personagem.atri = [2, 8, 2, 3, 6]
        Personagem.maxHP = 60 + round(1.5 * Personagem.atri[3])
        Personagem.HP = Personagem.maxHP
        Personagem.maxMP = 120 + round(2.5 * Personagem.atri[1])
        Personagem.MP = Personagem.maxMP
        Personagem.baseAP = 10 + round(1.2 * Personagem.atri[0] + 1.2 * Personagem.atri[2])
        Personagem.baseAM = 35 + round(2 * Personagem.atri[1] + 1.5 * Personagem.atri[4])
        Personagem.baseDF = 10 + round(1.2 * Personagem.atri[0] + 1.2 * Personagem.atri[3])
        Personagem.bag[0] = armas["Cajado de Madeira"][4]
        Personagem.bag[1] = offhand["Livro de Encantamentos Básico"][4]
        Personagem.hab1[0] = habilidades_m["Fireball"][2]
        Personagem.hab1[1] = habilidades_m["Fireball"][3]
        Personagem.hab2[0] = habilidades_m["Rain of Fire"][2]
        Personagem.hab2[1] = habilidades_m["Rain of Fire"][3]
        Personagem.hab3[0] = habilidades_m["Corruption"][2]
        Personagem.hab3[1] = habilidades_m["Corruption"][3]
        Personagem.hab4[0] = habilidades_m["Pyroblast"][2]
        Personagem.hab4[1] = habilidades_m["Pyroblast"][3]
        print('>> Personagem {}, {} criado com sucesso!'.format(Personagem.nome, Personagem.classe))
        print('>> Pressione qualquer tecla para continuar...')
        continuar = input('>> ')
        menu()
    elif num_classe == '3':
        Personagem.classe = "Caçador"
        Personagem.atri = [4, 3, 8, 4, 3]
        Personagem.maxHP = 80 + round(1.8 * Personagem.atri[3])
        Personagem.HP = Personagem.maxHP
        Personagem.maxMP = 50 + round(1.8 * Personagem.atri[1])
        Personagem.MP = Personagem.maxMP
        Personagem.baseAP = 30 + round(1.5 * Personagem.atri[0] + 2 * Personagem.atri[2])
        Personagem.baseAM = 10 + round(1.2 * Personagem.atri[1] + 1.2 * Personagem.atri[4])
        Personagem.baseDF = 15 + round(1.3 * Personagem.atri[0] + 1.5 * Personagem.atri[3])
        Personagem.bag[0] = armas["Arco de Madeira"][4]
        Personagem.hab1[0] = habilidades_c["Scorpid Sting"][2]
        Personagem.hab1[1] = habilidades_c["Scorpid Sting"][3]
        Personagem.hab2[0] = habilidades_c["Black Arrow"][2]
        Personagem.hab2[1] = habilidades_c["Black Arrow"][3]
        Personagem.hab3[0] = habilidades_c["Arcane Shot"][2]
        Personagem.hab3[1] = habilidades_c["Arcane Shot"][3]
        Personagem.hab4[0] = habilidades_c["Kill Shot"][2]
        Personagem.hab4[1] = habilidades_c["Kill Shot"][3]
        print('>> Personagem {}, {} criado com sucesso!'.format(Personagem.nome, Personagem.classe))
        print('>> Pressione qualquer tecla para continuar...')
        continuar = input('>> ')
        menu()
    elif num_classe == '4':
        Personagem.classe = "Druida"
        Personagem.atri = [2, 6, 2, 4, 7]
        Personagem.maxHP = 75 + round(1.7 * Personagem.atri[3])
        Personagem.HP = Personagem.maxHP
        Personagem.maxMP = 75 + round(2 * Personagem.atri[1])
        Personagem.MP = Personagem.maxMP
        Personagem.baseAP = 10 + round(1.2 * Personagem.atri[0] + 1.2 * Personagem.atri[2])
        Personagem.baseAM = 25 + round(1.5 * Personagem.atri[1] + 2 * Personagem.atri[4])
        Personagem.baseDF = 20 + round(1.3 * Personagem.atri[0] + 1.5 * Personagem.atri[3])
        Personagem.bag[0] = armas["Cajado de Madeira"][4]
        Personagem.bag[1] = offhand["Escudo de Madeira"][4]
        Personagem.hab1[0] = habilidades_d["Wrath"][2]
        Personagem.hab1[1] = habilidades_d["Wrath"][3]
        Personagem.hab2[0] = habilidades_d["Starfire"][2]
        Personagem.hab2[1] = habilidades_d["Starfire"][3]
        Personagem.hab3[0] = habilidades_d["Hurricane"][2]
        Personagem.hab3[1] = habilidades_d["Hurricane"][3]
        Personagem.hab4[0] = habilidades_d["Starfall"][2]
        Personagem.hab3[1] = habilidades_d["Hurricane"][3]
        print('>> Personagem {}, {} criado com sucesso!'.format(Personagem.nome, Personagem.classe))
        print('>> Pressione qualquer tecla para continuar...')
        continuar = input('>> ')
        menu()
    else:
        print('>> Digite uma opção válida!')
        define_classe()

def menu():
    os.system('cls')
    print('-------------------------------------------------------\n')
    print('-------- BEM VINDO AO RPG TEXT BASED EM PYTHON --------\n')
    print('-------------------------------------------------------\n')
    print("---------------- VOCE ESTÁ NA CAPITAL ----------------\n")
    print('| Nome: {} | Classe: {}'.format(Personagem.nome,Personagem.classe))
    print('| Level: {} | XP: ({}/{})'.format(Personagem.lvl,Personagem.xp,Personagem.nxtxp))
    print('| HP: ({}/{})           '
          '\n| MP: ({}/{})         '.format(Personagem.HP,Personagem.maxHP,Personagem.MP,Personagem.maxMP))
    print('| Ataque Físico:  {}    '.format(Personagem.AP))
    print('| Ataque Mágico:  {}    '.format(Personagem.AM))
    print('| Defesa:         {}    \n'.format(Personagem.DF))
    print(">> 1) Viajar entre as cidades")
    print(">> 2) Explorar os mapas")
    print(">> 3) Abrir seu inventário")
    print(">> 4) Ir para o comércio da cidade")
    print(">> 5) Salvar")
    print(">> 6) Sair do jogo")
    opcao = input(">> ")
    if opcao == '1':
        pass
    elif opcao == '2':
        Capital()
    elif opcao == '3':
        inventario()
    elif opcao == '4':
        print(">> Em construção...")
        continuar = input(">> ")
    elif opcao == '5':
        salvar_jogo()
    elif opcao == '6':
        sys.exit
        os.system('cls')
    else:
        menu()

## Mudar o nome dessa cidade
def Capital():
    os.system('cls')
    print('-------------------------------------------------------\n')
    print('-------- BEM VINDO AO RPG TEXT BASED EM PYTHON --------\n')
    print('-------------------------------------------------------\n')
    print(">> Nos arredores da Capital, você consegue acessar os seguintes locais: ")
    print(">> 1) Floresta Tropical")
    print(">> 2) Ruínas Piratas")
    print(">> 3) Pântano")
    print(">> 4) Calabouço")
    print(">> 0) Voltar")
    print(">> Escolha alguma dessas opções para explorar: ")
    opcao = input(">> ")
    if opcao == '1':
        Floresta_Tropical()
    elif opcao == '2':
        Ruínas_Piratas()
    elif opcao == '3':
        Pântano()
    elif opcao == '4':
        Calabouço()
    elif opcao == '0':
        menu()
    else:
        Capital()

def Floresta_Tropical():
    os.system('cls')
    print('-------------------------------------------------------\n')
    print('-------- VOCÊ ESTÁ NA FLORESTA TROPICAL----------------\n')
    print('-------------------------------------------------------\n')
    num_criatura = random.randint(1,4)
    num_criatura = str(num_criatura)
    nome_criatura = criaturas[num_criatura][0]
    global Inimigo
    Inimigo = Enemy(nome_criatura)
    Inimigo.maxHP = criaturas[num_criatura][1]
    Inimigo.HP = Inimigo.maxHP
    Inimigo.ATK = criaturas[num_criatura][2]
    Inimigo.DF = criaturas[num_criatura][3]
    Inimigo.XP = criaturas[num_criatura][4]
    Inimigo.gold = criaturas[num_criatura][5]
    print(">> Um {} apareceu!\n".format(Inimigo.nome_criatura))
    print(">> 1) Batalhar")
    print(">> 2) Fugir")
    print(">> 3) Sair deste local")
    opcao = input(">> ")
    if opcao == '1':
        batalha()
    elif opcao == '2':
        pass
    elif opcao == '3':
        Capital()


def Ruínas_Piratas():
    pass

def Pântano():
    pass

def Calabouço():
    pass

def batalha():
    os.system('cls')
    print('-------------------------------------------------------\n')
    print('-------- VOCÊ ESTÁ EM BATALHA--------------------------\n')
    print('-------------------------------------------------------\n')
    print("| {} ".format(Personagem.nome))
    print('| HP: ({}/{})           '
          '\n| MP: ({}/{})         '.format(Personagem.HP, Personagem.maxHP, Personagem.MP, Personagem.maxMP))
    print("------------------------")
    print("| {} ".format(Inimigo.nome_criatura))
    print("| HP ({}/{})            \n".format(Inimigo.HP,Inimigo.maxHP))
    print(">> Selecione a habilidade que deseja utilizar: ")
    if Personagem.lvl >= Personagem.hab4[1]:
        print(">> 1) {}".format(Personagem.hab1[0]))
        print(">> 2) {}".format(Personagem.hab2[0]))
        print(">> 3) {}".format(Personagem.hab3[0]))
        print(">> 4) {}".format(Personagem.hab4[0]))
    elif Personagem.lvl >= Personagem.hab3[1]:
        print(">> 1) {}".format(Personagem.hab1[0]))
        print(">> 2) {}".format(Personagem.hab2[0]))
        print(">> 3) {}".format(Personagem.hab3[0]))
    elif Personagem.lvl >= Personagem.hab2[1]:
        print(">> 1) {}".format(Personagem.hab1[0]))
        print(">> 2) {}".format(Personagem.hab2[0]))
    else:
        print(">> 1) {}".format(Personagem.hab1[0]))

    opcao = input(">> ")
    if opcao == '1':
        pass
    elif opcao == '2':
        pass
    elif opcao == '3':
        pass
    elif opcao == '4':
        pass
    else:
        batalha()


def inventario():
    os.system('cls')
    print('----------------- INVENTÁRIO ----------------')
    print('>> Elmo:     {}'.format(Personagem.elmo_equipado))
    print('>> Peitoral: {}'.format(Personagem.peito_equipado))
    print('>> Calça:    {}'.format(Personagem.calca_equipada))
    print('>> Bota:     {}'.format(Personagem.bota_equipada))
    print('>> Arma:     {}'.format(Personagem.arma_equipada))
    print('>> Off Hand: {}'.format(Personagem.offhand_equipada))
    print('>> Mochila: ')
    print('          > {}'.format(Personagem.bag[0]))
    print('          > {}'.format(Personagem.bag[1]))
    print('          > {}'.format(Personagem.bag[2]))
    print('          > {}'.format(Personagem.bag[3]))
    print('          > {}'.format(Personagem.bag[4]))
    print('          > {}'.format(Personagem.bag[5]))
    print('          > {}'.format(Personagem.bag[6]))
    print('          > {}'.format(Personagem.bag[7]))
    print('          > {}'.format(Personagem.bag[8]))
    print('          > {}'.format(Personagem.bag[9]))
    print('          > {}'.format(Personagem.bag[10]))
    print('          > {}'.format(Personagem.bag[11]))
    print('\n\n\n>> 1) Equipar algum item da mochila.')
    print('>> 0) Voltar.')
    opcao = input('>> ')
    if opcao == '0':
        menu()
    elif opcao == '1':
        equipar()
    else:
        inventario()

## Precisa melhorar essa bosta
def equipar():
    print(">> Digite corretamente e completamente o nome do item que deseja equipar: ")
    opcao = input(">> ")
    if opcao == Personagem.bag[0]:
        print(">> Deseja equipar {} ?".format(opcao))
        print(">> 1) Sim")
        print(">> 2) Não")
        continuar = input(">> ")
        if continuar == '1':
            if opcao in armas:
                Personagem.bag[0] = ''
                Personagem.arma_equipada = opcao
                print("{} equipado com sucesso! Pressione qualquer tecla para continuar".format(opcao))
                cont = input(">> ")
                inventario()
            elif opcao in offhand:
                Personagem.bag[0] = ''
                Personagem.offhand_equipada = opcao
                print("{} equipado com sucesso! Pressione qualquer tecla para continuar".format(opcao))
                cont = input(">> ")
                inventario()
            elif opcao in peitoral:
                Personagem.bag[0] = ''
                Personagem.peito_equipado = opcao
                print("{} equipado com sucesso! Pressione qualquer tecla para continuar".format(opcao))
                cont = input(">> ")
                inventario()
            elif opcao in calca:
                Personagem.bag[0] = ''
                Personagem.calca_equipada = opcao
                print("{} equipado com sucesso! Pressione qualquer tecla para continuar".format(opcao))
                cont = input(">> ")
                inventario()
            elif opcao in elmo:
                Personagem.bag[0] = ''
                Personagem.elmo_equipado = opcao
                print("{} equipado com sucesso! Pressione qualquer tecla para continuar".format(opcao))
                cont = input(">> ")
                inventario()
            elif opcao in bota:
                Personagem.bag[0] = ''
                Personagem.bota_equipada = opcao
                print("{} equipado com sucesso! Pressione qualquer tecla para continuar".format(opcao))
                cont = input(">> ")
                inventario()
            else:
                print(">> Item inexistente...pressione qualquer tecla")
                cont = input(">> ")
                inventario()
        elif continuar == '2':
            inventario()
        else:
            inventario()
    elif opcao == Personagem.bag[1]:
        print(">> Deseja equipar {} ?".format(opcao))
        print(">> 1) Sim")
        print(">> 2) Não")
        continuar = input(">> ")
        if continuar == '1':
            if opcao in armas:
                Personagem.bag[1] = ''
                Personagem.arma_equipada = opcao
                print("{} equipado com sucesso! Pressione qualquer tecla para continuar".format(opcao))
                cont = input(">> ")
                inventario()
            elif opcao in offhand:
                Personagem.bag[1] = ''
                Personagem.offhand_equipada = opcao
                print("{} equipado com sucesso! Pressione qualquer tecla para continuar".format(opcao))
                cont = input(">> ")
                inventario()
            elif opcao in peitoral:
                Personagem.bag[1] = ''
                Personagem.peito_equipado = opcao
                print("{} equipado com sucesso! Pressione qualquer tecla para continuar".format(opcao))
                cont = input(">> ")
                inventario()
            elif opcao in calca:
                Personagem.bag[1] = ''
                Personagem.calca_equipada = opcao
                print("{} equipado com sucesso! Pressione qualquer tecla para continuar".format(opcao))
                cont = input(">> ")
                inventario()
            elif opcao in elmo:
                Personagem.bag[1] = ''
                Personagem.elmo_equipado = opcao
                print("{} equipado com sucesso! Pressione qualquer tecla para continuar".format(opcao))
                cont = input(">> ")
                inventario()
            elif opcao in bota:
                Personagem.bag[1] = ''
                Personagem.bota_equipada = opcao
                print("{} equipado com sucesso! Pressione qualquer tecla para continuar".format(opcao))
                cont = input(">> ")
                inventario()
            else:
                print(">> Item inexistente...pressione qualquer tecla")
                cont = input(">> ")
                inventario()
        elif continuar == '2':
            inventario()
        else:
            inventario()
    elif opcao == Personagem.bag[2]:
        print(">> Deseja equipar {} ?".format(opcao))
        print(">> 1) Sim")
        print(">> 2) Não")
        continuar = input(">> ")
        if continuar == '1':
            if opcao in armas:
                Personagem.bag[2] = ''
                Personagem.arma_equipada = opcao
                print("{} equipado com sucesso! Pressione qualquer tecla para continuar".format(opcao))
                cont = input(">> ")
                inventario()
            elif opcao in offhand:
                Personagem.bag[2] = ''
                Personagem.offhand_equipada = opcao
                print("{} equipado com sucesso! Pressione qualquer tecla para continuar".format(opcao))
                cont = input(">> ")
                inventario()
            elif opcao in peitoral:
                Personagem.bag[2] = ''
                Personagem.peito_equipado = opcao
                print("{} equipado com sucesso! Pressione qualquer tecla para continuar".format(opcao))
                cont = input(">> ")
                inventario()
            elif opcao in calca:
                Personagem.bag[2] = ''
                Personagem.calca_equipada = opcao
                print("{} equipado com sucesso! Pressione qualquer tecla para continuar".format(opcao))
                cont = input(">> ")
                inventario()
            elif opcao in elmo:
                Personagem.bag[2] = ''
                Personagem.elmo_equipado = opcao
                print("{} equipado com sucesso! Pressione qualquer tecla para continuar".format(opcao))
                cont = input(">> ")
                inventario()
            elif opcao in bota:
                Personagem.bag[2] = ''
                Personagem.bota_equipada = opcao
                print("{} equipado com sucesso! Pressione qualquer tecla para continuar".format(opcao))
                cont = input(">> ")
                inventario()
            else:
                print(">> Item inexistente...pressione qualquer tecla")
                cont = input(">> ")
                inventario()
        elif continuar == '2':
            inventario()
        else:
            inventario()
    elif opcao == Personagem.bag[3]:
        print(">> Deseja equipar {} ?".format(opcao))
        print(">> 1) Sim")
        print(">> 2) Não")
        continuar = input(">> ")
        if continuar == '1':
            if opcao in armas:
                Personagem.bag[3] = ''
                Personagem.arma_equipada = opcao
                print("{} equipado com sucesso! Pressione qualquer tecla para continuar".format(opcao))
                cont = input(">> ")
                inventario()
            elif opcao in offhand:
                Personagem.bag[3] = ''
                Personagem.offhand_equipada = opcao
                print("{} equipado com sucesso! Pressione qualquer tecla para continuar".format(opcao))
                cont = input(">> ")
                inventario()
            elif opcao in peitoral:
                Personagem.bag[3] = ''
                Personagem.peito_equipado = opcao
                print("{} equipado com sucesso! Pressione qualquer tecla para continuar".format(opcao))
                cont = input(">> ")
                inventario()
            elif opcao in calca:
                Personagem.bag[3] = ''
                Personagem.calca_equipada = opcao
                print("{} equipado com sucesso! Pressione qualquer tecla para continuar".format(opcao))
                cont = input(">> ")
                inventario()
            elif opcao in elmo:
                Personagem.bag[3] = ''
                Personagem.elmo_equipado = opcao
                print("{} equipado com sucesso! Pressione qualquer tecla para continuar".format(opcao))
                cont = input(">> ")
                inventario()
            elif opcao in bota:
                Personagem.bag[3] = ''
                Personagem.bota_equipada = opcao
                print("{} equipado com sucesso! Pressione qualquer tecla para continuar".format(opcao))
                cont = input(">> ")
                inventario()
            else:
                print(">> Item inexistente...pressione qualquer tecla")
                cont = input(">> ")
                inventario()
        elif continuar == '2':
            inventario()
        else:
            inventario()
    elif opcao == Personagem.bag[4]:
        print(">> Deseja equipar {} ?".format(opcao))
        print(">> 1) Sim")
        print(">> 2) Não")
        continuar = input(">> ")
        if continuar == '1':
            if opcao in armas:
                Personagem.bag[4] = ''
                Personagem.arma_equipada = opcao
                print("{} equipado com sucesso! Pressione qualquer tecla para continuar".format(opcao))
                cont = input(">> ")
                inventario()
            elif opcao in offhand:
                Personagem.bag[4] = ''
                Personagem.offhand_equipada = opcao
                print("{} equipado com sucesso! Pressione qualquer tecla para continuar".format(opcao))
                cont = input(">> ")
                inventario()
            elif opcao in peitoral:
                Personagem.bag[4] = ''
                Personagem.peito_equipado = opcao
                print("{} equipado com sucesso! Pressione qualquer tecla para continuar".format(opcao))
                cont = input(">> ")
                inventario()
            elif opcao in calca:
                Personagem.bag[4] = ''
                Personagem.calca_equipada = opcao
                print("{} equipado com sucesso! Pressione qualquer tecla para continuar".format(opcao))
                cont = input(">> ")
                inventario()
            elif opcao in elmo:
                Personagem.bag[4] = ''
                Personagem.elmo_equipado = opcao
                print("{} equipado com sucesso! Pressione qualquer tecla para continuar".format(opcao))
                cont = input(">> ")
                inventario()
            elif opcao in bota:
                Personagem.bag[4] = ''
                Personagem.bota_equipada = opcao
                print("{} equipado com sucesso! Pressione qualquer tecla para continuar".format(opcao))
                cont = input(">> ")
                inventario()
            else:
                print(">> Item inexistente...pressione qualquer tecla")
                cont = input(">> ")
                inventario()
        elif continuar == '2':
            inventario()
        else:
            inventario()
    elif opcao == Personagem.bag[5]:
        print(">> Deseja equipar {} ?".format(opcao))
        print(">> 1) Sim")
        print(">> 2) Não")
        continuar = input(">> ")
        if continuar == '1':
            if opcao in armas:
                Personagem.bag[5] = ''
                Personagem.arma_equipada = opcao
                print("{} equipado com sucesso! Pressione qualquer tecla para continuar".format(opcao))
                cont = input(">> ")
                inventario()
            elif opcao in offhand:
                Personagem.bag[5] = ''
                Personagem.offhand_equipada = opcao
                print("{} equipado com sucesso! Pressione qualquer tecla para continuar".format(opcao))
                cont = input(">> ")
                inventario()
            elif opcao in peitoral:
                Personagem.bag[5] = ''
                Personagem.peito_equipado = opcao
                print("{} equipado com sucesso! Pressione qualquer tecla para continuar".format(opcao))
                cont = input(">> ")
                inventario()
            elif opcao in calca:
                Personagem.bag[5] = ''
                Personagem.calca_equipada = opcao
                print("{} equipado com sucesso! Pressione qualquer tecla para continuar".format(opcao))
                cont = input(">> ")
                inventario()
            elif opcao in elmo:
                Personagem.bag[5] = ''
                Personagem.elmo_equipado = opcao
                print("{} equipado com sucesso! Pressione qualquer tecla para continuar".format(opcao))
                cont = input(">> ")
                inventario()
            elif opcao in bota:
                Personagem.bag[5] = ''
                Personagem.bota_equipada = opcao
                print("{} equipado com sucesso! Pressione qualquer tecla para continuar".format(opcao))
                cont = input(">> ")
                inventario()
            else:
                print(">> Item inexistente...pressione qualquer tecla")
                cont = input(">> ")
                inventario()
        elif continuar == '2':
            inventario()
        else:
            inventario()
    elif opcao == Personagem.bag[6]:
        print(">> Deseja equipar {} ?".format(opcao))
        print(">> 1) Sim")
        print(">> 2) Não")
        continuar = input(">> ")
        if continuar == '1':
            if opcao in armas:
                Personagem.bag[6] = ''
                Personagem.arma_equipada = opcao
                print("{} equipado com sucesso! Pressione qualquer tecla para continuar".format(opcao))
                cont = input(">> ")
                inventario()
            elif opcao in offhand:
                Personagem.bag[6] = ''
                Personagem.offhand_equipada = opcao
                print("{} equipado com sucesso! Pressione qualquer tecla para continuar".format(opcao))
                cont = input(">> ")
                inventario()
            elif opcao in peitoral:
                Personagem.bag[6] = ''
                Personagem.peito_equipado = opcao
                print("{} equipado com sucesso! Pressione qualquer tecla para continuar".format(opcao))
                cont = input(">> ")
                inventario()
            elif opcao in calca:
                Personagem.bag[6] = ''
                Personagem.calca_equipada = opcao
                print("{} equipado com sucesso! Pressione qualquer tecla para continuar".format(opcao))
                cont = input(">> ")
                inventario()
            elif opcao in elmo:
                Personagem.bag[6] = ''
                Personagem.elmo_equipado = opcao
                print("{} equipado com sucesso! Pressione qualquer tecla para continuar".format(opcao))
                cont = input(">> ")
                inventario()
            elif opcao in bota:
                Personagem.bag[6] = ''
                Personagem.bota_equipada = opcao
                print("{} equipado com sucesso! Pressione qualquer tecla para continuar".format(opcao))
                cont = input(">> ")
                inventario()
            else:
                print(">> Item inexistente...pressione qualquer tecla")
                cont = input(">> ")
                inventario()
        elif continuar == '2':
            inventario()
        else:
            inventario()
    elif opcao == Personagem.bag[7]:
        print(">> Deseja equipar {} ?".format(opcao))
        print(">> 1) Sim")
        print(">> 2) Não")
        continuar = input(">> ")
        if continuar == '1':
            if opcao in armas:
                Personagem.bag[7] = ''
                Personagem.arma_equipada = opcao
                print("{} equipado com sucesso! Pressione qualquer tecla para continuar".format(opcao))
                cont = input(">> ")
                inventario()
            elif opcao in offhand:
                Personagem.bag[7] = ''
                Personagem.offhand_equipada = opcao
                print("{} equipado com sucesso! Pressione qualquer tecla para continuar".format(opcao))
                cont = input(">> ")
                inventario()
            elif opcao in peitoral:
                Personagem.bag[7] = ''
                Personagem.peito_equipado = opcao
                print("{} equipado com sucesso! Pressione qualquer tecla para continuar".format(opcao))
                cont = input(">> ")
                inventario()
            elif opcao in calca:
                Personagem.bag[7] = ''
                Personagem.calca_equipada = opcao
                print("{} equipado com sucesso! Pressione qualquer tecla para continuar".format(opcao))
                cont = input(">> ")
                inventario()
            elif opcao in elmo:
                Personagem.bag[7] = ''
                Personagem.elmo_equipado = opcao
                print("{} equipado com sucesso! Pressione qualquer tecla para continuar".format(opcao))
                cont = input(">> ")
                inventario()
            elif opcao in bota:
                Personagem.bag[7] = ''
                Personagem.bota_equipada = opcao
                print("{} equipado com sucesso! Pressione qualquer tecla para continuar".format(opcao))
                cont = input(">> ")
                inventario()
            else:
                print(">> Item inexistente...pressione qualquer tecla")
                cont = input(">> ")
                inventario()
        elif continuar == '2':
            inventario()
        else:
            inventario()
    elif opcao == Personagem.bag[8]:
        print(">> Deseja equipar {} ?".format(opcao))
        print(">> 1) Sim")
        print(">> 2) Não")
        continuar = input(">> ")
        if continuar == '1':
            if opcao in armas:
                Personagem.bag[8] = ''
                Personagem.arma_equipada = opcao
                print("{} equipado com sucesso! Pressione qualquer tecla para continuar".format(opcao))
                cont = input(">> ")
                inventario()
            elif opcao in offhand:
                Personagem.bag[8] = ''
                Personagem.offhand_equipada = opcao
                print("{} equipado com sucesso! Pressione qualquer tecla para continuar".format(opcao))
                cont = input(">> ")
                inventario()
            elif opcao in peitoral:
                Personagem.bag[8] = ''
                Personagem.peito_equipado = opcao
                print("{} equipado com sucesso! Pressione qualquer tecla para continuar".format(opcao))
                cont = input(">> ")
                inventario()
            elif opcao in calca:
                Personagem.bag[8] = ''
                Personagem.calca_equipada = opcao
                print("{} equipado com sucesso! Pressione qualquer tecla para continuar".format(opcao))
                cont = input(">> ")
                inventario()
            elif opcao in elmo:
                Personagem.bag[8] = ''
                Personagem.elmo_equipado = opcao
                print("{} equipado com sucesso! Pressione qualquer tecla para continuar".format(opcao))
                cont = input(">> ")
                inventario()
            elif opcao in bota:
                Personagem.bag[8] = ''
                Personagem.bota_equipada = opcao
                print("{} equipado com sucesso! Pressione qualquer tecla para continuar".format(opcao))
                cont = input(">> ")
                inventario()
            else:
                print(">> Item inexistente...pressione qualquer tecla")
                cont = input(">> ")
                inventario()
        elif continuar == '2':
            inventario()
        else:
            inventario()
    elif opcao == Personagem.bag[9]:
        print(">> Deseja equipar {} ?".format(opcao))
        print(">> 1) Sim")
        print(">> 2) Não")
        continuar = input(">> ")
        if continuar == '1':
            if opcao in armas:
                Personagem.bag[9] = ''
                Personagem.arma_equipada = opcao
                print("{} equipado com sucesso! Pressione qualquer tecla para continuar".format(opcao))
                cont = input(">> ")
                inventario()
            elif opcao in offhand:
                Personagem.bag[9] = ''
                Personagem.offhand_equipada = opcao
                print("{} equipado com sucesso! Pressione qualquer tecla para continuar".format(opcao))
                cont = input(">> ")
                inventario()
            elif opcao in peitoral:
                Personagem.bag[9] = ''
                Personagem.peito_equipado = opcao
                print("{} equipado com sucesso! Pressione qualquer tecla para continuar".format(opcao))
                cont = input(">> ")
                inventario()
            elif opcao in calca:
                Personagem.bag[9] = ''
                Personagem.calca_equipada = opcao
                print("{} equipado com sucesso! Pressione qualquer tecla para continuar".format(opcao))
                cont = input(">> ")
                inventario()
            elif opcao in elmo:
                Personagem.bag[9] = ''
                Personagem.elmo_equipado = opcao
                print("{} equipado com sucesso! Pressione qualquer tecla para continuar".format(opcao))
                cont = input(">> ")
                inventario()
            elif opcao in bota:
                Personagem.bag[9] = ''
                Personagem.bota_equipada = opcao
                print("{} equipado com sucesso! Pressione qualquer tecla para continuar".format(opcao))
                cont = input(">> ")
                inventario()
            else:
                print(">> Item inexistente...pressione qualquer tecla")
                cont = input(">> ")
                inventario()
        elif continuar == '2':
            inventario()
        else:
            inventario()
    elif opcao == Personagem.bag[10]:
        print(">> Deseja equipar {} ?".format(opcao))
        print(">> 1) Sim")
        print(">> 2) Não")
        continuar = input(">> ")
        if continuar == '1':
            if opcao in armas:
                Personagem.bag[10] = ''
                Personagem.arma_equipada = opcao
                print("{} equipado com sucesso! Pressione qualquer tecla para continuar".format(opcao))
                cont = input(">> ")
                inventario()
            elif opcao in offhand:
                Personagem.bag[10] = ''
                Personagem.offhand_equipada = opcao
                print("{} equipado com sucesso! Pressione qualquer tecla para continuar".format(opcao))
                cont = input(">> ")
                inventario()
            elif opcao in peitoral:
                Personagem.bag[10] = ''
                Personagem.peito_equipado = opcao
                print("{} equipado com sucesso! Pressione qualquer tecla para continuar".format(opcao))
                cont = input(">> ")
                inventario()
            elif opcao in calca:
                Personagem.bag[10] = ''
                Personagem.calca_equipada = opcao
                print("{} equipado com sucesso! Pressione qualquer tecla para continuar".format(opcao))
                cont = input(">> ")
                inventario()
            elif opcao in elmo:
                Personagem.bag[10] = ''
                Personagem.elmo_equipado = opcao
                print("{} equipado com sucesso! Pressione qualquer tecla para continuar".format(opcao))
                cont = input(">> ")
                inventario()
            elif opcao in bota:
                Personagem.bag[10] = ''
                Personagem.bota_equipada = opcao
                print("{} equipado com sucesso! Pressione qualquer tecla para continuar".format(opcao))
                cont = input(">> ")
                inventario()
            else:
                print(">> Item inexistente...pressione qualquer tecla")
                cont = input(">> ")
                inventario()
        elif continuar == '2':
            inventario()
        else:
            inventario()
    elif opcao == Personagem.bag[11]:
        print(">> Deseja equipar {} ?".format(opcao))
        print(">> 1) Sim")
        print(">> 2) Não")
        continuar = input(">> ")
        if continuar == '1':
            if opcao in armas:
                Personagem.bag[11] = ''
                Personagem.arma_equipada = opcao
                print("{} equipado com sucesso! Pressione qualquer tecla para continuar".format(opcao))
                cont = input(">> ")
                inventario()
            elif opcao in offhand:
                Personagem.bag[11] = ''
                Personagem.offhand_equipada = opcao
                print("{} equipado com sucesso! Pressione qualquer tecla para continuar".format(opcao))
                cont = input(">> ")
                inventario()
            elif opcao in peitoral:
                Personagem.bag[11] = ''
                Personagem.peito_equipado = opcao
                print("{} equipado com sucesso! Pressione qualquer tecla para continuar".format(opcao))
                cont = input(">> ")
                inventario()
            elif opcao in calca:
                Personagem.bag[11] = ''
                Personagem.calca_equipada = opcao
                print("{} equipado com sucesso! Pressione qualquer tecla para continuar".format(opcao))
                cont = input(">> ")
                inventario()
            elif opcao in elmo:
                Personagem.bag[11] = ''
                Personagem.elmo_equipado = opcao
                print("{} equipado com sucesso! Pressione qualquer tecla para continuar".format(opcao))
                cont = input(">> ")
                inventario()
            elif opcao in bota:
                Personagem.bag[11] = ''
                Personagem.bota_equipada = opcao
                print("{} equipado com sucesso! Pressione qualquer tecla para continuar".format(opcao))
                cont = input(">> ")
                inventario()
            else:
                print(">> Item inexistente...pressione qualquer tecla")
                cont = input(">> ")
                inventario()
        elif continuar == '2':
            inventario()
        else:
            inventario()
    else:
        print("Voce não possui este item...pressione qualquer tecla para continuar")
        continuar = input(">> ")
        inventario()

## Funcionando
def salvar_jogo():
    os.system('cls')
    print('-------------------------------------------------------\n')
    print('-------- BEM VINDO AO RPG TEXT BASED EM PYTHON --------\n')
    print('-------------------------------------------------------\n')
    print(">> Escolha onde deseja salvar seu jogo: ")
    print(">> 1) Jogo 1")
    print(">> 2) Jogo 2")
    print(">> 3) Jogo 3")
    print(">> 4) Jogo 4")
    salvar = input(">> ")
    if salvar == '1':
        with open("savefile1","wb") as f:
            pickle.dump(Personagem,f)
            print(">> Jogo salvo com sucesso! Aperte qualquer tecla para continuar")
            cont = input(">> ")
            menu()
    elif salvar == '2':
        with open("savefile2","wb") as f:
            pickle.dump(Personagem,f)
            print(">> Jogo salvo com sucesso! Aperte qualquer tecla para continuar")
            cont = input(">> ")
            menu()
    elif salvar == '3':
        with open("savefile3","wb") as f:
            pickle.dump(Personagem,f)
            print(">> Jogo salvo com sucesso! Aperte qualquer tecla para continuar")
            cont = input(">> ")
            menu()
    elif salvar == '4':
        with open("savefile4","wb") as f:
            pickle.dump(Personagem,f)
            print(">> Jogo salvo com sucesso! Aperte qualquer tecla para continuar")
            cont = input(">> ")
            menu()
    else:
        salvar_jogo()

## Funcionando
def carregar_jogo():
    os.system('cls')
    global Personagem
    print(">> Escolha qual jogo deseja carregar: ")
    print(">> 1) Jogo 1")
    print(">> 2) Jogo 2")
    print(">> 3) Jogo 3")
    print(">> 4) Jogo 4")
    carregar = input(">> ")
    if carregar == '1':
        if os.path.exists("savefile1") == True:
            with open("savefile1", "rb") as f:
                Personagem = pickle.load(f)
                menu()
        else:
            print(">> Voce não tem nada salvo aqui! Aperte qualquer tecla para continuar")
            cont = input(">> ")
            tela_inicial()
    elif carregar == '2':
        if os.path.exists("savefile2") == True:
            with open("savefile2", "rb") as f:
                Personagem = pickle.load(f)
                menu()
        else:
            print(">> Voce não tem nada salvo aqui! Aperte qualquer tecla para continuar")
            cont = input(">> ")
            tela_inicial()
    elif carregar == '3':
        if os.path.exists("savefile3") == True:
            with open("savefile3", "rb") as f:
                Personagem = pickle.load(f)
                menu()
        else:
            print(">> Voce não tem nada salvo aqui! Aperte qualquer tecla para continuar")
            cont = input(">> ")
            tela_inicial()
    elif carregar == '4':
        if os.path.exists("savefile4") == True:
            with open("savefile4", "rb") as f:
                Personagem = pickle.load(f)
                menu()
        else:
            print(">> Voce não tem nada salvo aqui! Aperte qualquer tecla para continuar")
            cont = input(">> ")
            tela_inicial()
    else:
        carregar_jogo()

## Funcionando
def tela_inicial():
    os.system('cls')
    print('-------------------------------------------------------\n')
    print('-------- BEM VINDO AO RPG TEXT BASED EM PYTHON --------\n')
    print('-------------------------------------------------------\n')
    print('>> 1) Criar novo Personagem.')
    print('>> 2) Carregar jogo existente.')
    print('>> 3) Sair.')
    opcao = input(">> ")
    if opcao == '1':
        global Personagem
        print(">> Digite o nome do seu personagem: ")
        nome = input('>> ')
        Personagem = Player(nome)
        print(">> Nome {} escolhido com sucesso".format(Personagem.nome))
        print('>> Agora está na hora de escolher a classe do seu heroí!\n')
        print('>> 1) GUERREIRO: Bravos empunhadores de espada, podem se beneficiar de sua força e '
          'resistência para travar longas batalhas com seus inimigos.\n')
        print('>> 2) MAGO: Muito estudiosos e inteligentes, aprenderam a dominar com maestria os recursos de '
              ' mana e desenvolveram habilidades mágicas utilizando diversos elementos.\n')
        print('>> 3) CAÇADOR: Velozes e ágeis, os caçadores utilizam armas de longo alcance e sua '
              'velocidade para rapidamente finalizar seus inimigos em batalhas de curta duração.\n')
        print('>> 4) DRUIDA: Amantes da natureza, se beneficiam de sua graça proveniente de  várias fontes '
              'para regenerar e também atacar inimigos.\n')
        define_classe()
    elif opcao == '2':
        carregar_jogo()
    elif opcao == '3':
        sys.exit
        os.system('cls')
    else:
        sys.exit
        os.system('cls')

tela_inicial()
