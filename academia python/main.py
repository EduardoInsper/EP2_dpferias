import funcoes
import dados
print("\n")
print('\033[0;37;45m Olá! Você está na Fortuna DesSoft e terá a oportunidade de enriquecer! \033[0;0m')
print("\n")
nome=input("Qual o seu nome? ")
print(f"\nOk {nome}, você tem direito a pular 3 vezes e 2 ajudas!")                           
print('As opções de resposta são "A", "B", "C", "D", "ajuda", "pula" e "parar"!\n')
input("Aperte ENTER para continuar...")
print("\nO jogo já vai começar! Lá vem a primeira questão!\n")
print("\033[3;36m Vamos começar com questões do nível FACIL! \033[0;0m")                                      
continua=input("Aperte ENTER para continuar...\n\n")
id=1
pular=3
ajudas=2
ajuda_cond = False
nivel="facil"
lista_sorteada=[]
lista_dinheiro=[0, 1000, 5000, 10000, 30000, 50000, 100000, 300000, 500000, 1000000]
dinheiro = lista_dinheiro[id-1]
questao = funcoes.sorteia_questao_inedida(dados.dados, nivel, lista_sorteada)
while continua!="exit" and continua!="EXIT":
    if dinheiro == 1000000:
        print("\033[1;30;42m \nPARABÉNS, você zerou o jogo e ganhou um milhão de reais! \033[0;0m ")
        break
    print(funcoes.questao_para_texto(questao, id))
    resposta= input("\nSua resposta: ")
    opcoes=["A", "B", "C", "D", "pula", "ajuda", "parar"]
    while resposta not in opcoes:
        print('Opção inválida!')
        print('As opções de resposta são "A", "B", "C", "D", "ajuda", "pula" e "parar"!')
        resposta= input("\nSua resposta: ")
    else:
        if resposta==questao["correta"]:
            dinheiro = lista_dinheiro[id]
            print(f"\033[3;32m Você acertou! Seu prêmio atual é de R$ {dinheiro:.2f} \033[0;0m ")
            continua=input("Aperte ENTER para continuar ou EXIT para sair...\n\n")
            id+=1
            ajuda_cond = False
            if dinheiro==30000:
                print("\033[3;33m Parabéns! Você está no nível MEDIO\n \033[0;0m")
                nivel="medio"
            if dinheiro==300000:
                print("\033[3;31m Parabéns! Você está no nível DIFICIL\n \033[0;0m")
                nivel="dificil"
            questao = funcoes.sorteia_questao_inedida(dados.dados, nivel, lista_sorteada)
        elif resposta=="pula":
            if pular>0:
                pular -= 1
                if pular==0:
                    print(f"Ok, pulando! ATENÇÃO: Você não tem mais direito a pulos!")
                else:
                    print(f"Ok, pulando! Você ainda tem {pular} pulos! ")
                continua=input("Aperte ENTER para continuar...\n\n")
                questao = funcoes.sorteia_questao_inedida(dados.dados, nivel, lista_sorteada)
                ajuda_cond = False
            else:
                print("Não deu! Você não tem mais direito a pulos!")
                continua=input("Aperte ENTER para continuar...\n\n")
                print(funcoes.questao_para_texto(questao, id))
                resposta= input("\nSua resposta: ")     
        elif resposta=="ajuda":
            if ajuda_cond == False:
                ajudas -= 1
                if ajudas>0:
                    print(f"Ok, você tem {ajudas} ajudas restantes!")
                    continua=input("\nAperte ENTER para continuar... ")
                    print(f"\033[1;37m {funcoes.gera_ajuda(questao)} \033[0;0m")
                    ajuda_cond = True
                elif ajudas == 0:
                    print(f"Ok, você não tem mais ajudas!")
                    continua=input("\nAperte ENTER para continuar... ")
                    print(f"\033[1;37m {funcoes.gera_ajuda(questao)} \033[0;0m")
                    ajuda_cond = True
                else :
                    print("Não deu! Você não tem mais ajudas!")
                    continua=input("\nAperte ENTER para continuar... ")
            elif ajuda_cond == True:
                 print("Não deu! Você já pediu ajuda nessa questão!")
                 continua=input("\nAperte ENTER para continuar... ")
        elif resposta=="parar":
            quer_parar = input(f'Deseja mesmo parar [S/N]?? Caso responda "S", sairá com R$ {dinheiro}!')
            if quer_parar=="S":
                print(f"Ok, você saiu com R$ {dinheiro}!")
                break
        else:
            print(" \033[1;30;41m Que pena! Você errou e vai sair sem nada:( \033[0;0m ")
            continua=input("Aperte EXIT para sair ou ENTER para recomeçar... ")
            if continua=="exit" or continua=="EXIT":
                print("Obrigado por jogar!")
                break
            else:
                print("\033[0;37;45m O jogo vai recomeçar! \033[0;0m")
                continua=input("Aperte ENTER para continuar... ")
                id=1
                lista_sorteada=[]
                pular=3
                ajudas=2
                questao = funcoes.sorteia_questao_inedida(dados.dados, nivel, lista_sorteada)
                ajuda_cond = False