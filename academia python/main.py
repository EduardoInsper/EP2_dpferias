import funcoes
import dados
print('\nOlá! Você está na Fortuna DesSoft e terá a oportunidade de enriquecer!\n')
nome=input("Qual o seu nome? ")
print(f"\nOk {nome}, você tem direito a pular 3 vezes e 2 ajudas!")                           
print('As opções de resposta são "A", "B", "C", "D", "ajuda", "pula" e "parar"!\n')
input("Aperte ENTER para continuar...")
print("\nO jogo já vai começar! Lá vem a primeira questão!\n")
print("Vamos começar com questões do nível FACIL!")                                      
continua=input("Aperte ENTER para continuar...\n\n")
id=1
pular=3
ajudas=2
ajuda_cond = False
nivel="facil"
lista_sorteada=[]
lista_dinheiro=[0, 1000, 5000, 10000, 30000, 50000, 100000, 300000, 500000, 1000000]
dinheiro = lista_dinheiro[id]
questao = funcoes.sorteia_questao_inedida(dados.dados, nivel, lista_sorteada)
while continua!="exit" and continua!="EXIT":
    if dinheiro == 1000000:
        print("\nPARABÉNS, você zerou o jogo e ganhou um milhão de reais!")
        break
    if dinheiro==30000:
        print("Parabéns! Você está no nível médio\n")
        nivel="medio"
    if dinheiro==300000:
        print("Parabéns! Você está no nível dificil\n")
        nivel="dificil"
    print(funcoes.questao_para_texto(questao, id))
    resposta= input("\nSua resposta: ")
    opcoes=["A", "B", "C", "D", "pula", "ajuda"]
    while resposta not in opcoes:
        print('Opção inválida!')
        print('As opções de resposta são "A", "B", "C", "D", "ajuda", "pula" e "parar"!')
        resposta= input("\nSua resposta: ")
    else:
        if resposta==questao["correta"]:
            dinheiro = lista_dinheiro[id]
            print(f"Você acertou! Seu prêmio atual é de R$ {dinheiro} ")
            continua=input("Aperte ENTER para continuar ou EXIT para sair...\n\n")
            id+=1
            ajuda_cond = False
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
                    print(funcoes.gera_ajuda(questao))
                    ajuda_cond = True
                elif ajudas == 0:
                    print(f"Ok, você não tem mais ajudas!")
                    continua=input("\nAperte ENTER para continuar... ")
                    print(funcoes.gera_ajuda(questao))
                    ajuda_cond = True
                else :
                    print("Não deu! Você não tem mais ajudas!")
                    continua=input("\nAperte ENTER para continuar... ")
            elif ajuda_cond == True:
                 print("Não deu! Você já pediu ajuda nessa questão!")
                 continua=input("\nAperte ENTER para continuar... ")
        else:
            print("Que pena! Você errou e vai sair sem nada:(")
            continua=input("Aperte EXIT para sair ou ENTER para recomeçar... ")
            if continua=="exit" or continua=="EXIT":
                print("Obrigado por jogar!")
                break
            else:
                print("O jogo vai recomeçar!")
                continua=input("Aperte ENTER para continuar... ")
                id=1
                lista_sorteada=[]
                pular=3
                ajudas=2
                questao = funcoes.sorteia_questao_inedida(dados.dados, nivel, lista_sorteada)
                ajuda_cond = False