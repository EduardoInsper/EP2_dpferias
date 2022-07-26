import random
def sorteia_questao_inedida(dicc_questao, nivel, lista_sorteadas):
    a=dicc_questao[nivel]
    b=random.choice(a)
    while b in lista_sorteadas:
        b=random.choice(a)
    lista_sorteadas.append(b)
    return b