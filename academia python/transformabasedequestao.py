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