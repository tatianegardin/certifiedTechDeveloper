#encoding:UTF-8
import random

userScore = 0
pcScore = 0
totalScore = 0


while True: 
    def percent():
        if totalScore > 0: 
            x = ((totalScore - pcScore) / totalScore) * 100
            return x
        elif totalScore == 0:
            x = 0
            return x



    aleatorio = random.randrange(0, 5)
    escolhaPc = ""
    print("1)Pedra")
    print("2)Papel")
    print("3)Tesoura")
    print("4)Lagarto")
    print("5)Spock")
    print("6) Show Scores")
    print("7)Sair do Programa")
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
        userScore = userScore + winUser
        pcScore = pcScore + pcWin
        totalScore = userScore + pcScore
        print ("Pontuações: ")
        print ("Usuário: ", userScore)
        print ("Pc: ", pcScore)
        print ("Porcentagem de vitórias: ", percent(), "% " )
        continue
    elif opcao == 7:
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

    winUser = 0
    pcWin = 0
    
    if escolhaPc == "pedra" and escolhaUsuario == "papel":
        print("Ganhou, papel cobre pedra")
        winUser += 1
    elif escolhaPc == "spock" and escolhaUsuario == "papel":
        print("Ganhou, papel refuta spock")
        winUser += 1
    elif escolhaPc == "papel" and escolhaUsuario == "tesoura":
        print("Ganhou, tesoura corta papel")
        winUser += 1
    elif escolhaPc == "lagarto" and escolhaUsuario == "tesoura":
        print("Ganhou, lagarto decapta tesoura")
        winUser += 1
    elif escolhaPc == "tesoura" and escolhaUsuario == "pedra":
        print("Ganhou, pedra amassa tesoura")
        winUser += 1
    elif escolhaPc == "lagarto" and escolhaUsuario == "pedra":
        print("Ganhou, pedra esmaga lagarto")
        winUser += 1
    elif escolhaPc == "spock" and escolhaUsuario == "lagarto":
        print("Ganhou, lagarto envenea o spock ")
        winUser += 1
    elif escolhaPc == "papel" and escolhaUsuario == "lagarto":
        print("Ganhou, lagarto come papel")
        winUser += 1
    elif escolhaPc == "tesoura" and escolhaUsuario == "spock":
        print("Ganhou, spock quebra a tesoura")
        winUser += 1
    elif escolhaPc == "pedra" and escolhaUsuario == "spock":
        print("Ganhou, spock vaporiza a pedra")
        winUser += 1


        
        
    if escolhaUsuario == "pedra" and escolhaPc == "papel":
        print("Perdeu, papel cobre pedra")
        pcWin += 1
    elif escolhaUsuario == "spock" and escolhaPc == "papel":
        print("Perdeu, papel refuta spock")
        pcWin += 1
    elif escolhaUsuario == "lagarto" and escolhaPc == "tesoura":
        print("Perdeu, tesoura decapta lagarto")
        pcWin += 1
    elif escolhaUsuario == "papel" and escolhaPc == "tesoura":
        print("Perdeu, tesoura corta papel")
        pcWin += 1
    elif escolhaUsuario == "tesoura" and escolhaPc == "pedra":
        print("Perdeu, pedra amassa tesoura")
        pcWin += 1
    elif escolhaUsuario == "lagarto" and escolhaPc == "pedra":
        print("Perdeu, pedra esmaga o lagarto")
        pcWin += 1
    elif escolhaUsuario == "spock" and escolhaPc == "lagarto":
        print("Perde, lagarto envenea o spock ")
        pcWin += 1
    elif escolhaUsuario == "papel" and escolhaPc == "lagarto":
        print("Perdeu, lagarto come papel")
        pcWin += 1
    elif escolhaUsuario == "tesoura" and escolhaPc == "spock":
        print("Perdeu, spock quebra a tesoura")
        pcWin += 1
    elif escolhaUsuario == "pedra" and escolhaPc == "spock":
        print("Perdeu, spock vaporiza a pedra")
        pcWin += 1
    elif escolhaPc == escolhaUsuario:
        print("Empate")
        pcWin += 1
    again = input("Jogar novamente? s/n: ")
    if 's' in again:
        continue
    elif 'n' in again:
        print("Nos vemos!")
        break
    else:
        print("Valor Invalido")








    

