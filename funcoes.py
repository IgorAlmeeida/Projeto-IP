import sys
sys.setrecursionlimit(16000)

def qtt_top():
    num = input("Digite a quantidade de jogos nesse top: ")
    aux = teste_int(num)
    if aux == True:
        return int (num)
    else:
        print ("ERRO!\nO valor inserido não é um número.")
        return qtt_top()

def dados_6():
    aux = True
    while aux:
        anos_disponiveis ()
        quantidade_generos_disponiveis()
        ano_inicial = input("Digite o ano de início da busca: ")
        ano_final = input("Digite o ano de término da busca: ")
        qtt_gen = input("Digite a quantidade de gêneros desse top: ")
        aux2 = teste_int(ano_inicial)
        aux3 = teste_int(ano_final)
        aux4 = teste_int(qtt_gen)
        if aux2 == True and aux3 == True and aux4 == True:
            if int (ano_final) > 2017:
                print ("ERRO!\nO Ano de término não faz parte do bando de dados.\nPor favor insira novamente os dados.")
            elif int (ano_inicial) < 1980:
                print ("ERRO!\nO Ano de início não faz parte do bando de dados.\nPor favor insira novamente os dados.")
            elif int (ano_inicial) > int (ano_final):
                print ("ERRO!\nO intervalo digitado é negativo\nPor favor insira novamente os dados.")
            elif int (qtt_gen) > 12 or int (qtt_gen) < 1:
                print ("ERRO!\nA quantidade de gêneros solicitada não é compatível com o banco de dados\nPor favor insira novamente os dados.")
            else:
                aux = False
        else:
            print ("ERRO!\nUm ou mais dos dados inseridos não são números.\nInsira novamente esses dados.")
    return int (ano_inicial), int (ano_final), int (qtt_gen)

def print_cache():
    print ("Essa Busca já foi realizada.\nExibiremos os dados já armazenados em seu histórico.")

def print_artiscos():
    print ("*"*120)

def escolha_busca(nBusca):
    print_artiscos()
    print ("Busca {}".format(nBusca).center(120))
    print_artiscos()

def nome_grafico(busca):
    if busca == "B1" or busca == "B7":
        return "Barra"
    if busca == "B4" or busca == "B10":
        return "Pizza"
    if busca == "B3":
        return "Pontos"
    if busca == "B6" or busca == "B8":
        return "Linhas Sobrepostas"
    
def print_ano():
    anos_disponiveis ()
    ano = input("Digite o ano: ")
    aux = teste_int(ano)
    if aux == True:
        if int (ano) < 1980 or int (ano) > 2017:
            print ("ERRO!\nO Ano não faz parte do banco de dados.\nPor favor, insira novamente os dados.")
            return print_ano()
        else:
            ano2 = int (ano)
            return ano2
    else:
        print ("ERRO!\nValor inválido.")
        return print_ano()

def print_regiao():
    aux3 = True
    while aux3:
        print ("Escolha uma região:\n[1] - NA SALES\n[2] - EU SALES\n[3] - JP SALES\n[4] - OTHER SALES\n[5] - GLOBAL SALES")
        op3 = input("Opção: ")
        if op3 == "1":
            aux = "NA_Sales"
            aux2 = 6
            aux3 = False
        elif op3 == "2":
            aux = "EU_Sales"
            aux2 = 7
            aux3 = False
        elif op3 == "3":
            aux = "JP_Sales"
            aux2 = 8
            aux3 = False
        elif op3 == "4":
            aux = "Other_Sales"
            aux2 = 9
            aux3 = False
        elif op3 == "5":
            aux = "Global_Sales"
            aux2 = 10
            aux3 = False
        else:
            print ("ERRO!\nOpção INVÁLIDA.")
    return aux2, aux
            

def print_publi():
    lista = []
    banco_dados = open("vgsales.csv", "r")
    primeira_linha = True
    for linha in banco_dados:
        valores = linha.split(",")
        if valores[5] != "Publisher":
            if valores[5] not in lista:
                lista.append(valores[5])
    while True:
        print ("Mais de 500 publicadoras disponíveis.")
        publicadora = input("Digite a publicadora que deseja pequisar: ")
        publicadora2 = publicadora.title()
        if publicadora2 in lista:
            return publicadora2
        else:
            print ("ERRO!\nEsta publicadora não faz parte do banco de dados")
            print ("Por favor, insira novamente esse dado.")


