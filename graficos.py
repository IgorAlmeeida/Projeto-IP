# -*- coding: cp1252 -*-
import matplotlib.pyplot as plt
from matplotlib.pyplot import style

def plot_pizza(dicio,genero):
    valores = dicio.values()
    nomes = dicio.keys()
    valores_pct = []
    aux = sum(valores)
    cores = ["y","b","r","c","m"]
    for i in valores:
        valores_pct.append(i/aux)

    plt.pie(valores_pct, labels = nomes,colors = cores, startangle = 90, explode =(0,0,0,0.1,0) , autopct = "%1.1f%%")
    plt.title(u"Locais X Média, Gênero: {}".format(genero))
    plt.show()

def plot_linha(EU, NA):
    style.use("ggplot")
    x = []
    x1 = []
    y = []
    for i in range(len(EU)):
        x.append(EU[i][1])
        x1.append(NA[i][1])
        y.append(i+1)
        
    plt.plot(y,x, label = u"EU")
    plt.plot(y,x1, label = u"NA")
    plt.xlabel(u"Posição dos jogos mais vendidos em cada região.")
    plt.ylabel(u"Total de Vendas")
    plt.title(u"Top {} de vendas, EU e NA".format(len(EU)))
    plt.legend()
    plt.show()

def plot_barras (dicio,publica):
    style.use("ggplot")
    x = dicio.keys()
    y = dicio.values()
     
    plt.bar(x,y)
    plt.xlabel(u"Plataformas")
    plt.ylabel(u"Vendas")
    plt.title(u"Vendas Globais de jogos por plataforma.\n Publicadora: {}.".format(publica))
    plt.show()

def plot_barras_2(ano, medias):
    style.use("ggplot")

    fig = plt.figure()
    ax1 = plt.subplot2grid((1,1),(0,0))

    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
    for i in range (len(medias)):
        ax1.bar(medias[i][0],medias[i][1])
    plt.xlabel(u"Gêneros")
    plt.ylabel(u"Média de Vendas")
    plt.title(u"Média de vendas por gênero.\n Ano: {}.".format(ano))
    plt.show()
    
def plot_linha_2 (lista_ano, anoI, anoF):
    style.use("ggplot")
    lista = []
    for i in range((anoF - anoI) + 1):
        lista.append(anoI+i)

    for k in range(len(lista_ano)):
        plt.plot(lista,lista_ano[k][1:len(lista_ano[k])], label = "{}".format(lista_ano[k][0]))
    plt.xlabel(u"Anos")
    plt.ylabel(u"Quantidade de Jogos")
    plt.title(u"Quantidade de jogos pelos {} maiores gêneros.\nEntre {} e {}.".format(len(lista_ano),anoI, anoF))
    plt.legend()
    plt.show()

def plot_pontos (regiao, media):
    style.use("ggplot")
    for i in range (len(media)):
        plt.scatter(media[i][0],media[i][1])
    plt.xlabel(u"Plataformas")
    plt.ylabel(u"Medias")
    plt.title(u"Top 10 média de vendas por plataforma.\nRegião: {}.".format(regiao))
    plt.show()

def plot_pizza_2(dicio, ano, top):
    valores = dicio.values()
    nomes1 = dicio.keys()

    plt.pie(valores, labels = nomes1, autopct = "%1.1f%%")
    plt.title(u"Top {} dos jogos mais vendidos em {}.".format(top, ano))
    plt.show()
