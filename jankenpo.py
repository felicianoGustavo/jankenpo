from time import sleep
import random
import os

def mostrar_menu(ponto1, ponto2):
    os.system("cls")
    print("=====================================================")
    print("||                   JANKENPON                     ||")
    print("=====================================================")
    print("||                   PLACAR                        ||")
    print("=====================================================")
    print("")
    print("                     VOCÊ: {}".format(ponto1))
    print("            MESTRE JANKEN: {}".format(ponto2))
    print("")
    print("=====================================================")
    print("||               FAÇA SUA JOGADA                   ||")
    print("=====================================================")
    print("||                1 - PEDRA                        ||")
    print("||                2 - PAPEL                        ||")
    print("||                3 - TESOURA                      ||")
    print("||                4 - SAIR                         ||")
    print("=====================================================")
    print("")
    print("QUAL VAI SER A SUA JOGADA ? ")
    opcao = int(input())
    return opcao

def janken(opcao, janken_opcao, ponto1, ponto2):
    print("")
    print("VOCÊ ESCOLHEU {}, VAMOS AO EMBATE !".format(janken_list[opcao - 1]))
    sleep(1)
    print("")
    print("PREPARADO ? ? ? ")
    sleep(1.5)
    print("")
    print(" J A N")
    sleep(1.5)
    print(" K E N")
    sleep(1.5)
    print(" P O !")
    sleep(1)
    print("")
    opcao = janken_list[opcao - 1]
    print("")
    print("VOCÊ JOGOU: {}".format(opcao))
    print("MESTRE JANKEN JOGOU: {}".format(janken_opcao))
    print("")

    if opcao == janken_opcao:
        print("")
        print("{} X {} = EMPATE".format(opcao, janken_opcao))
        print("")
    elif (opcao == "PEDRA" and janken_opcao == "TESOURA") or \
         (opcao == "PAPEL" and janken_opcao == "PEDRA") or \
         (opcao == "TESOURA" and janken_opcao == "PAPEL"):
        print("")
        print("{} GANHA DE {}, VOCÊ GANHOU!".format(opcao, janken_opcao))
        print("")
        ponto1 += 1
    else:
        print("")
        print("{} GANHA DE {}, MESTRE JANKEN GANHOU!".format(janken_opcao, opcao))
        print("")
        ponto2 += 1
    
    input("Pressione Enter para voltar ao menu...")
    return ponto1, ponto2

ponto1 = 0
ponto2 = 0
janken_list = ["PEDRA", "PAPEL", "TESOURA"]

while True:
    opcao = mostrar_menu(ponto1, ponto2)
    if opcao == 4:
        print("")
        print("Obrigado por se divertir com a gente, espero que volte logo!")
        print("")
        break
    janken_opcao = janken_list[random.randint(0, 2)]
    ponto1, ponto2 = janken(opcao, janken_opcao, ponto1, ponto2)
    print(ponto1, ponto2)
