import funcoes
nome=input("Qual o seu nome? ")
print(f"Ok {nome}, você tem direito a pular 3 vezes e 2 ajudas!")                           
print("As opções de resposta são "A", "B", "C", "D", "ajuda", "pula" e "parar"! ")
input("Aperte ENTER para continuar...")
print("O jogo já vai começar! Lá vem a primeira questão!  ")
print("Vamos começar com questões do nível FACIL!")                                      
continua=input("Aperte ENTER para continuar...")
pular=3
ajudas=2
id=0
nivel="facil"
lista_sorteadas=list()
lista_dinheiro=[0, 1000, 5000, 10000, 30000, 50000, 100000, 300000, 500000, 1000000]
dinheiro=lista_dinheiro[0]
while continua!="exit" or continua!="EXIT":
    questao= funcoes.sorteia_questao_inedida(dados.dados, nivel, lista_sorteadas)
    lista_sorteada.append(questao)
    print(funcao.questao_para_texto(questao, id))
    resposta= input(" ")
    if resposta==questao["correta"]:
        dinheiro+= lista_dinheiro[id]
        print("Você acertou! Seu prêmio atual é de R$ {dinheiro:.2f} ")
        continua=input("Aperte ENTER para continuar ou EXIT para sair... ")
    else:
        print("Que pena! Você errou e vai sair sem nada:(")
        continua=input("Aperte EXIT para sair... ")