#encoding:UTF-8
import random

while True: 
    aleatorio = random.randrange(0, 5)
    escolhaPc = ""
    print("1)Pedra")
    print("2)Papel")
    print("3)Tesoura")
    print("4)Lagarto")
    print("5)Spock")
    print("6)Sair do Programa")
    opcao = int(input("O que você escolhe: "))
    
    if opcao == 1:
        escolhaUsuario = "pedra"
    elif opcao == 2:
        escolhaUsuario = "papel"
    elif opcao == 3:
        escolhaUsuario = "tesoura"
    elif opcao == 4:
        escolhaUsuario = "lagarto"
    elif opcao == 5:
        escolhaUsuario = "spock"
    elif opcao == 6:
        print ("Nos vemos!")
        break
    else:
        print ("Valor Invalido")
        continue
        
    print("Tua escolha: ", escolhaUsuario)   
    if aleatorio == 0:
        escolhaPc = "pedra"
    elif aleatorio == 1:
        escolhaPc = "papel"
    elif aleatorio == 2:
        escolhaPc = "tesoura"
    elif aleatorio == 3:
        escolhaPc = "lagarto"
    elif aleatorio == 4:
        escolhaPc = "spock"

    print("PC escolheu: ", escolhaPc)
    print("...")
    
    if escolhaPc == "pedra" and escolhaUsuario == "papel":
        print("Ganhou, papel cobre pedra")
    elif escolhaPc == "spock" and escolhaUsuario == "papel":
        print("Ganhou, papel refuta spock")
    elif escolhaPc == "papel" and escolhaUsuario == "tesoura":
        print("Ganhou, tesoura corta papel")
    elif escolhaPc == "lagarto" and escolhaUsuario == "tesoura":
        print("Ganhou, lagarto decapta tesoura")
    elif escolhaPc == "tesoura" and escolhaUsuario == "pedra":
        print("Ganhou, pedra amassa tesoura")
    elif escolhaPc == "lagarto" and escolhaUsuario == "pedra":
        print("Ganhou, pedra esmaga lagarto")
    elif escolhaPc == "spock" and escolhaUsuario == "lagarto":
        print("Ganhou, lagarto envenea o spock ")
    elif escolhaPc == "papel" and escolhaUsuario == "lagarto":
        print("Ganhou, lagarto come papel")
    elif escolhaPc == "tesoura" and escolhaUsuario == "spock":
        print("Ganhou, spock quebra a tesoura")
    elif escolhaPc == "pedra" and escolhaUsuario == "spock":
        print("Ganhou, spock vaporiza a pedra")


        
        
    if escolhaUsuario == "pedra" and escolhaPc == "papel":
        print("Perdeu, papel cobre pedra")
    elif escolhaUsuario == "spock" and escolhaPc == "papel":
        print("Perdeu, papel refuta spock")
    elif escolhaUsuario == "lagarto" and escolhaPc == "tesoura":
        print("Perdeu, tesoura decapta lagarto")
    elif escolhaUsuario == "papel" and escolhaPc == "tesoura":
        print("Perdeu, tesoura corta papel")
    elif escolhaUsuario == "tesoura" and escolhaPc == "pedra":
        print("Perdeu, pedra amassa tesoura")
    elif escolhaUsuario == "lagarto" and escolhaPc == "pedra":
        print("Perdeu, pedra esmaga o lagarto")
    elif escolhaPc == escolhaUsuario:
        print("Empate")
    again = input("Jogar novamente? s/n: ")
    if 's' in again:
        continue
    elif 'n' in again:
        print("Nos vemos!")
        break
    else:
        print("Valor Invalido")