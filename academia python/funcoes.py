import random
def sorteia_questao_inedida(dicc_questao, nivel, lista_sorteadas):
    a=dicc_questao[nivel]
    b=random.choice(a)
    while b in lista_sorteadas:
        b=random.choice(a)
    lista_sorteadas.append(b)
    return b

def transforma_base(lista):
    res={ } 
    niveis=list()
    i=0
    while i< len(lista):
        a= str(lista[i]["nivel"])
        niveis.append(a)
        i+=1
    lista_unica_niveis = list(set(niveis))
    for i in lista_unica_niveis:
        listai=list()
        for dicc in lista:
            if dicc["nivel"]==i:
                listai.append(dicc)
                res[i]=listai
    return res

def questao_para_texto(dic_questao, id_questao):
    res = ('----------------------------------------\n')
    res += f'QUESTAO {id_questao}\n'
    res += (f'\n{dic_questao["titulo"]}\n\n')
    res += ('RESPOSTAS:')
    for alternativa, resp in dic_questao['opcoes'].items():
        res+= (f'\n{alternativa}: {resp}')
    return res

def gera_ajuda(dic_questao):
    dica = 0
    lista_erradas = []
    for alternativa in dic_questao['opcoes']:
        if dic_questao['correta'] != alternativa:
            lista_erradas.append(dic_questao['opcoes'][alternativa])
    sorteado = random.choice(lista_erradas)
    lista_erradas.remove(sorteado)
    if dica == 0:
        res = f"DICA:\nOpções certamente erradas: {sorteado}"
        dica += 1
    else:
        res += f' | {sorteado}'
    return res

def valida_questao(dic_questao):
    dic_problemas = {}
    dic_opcoes = {}
    conta_erro = 0
    if 'titulo' not in dic_questao:
        dic_problemas['titulo'] = 'nao_encontrado'
        conta_erro += 1
    elif dic_questao['titulo'].replace(' ', '').replace('\t', '') == '':
        dic_problemas['titulo'] = 'vazio'
        conta_erro += 1
    if 'nivel' not in dic_questao:
        dic_problemas['nivel'] = 'nao_encontrado'
        conta_erro += 1
    elif dic_questao['nivel'] not in ['facil', 'medio', 'dificil']:
        dic_problemas['nivel'] = 'valor_errado'
        conta_erro += 1
    if 'opcoes' not in dic_questao:
        dic_problemas['opcoes'] = 'nao_encontrado'
        conta_erro += 1
    elif len(dic_questao['opcoes']) != 4:
        dic_problemas['opcoes'] = 'tamanho_invalido'
        conta_erro += 1
    elif 'A' not in dic_questao['opcoes'] or 'B' not in dic_questao['opcoes'] or 'C' not in dic_questao['opcoes'] or 'D' not in dic_questao['opcoes']:
        dic_problemas['opcoes'] = 'chave_invalida_ou_nao_encontrada'
        conta_erro += 1
    else:
        for opcao in dic_questao['opcoes']:
            if dic_questao['opcoes'][opcao].replace('\t', '').replace(' ','') == '':
                dic_opcoes[opcao] = 'vazia'
                conta_erro += 1
        if len(dic_opcoes) != 0:
            dic_problemas['opcoes'] = dic_opcoes
    if 'correta' not in dic_questao:
        dic_problemas['correta'] = 'nao_encontrado'
        conta_erro += 1
    elif dic_questao['correta'] not in ['A', 'B', 'C', 'D']:
        dic_problemas['correta'] = 'valor_errado'
        conta_erro += 1
    if len(dic_questao) != 4:
        dic_problemas['outro'] = 'numero_chaves_invalido'
        conta_erro += 1
    if conta_erro == 0:
        return {}
    else:
        return dic_problemas
        
def valida_questoes(lista_questoes):
    listafinal = []
    for i in range(len(lista_questoes)):
        listafinal.append(valida_questao(lista_questoes[i]))
    return listafinal