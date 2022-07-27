import funcoes
import dados
print('\nOlá! Você está na Fortuna DesSoft e terá a oportunidade de enriquecer!\n')
nome=input("Qual o seu nome? ")
print(f"\nOk {nome}, você tem direito a pular 3 vezes e 2 ajudas!")                           
print('As opções de resposta são "A", "B", "C", "D", "ajuda", "pula" e "parar"!\n')
input("Aperte ENTER para continuar...")
print("\nO jogo já vai começar! Lá vem a primeira questão!\n")
print("Vamos começar com questões do nível FACIL!")                                      
continua=input("Aperte ENTER para continuar...")
pular=3
ajudas=2
id=1
nivel="facil"
lista_sorteada=[]
lista_dinheiro=[0, 1000, 5000, 10000, 30000, 50000, 100000, 300000, 500000, 1000000]
dinheiro = lista_dinheiro[id]
while continua!="exit" and continua!="EXIT" and dinheiro!=100000:
    questao= funcoes.sorteia_questao_inedida(dados.dados, nivel, lista_sorteada)
    lista_sorteada.append(questao)
    print(funcoes.questao_para_texto(questao, id))
    resposta= input(" ")
    opcoes=["A", "B", "C", "D", "pula", "ajuda"]
    if resposta in opcoes:
        id+=1
        if resposta==questao["correta"]:
            dinheiro = lista_dinheiro[id]
            print("Você acertou! Seu prêmio atual é de R$ {dinheiro:.2f} ")
            continua=input("Aperte ENTER para continuar ou EXIT para sair... ")
        else:
            print("Que pena! Você errou e vai sair sem nada:(")
            continua=input("Aperte EXIT para sair... ")