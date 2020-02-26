import os
import json
import datetime
os.chdir("dados")
from funcoes import nome_grafico
from funcoes import print_artiscos


def hora ():
    tempo = datetime.datetime.now()
    return str(tempo)

def escreve_historico_generica(busca,entrada,saida,usuario):
    arquivo = open(usuario+".txt","a")
    arquivo.write(busca+"%")
    arquivo.write(str(entrada)+"%")
    aux = json.dumps(saida)
    arquivo.write(aux)
    arquivo.write("%")
    arquivo.write(hora ())
    arquivo.write("%\n")
    arquivo.close()

def escreve_historico_6(qtt_gen, generos_plot, ano1, ano2, usuario):
    arquivo = open(usuario+".txt","a")
    arquivo.write("B6%")
    arquivo.write(str(ano1)+"%"+str(ano2)+"%"+str(qtt_gen)+"%")
    aux = json.dumps(generos_plot)
    arquivo.write(aux)
    arquivo.write("%")
    arquivo.write(hora ())
    arquivo.write("%\n")
    arquivo.close()

def escreve_historico_10(entrada1,entrada2,saida,usuario):
    arquivo = open(usuario+".txt","a")
    arquivo.write("B10%")
    arquivo.write(str(entrada1)+"%"+str(entrada2)+"%")
    aux = json.dumps(saida)
    arquivo.write(aux)
    arquivo.write("%")
    arquivo.write(hora ())
    arquivo.write("%\n")
    arquivo.close()

def ler_historico_generica (busca,usuario, entrada):
    arquivo = open(usuario+".txt","r")
    for linhas in arquivo:
        linha = linhas.split("%")
        if linha[0] == busca:
            if linha[1] == entrada:
                dados = json.loads(linha[2])
                return True, dados
            
    return False, 0

def ler_historico_b1_b8 (busca, usuario, numero):
    arquivo = open(usuario+".txt","r")
    for linhas in arquivo:
        linha = linhas.split("%")
        if linha[0] == busca:
            if int (linha[1]) == int (numero):
                dados = json.loads(linha[2])
                return True, dados
            
    return False, 0

def ler_historico_b6 (usuario, entrada1, entrada2, entrada3):
    arquivo = open(usuario+".txt","r")
    for linhas in arquivo:
        linha = linhas.split("%")
        if linha[0] == "B6":
            if int (linha[1]) == entrada1 and int (linha[2])== entrada2 and int (linha[3])== entrada3:
                dados = json.loads(linha[4])
                return True, dados

    return False, 0

def ler_historio_b10(usuario, entrada1, entrada2):
    arquivo = open(usuario+".txt","r")
    for linhas in arquivo:
        linha = linhas.split("%")
        if linha[0] == "B10":
            if int (linha[1]) == int(entrada1) and int (linha[2]) == int (entrada2):
                dados = json.loads(linha[3])
                return True, dados
            
    return False, 0

def exibir_historico (usuario):
    arquivo = open(usuario+".txt","r")
    print_artiscos()
    print ("Histórico de Buscas".center(120))
    print_artiscos()
    for linhas in arquivo:
        linha = linhas.split("%")
        if linha[0] != "G" and linha[0] != "F":
            grafico = nome_grafico(linha[0])
            if linha[0] != "B6" and linha[0] != "B10":
                print ("Busca {}  - Entrada: {} - Saída: Gráfico {} - Data: ".format(linha[0][1], linha[1], grafico),linha[3])
            if linha[0] == "B6":
                print ("Busca {}  - Entrada: {}, {}, {} - Saída: Gráfico {} - Data: {}".format(linha[0][1],linha[1],linha[2],linha[3],grafico,linha[5]))
            if linha[0] == "B10":
                print ("Busca {} - Entrada: {}, {} - Saída: Gráfico {}- Data: {}".format(linha[0][1:3],linha[1],linha[2],grafico,linha[4]))
