import sys
import funcoes
sys.setrecursionlimit(16000)

def busca_1 (ano):
    generos = []
    banco_dados = open("vgsales.csv", "r")
    primeira_linha = True

    for linha in banco_dados:
        valores = linha.split(",")
        if valores[3] != "Year" and valores[4] != "Genre" and valores[10] != "Global_Sales":
            if valores[3] != "N/A":
                if float (valores[3]) == ano:
                    if primeira_linha == True:
                        generos.append(funcoes.escrever_lista_4(valores[4],valores[10]))
                        primeira_linha = False
                    else:
                        fun,var = funcoes.existencia(generos,valores[4])
                        if fun == False:
                            generos.append(funcoes.escrever_lista_4(valores[4],valores[10]))
                        else:
                            for l in range (len(generos)):
                                if generos[l][0] == var:
                                    generos[l][1] += float (valores[10])
                                    generos[l][2] += 1
    banco_dados.close()
    medias = funcoes.lista_bi_media (generos)
    medias_ord = funcoes.ordenar_lista_bi (medias)
    return medias_ord

def busca_3(ind, regiao):
    plataformas = []
    
    banco_dados = open("vgsales.csv", "r")
    primeira_linha = True
    
    for linha in banco_dados:
        valores = linha.split(",")
        if valores[2] != "Platform" and valores[ind] != regiao:
            if primeira_linha == True:
                plataformas.append(funcoes.escrever_lista_4(valores[2], valores[ind]))
                primeira_linha = False
            else:
                fun,var = funcoes.existencia(plataformas,valores[2])
                if fun == False:
                    plataformas.append(funcoes.escrever_lista_4(valores[2], valores[ind]))
                else:
                    for l in range (len(plataformas)):
                        if plataformas[l][0] == var:
                            plataformas[l][1] += float (valores[ind])
                            plataformas[l][2] += 1
    banco_dados.close()

    medias = funcoes.lista_bi_media (plataformas)

    medias_ord = funcoes.ordenar_lista_bi (medias)
    
    return medias_ord[0:9]

def busca_4 (nome_reg, genere, ind):
    lista = []
    
    banco_dados = open("vgsales.csv", "r")
    
    for linha in banco_dados:
        valores = linha.split(",")
        if valores[4] != "Genre" and valores[ind]!= nome_reg:
            if valores[4] == genere:
                lista.append(float (valores[ind]))
    banco_dados.close()
    soma = funcoes.soma_rec(lista)
    
    return soma/len(lista)

def busca_6 (ano1, ano2, num):
    genere = []
    genere_qtt = []
    lista_aux = []
    primeira_linha = True

    banco_dados = open("vgsales.csv", "r")
    for linha in banco_dados:
        valores = linha.split(",")
        if valores[3] != "Year" and valores[4]!= "Genre":
            if valores[3] != "N/A":
                if int (valores[3]) >= ano1 and int (valores[3]) <= ano2:
                    if primeira_linha == True:
                        genere.append(funcoes.escrever_lista (valores[3],valores[4])) 
                        primeira_linha = False
                    else:
                        fun,var = funcoes.existencia(genere,valores[3])
                        if fun == False:
                            genere.append(funcoes.escrever_lista (valores[3],valores[4]))
                        else:
                            for k in range (len(genere)):
                                if genere[k][0] == valores[3]:
                                    fun2, var2 = funcoes.existencia_2(genere[k],valores[4])
                                    if fun2 ==  True:
                                        genere[k][var2][1] += 1
                                    else:
                                        genere[k].append(funcoes.escrever_lista_2(valores[4]))
       
    banco_dados.close()

    primeiro_lista = True
    for k in range (len(genere)):
        for i in range (1,len(genere[k])):
            if primeiro_lista == True:
                genere_qtt.append(funcoes.escreve_lista_3(genere[k][i][0],genere[k][i][1]))
                primeiro_lista = False
            else:
                fun3, var3 = funcoes.existencia_3(genere_qtt,genere[k][i][0])
                if fun3 == True:
                    genere_qtt[var3][1] += genere[k][i][1]
                else:
                    genere_qtt.append(funcoes.escreve_lista_3(genere[k][i][0],genere[k][i][1]))
                    
    genere_qtt2 = funcoes.ordenar_lista_bi(genere_qtt)

    for i in range(len(genere)):
        for genero_ord in genere_qtt2:
            aux5 = funcoes.teste_qtt_gen (genere[i], genero_ord[0])
            if aux5 == False:
                lista_aux4 = []
                lista_aux4.append(genero_ord[0])
                lista_aux4.append(0)
                genere[i].append(lista_aux4)

    for k in range(num):
        lista_aux2 = []
        lista_aux2.append(genere_qtt2[k][0])
        lista_aux.append(lista_aux2)

    lista_ano2 = sorted(genere, key=lambda x : x[0],reverse=False)

    for generos in lista_aux:
        for i in range (len(lista_ano2)):
            for k in range(1, len (lista_ano2[i])):
                if generos[0] == lista_ano2[i][k][0]:
                    generos.append(lista_ano2[i][k][1])
    
    return lista_aux

def busca_7 (publicadora):
    dados = {}
    primeira_linha = True
    banco_dados = open("vgsales.csv", "r")
    for linha in banco_dados:
        valores = linha.split(",")
        if valores[2] != "Platform" and valores[5]!= "Publisher" and valores[10] != "Global_Sales":
            if valores[5] == publicadora:
                if primeira_linha == True:
                    dados.update({valores[2]:float(valores[10])})
                    primeira_linha = False
                else:
                    if valores[2] in dados:
                        for elementos, valor in dados.items():
                            if elementos == valores[2]:
                                aux = float (valor)
                                aux += float (valores[10])
                                dados.update({valores[2]:aux})
                                break
                    else:
                        dados.update({valores[2]:float(valores[10])})
    banco_dados.close()
    return dados

def busca_8 (nome, indice, x_primer):
    linhas = []
    banco_dados = open("vgsales.csv", "r")
    for linha in banco_dados:
        valores = linha.split(",")
        if valores[indice] != nome and valores[1] != "Name":
            tupla = (valores[1], float (valores[indice]))
            linhas.append(tupla)
    banco_dados.close()

    lista = funcoes.ordenar_lista_bi(linhas)
    listaT = tuple (lista)
    return listaT[0:x_primer]

def busca_10 (ano, top):
    jogos_do_ano = []
    banco_dados = open("vgsales.csv", "r")
    primeira_linha = True

    for linha in banco_dados:
        valores = linha.split(",")
        if valores[3] != "Year" and valores[1] != "Name" and valores[10] != "Global_Sales":
            if valores[3] != "N/A":
                if float (valores[3]) == ano:
                    if primeira_linha == True:
                        jogos_do_ano.append(funcoes.escreve_lista_3 (valores[1], float (valores[10])))

    lista = funcoes.retorno_recursivo(jogos_do_ano,top)
    dicionario = dict(lista)

    return dicionario