def print_gen():
    var = input("Digite o valor do respectivo gênero:\n[1] - Sports\n[2] - Platform\n[3] - Racing\n[4] - Role-Playing\n[5] - Puzzle\n[6] - Misc\n[7] - Shooter\n[8] - Simulation\n[9] - Action\n[10] - Fighting\n[11] - Adventure\n[12] - Strategy\n")
    if var == "1":
        var2 = "Sports"
        return var2
    elif var == "2":
        var2 = "Platform"
        return var2
    elif var == "3":
        var2 = "Racing"
        return var2
    elif var == "4":
        var2 = "Role-Playing"
        return var2
    elif var == "5":
        var2 = "Puzzle"
        return var2
    elif var == "6":
        var2 = "Misc"
        return var2
    elif var == "7":
        var2 = "Shooter"
        return var2
    elif var == "8":
        var2 = "Simulation"
        return var2
    elif var == "9":
        var2 = "Action"
        return var2
    elif var == "10":
        var2 = "Fighting"
        return var2
    elif var == "11":
        var2 = "Adventure"
        return var2
    elif var == "12":
        var2 = "Strategy"
        return var2
    else:
        print ("ERRO!\nOpção INVÁLIDA.")
        return print_gen()

def anos_disponiveis ():
    print ("Anos disponíveis: 1980 até 2017.")

def quantidade_generos_disponiveis():
    print ("Gêneros disponíveis: 12 Gêneros.")

def teste_int (num):
    try:
        a = int(num)
        return True
    except:
        return False

def teste_qtt_gen (lista_bi_ano, genero):
    for i in range(1, len(lista_bi_ano)):
        if lista_bi_ano[i][0] == genero:
            return True
    return False
    

def existencia(lista,elemento):
    for i in lista:
        for k in i:
            if k == elemento:
                return True, k
    return False, 0

def existencia_2 (lista,elemento):
    for k in range (1,len(lista)):
        if lista[k][0] == elemento:
            return True, k
    return False, 0

def existencia_3 (lista, elemento):
    for i in range (len(lista)):
        if lista[i][0] == elemento:
            return True, i
    return False, 0
            

def escrever_lista (ano, genero):
    lista_aux = []
    lista_aux_2 = []
    lista_aux.append(ano)
    lista_aux_2.append(genero)
    lista_aux_2.append(1)
    lista_aux.append(lista_aux_2[:])
    return lista_aux

def escrever_lista_2 (genero):
    lista_aux = []
    lista_aux.append(genero)
    lista_aux.append(1)
    return lista_aux

def escreve_lista_3 (genero, valor):
    lista_aux = []
    lista_aux.append(genero)
    lista_aux.append(valor)
    return lista_aux

def escrever_lista_4(plataform, vendas):
    lista_aux = []
    lista_aux.append(plataform)
    lista_aux.append(float (vendas))
    lista_aux.append(1)
    return lista_aux

def lista_bi_media (lista):
    medias = []
    for i in range(len(lista)):
        lista_aux = []
        lista_aux.append(lista[i][0])
        lista_aux.append(lista[i][1]/lista[i][2])
        medias.append(lista_aux)
    return medias

def achar_indice(lista, elemento):
    for i in range(len(lista)):
        if lista[i][0] == elemento:
            return i

def ordenar_lista_bi (lista):
    lista2 =sorted(lista, key=lambda x : x[1],reverse=True)
    return lista2

def soma_rec(lista):
    if len(lista) == 1 :
        return lista[0]     
    else:
        return soma_rec(lista[1:len(lista)])+ lista[0]

def retorno_recursivo (lista,nElementos):
    if nElementos == 1:
        lista_aux = [lista[0]]
        return lista_aux
    else:
        lista_aux = [lista[0]]
        return lista_aux + retorno_recursivo(lista[1:len(lista)], nElementos - 1)

def convert_tuple_list (lista):
    lista_aux = []
    lista_aux2 = []
    for k in range(len(lista)):
        for tupla in lista[k]:
            aux = list(tupla)
            lista_aux2.append(aux)
        lista_aux.append(lista_aux2)
        lista_aux2 = []
        
    return lista_aux

def convert_list_tuple (lista):
    lista_aux = []
    lista_aux2 = []
    for k in range(len(lista)):
        for tupla in lista[k]:
            aux = tuple(tupla)
            lista_aux2.append(aux)
        lista_aux.append(tuple (lista_aux2))
        lista_aux2 = []
    
    return lista_aux

