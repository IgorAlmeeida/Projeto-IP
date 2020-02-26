import os
from buscas import *
from funcoes import *
from historico import *
from graficos import *

def print_menu_1():
    print_artiscos()
    print ("Banco de dados UAG 2019".center(120))
    print_artiscos()
    print ("[1] - Login.\n[2] - Cadastrar Usuário.")
    op = input("Opção: ")
    if op == "1":
        login()
    elif op == "2":
        cargo = input("Selecione o cargo:\n[1] - Gerente\n[2] - Funcionário\nOpção: ")
        if cargo == "1":
            criar_usuario("G")
        elif cargo == "2":
            criar_usuario("F")
        else:
            print ("Opção INVÁLIDA.")
            print_menu_1()
    else:
        print ("Opção INVÁLIDA.")
        print_menu_1()
    
def print_menu_2(cargo, usuario):
    if cargo == "G":
        print_artiscos()
        print ("Menu Principal".center(120))
        print ("Gerente\n".center(120))
        print_artiscos()
        informacoes_busca()
        menu_op = input("Escolha uma opção: ")
        if menu_op < "1" or menu_op > "9" or len(menu_op) > 1:
            print ("ERRO!\nOpção INVÁLIDA")
            print_menu_2("G",usuario)
        else:
            central_buscas (str(menu_op), cargo, usuario)

    else:
        print_artiscos()
        print ("Menu Principal".center(120))
        print ("Funcionário\n".center(120))
        print_artiscos()
        informacoes_busca()
        menu_op = input("Escolha uma opção: ")
        if menu_op < "1" or menu_op > "9" or len(menu_op) > 1:
            print ("ERRO!\nOpção INVÁLIDA")
            print_menu_2("F",usuario)
        else:
            if menu_op == "2" or menu_op == "3" or menu_op == "4" or menu_op == "5":
                print ("Esta opção não está disponível para o seu tipo de conta.\nPor favor, escolha outra opção.")
                print_menu_2("F",usuario)
            else:
                central_buscas (str(menu_op), cargo, usuario)

def print_menu_avancado (usuario, cargo):
    print_artiscos()
    print ("Menu Avançado".center(120))
    print_artiscos()
    print("[1] - Exibir histórico de buscas\n[2] - Alterar senha\n[3] - Excluir Usuário\n[4] - Menu Anterior")
    operacao = input("Escolha uma opção: ")
    if operacao == "1":   
        exibir_historico (usuario)
    elif operacao == "2":
        alterar_senha(usuario, cargo)
    elif operacao == "3":
        remover_usuario(usuario)
    elif operacao == "4":
        print_menu_2(cargo, usuario)
    else:
        print ("ERRO!\nOpção INVÁLIDA")
        print_menu_avancado (usuario, cargo)
    
            
def informacoes_busca():
        print ("[1] - BUSCA 1 - Média global de vendas por gênero de jogos que foram lançados em um determinado ano.")
        print ("[2] - BUSCA 3 - Top 10 média de vendas por plataforma para uma determinada região.")
        print ("[3] - BUSCA 4 - Média de vendas de acordo com um determinado gênero dos jogos vendidos em NA, EU, JP, Outros e global.") 
        print ("[4] - BUSCA 6 - Quantidade de jogos de acordo com os “X” maiores gênero num intervalo de anos.")
        print ("[5] - BUSCA 7 - Vendas Globais de jogos de cada plataforma de uma determinada Publicadora.")
        print ("[6] - BUSCA 8 - Relação Top “X” de jogos, vendas NA e vendas EU.")
        print ("[7] - BUSCA 10 - Top “x” vendas de jogos em um determinado ano.")
        print ("[8] - Menu Avançado")
        print ("[9] - Sair")

def criar_usuario(cargo):
    usuario = input("Usuário: ")
    if len(usuario)== 0:
        print ("ERRO!\nUsuário não inserido.")
        criar_usuario(cargo)
    if verificar_usuario(usuario) == True:
        print ("O usuário já cadastrado!")
        print_menu_1()
    else:
        aux = 4
        while aux > 0 :
            if aux == 1:
                print_menu_1()
            else:
                senha = input ("Senha: ")
                senha2 = input ("Confirmar Senha: ")
                if senha == senha2 and len(senha) > 0:
                    print ("Cadastro realizado com sucesso.")
                    aux = 0
                else:
                    if len(senha) == 0:
                        print("ERRO!\nSenha não inserida.")
                        aux -= 1
                    else:
                        print ("ERRO!\nSenhas distintas!")
                        aux -= 1
        
        arquivo = open(usuario+".txt","w")
        arquivo.write(cargo+"%")
        arquivo.write(usuario+"%")
        arquivo.write(senha+"%\n")
        arquivo.close()
        print_menu_2(cargo, usuario)
        
def verificar_usuario(usuario):
    return os.path.exists(usuario+".txt")

def remover_usuario(usuario):
    arquivo = open(usuario+".txt","r")
    for dados in arquivo:
        for i in range(3):
            print ("Digite sua senha para continuar.")
            senha = input("Senha: ")
            linha = dados.split("%")
            if senha == linha[2]:
                confirmar = input("[1] - Confirmar\n[2] - Cancelar\nOpção: ")
                if confirmar == "1":
                    arquivo.close()
                    os.remove(usuario+".txt")
                    print ("Usuário removido com sucesso.")
                    print_menu_1()
                elif confirmar == "2":
                    print_menu_1()
                else:
                    print ("Opção INVÁLIDA.")
                    remover_usuario(usuario)
            else:
                print ("Senha Incorreta.")
        break
    print_menu_1()

def alterar_senha(usuario, cargo):
    print_artiscos()
    print ("Alterar Senha.". center(120))
    print_artiscos()
    arquivo = open(usuario+".txt", "r")
    for linha in arquivo:
        linhas = linha.split("%")
        cargo = linhas[0]
        user = linhas[1]
        senha_antiga = linhas[2]
        break
    arquivo.close
    senha_antiga2 = input("Senha: ")
    senha_antiga3 = input("Confirmar Senha: ")
    if senha_antiga2 == senha_antiga3:
        if senha_antiga2 == senha_antiga:
            print ("Os dados do histórico de buscas serão perdidos com alteração da senha.\nDeseja continuar ?")
            op = input("1 - Sim.\n2 - Não.\n")
            if op == "1":
                senha_nova = input("Nova Senha: ")
                senha_nova1 = input("Confirmar Nova Senha: ")
                if senha_nova == senha_nova1:
                    arquivo = open(usuario+".txt", "w")
                    arquivo.write(cargo+"%")
                    arquivo.write(user+"%")
                    arquivo.write(senha_nova+"%\n")
                    arquivo.close()
                    print ("Senha alterada com sucesso!")
                    print_menu_2(cargo, usuario)
                else:
                    print ("As senhas não são iguais.")
                    alterar_senha(usuario, cargo)
            elif op == "2":
                print_menu_2(cargo, usuario)
            else:
                print("ERRO!\nOpção Inválida!")
                alterar_senha(usuario, cargo)
        else:
            print ("Senha incorreta.")
            alterar_senha(usuario, cargo)
    else:
        print ("As senhas não são iguais.")
        alterar_senha(usuario, cargo)      

def login():
    usuario = input("Usuário: ")
    if verificar_usuario(usuario) == True:
        arquivo = open(usuario+".txt","r")
        for dados in arquivo:
            for i in range(3):
                senha = input("Senha: ")
                linha = dados.split("%")
                senhaComp = linha[2]
                arquivo.close()
                if senha == senhaComp:
                    print ("Login realizado com sucesso.")
                    if linha[0] == "G":
                        print_menu_2("G", usuario)
                        break
                    else:
                        print_menu_2("F", usuario)
                        break
                else:
                    print ("Senha Incorreta.")
            print ("Você errou três vezes sua senha\nVocê será direcionado ao Menu Principal.")
            break
        print_menu_1()
    else:
        print ("Usuário Não cadastrado")
        print_menu_1()

def central_buscas (menu_op_2,cargo, usuario):

    if menu_op_2 == "1":
        escolha_busca("1")
        ano = print_ano()
        teste_historico, medias = ler_historico_b1_b8 ("B1",usuario, ano)
        
        if teste_historico == True:
            print_cache()
            escreve_historico_generica("B1",ano, medias, usuario)
        
        else:
            medias = busca_1(ano)
            escreve_historico_generica("B1",ano, medias, usuario)

        plot_barras_2 (ano, medias)

    elif menu_op_2 == "2":
        escolha_busca("3")
        ind, regiao = print_regiao()
        teste_historico, media = ler_historico_generica("B3",usuario, regiao)

        if teste_historico == True:
            print_cache()
            escreve_historico_generica("B3",regiao, media,usuario)

        else:
            media = busca_3(ind, regiao)
            escreve_historico_generica("B3",regiao, media,usuario)
        
        plot_pontos(regiao, media)
    
    elif menu_op_2 == "3":
        escolha_busca("4")
        genero = print_gen()
        teste_historico, dicionario = ler_historico_generica("B4",usuario, genero)
        
        if teste_historico == True:
            print_cache()
            escreve_historico_generica("B4",genero,dicionario ,usuario)
            
        else:
            dicionario = {}
            dicionario.update({"NA Sales":busca_4("NA_Sales",genero,6)})
            dicionario.update({"EU Sales":busca_4("EU_Sales",genero,7)})
            dicionario.update({"JP Sales":busca_4("JP_Sales",genero,8)})
            dicionario.update({"Other Sales":busca_4("Other_Sales",genero,9)})
            dicionario.update({"Global Sales":busca_4("Global_Sales",genero,10)})
            
            escreve_historico_generica("B4",genero,dicionario ,usuario)
            
        plot_pizza(dicionario, genero)

    elif menu_op_2 == "4":
        escolha_busca("6")
        ano1,ano2,qtt_gen = dados_6()
        teste_historico, generos_plot = ler_historico_b6 (usuario, ano1, ano2, qtt_gen)
        
        if teste_historico == True:
            print_cache()
            escreve_historico_6(qtt_gen, generos_plot, ano1, ano2, usuario)
            
        else:
            generos_plot = busca_6(ano1, ano2,qtt_gen)
            escreve_historico_6(qtt_gen, generos_plot, ano1, ano2, usuario)
            
        plot_linha_2 (generos_plot, ano1, ano2)
            
    elif menu_op_2 == "5":
        escolha_busca("7")
        publicadora = print_publi()
        teste_historico, vendas = ler_historico_generica("B7",usuario, publicadora)
        if teste_historico == True:
            print_cache()
            escreve_historico_generica("B7",publicadora,vendas ,usuario)
            
        else:
            vendas = busca_7 (publicadora)
            escreve_historico_generica("B7",publicadora,vendas ,usuario)
        
        plot_barras (vendas,publicadora)
            
    elif menu_op_2 == "6":
        escolha_busca("8")
        num = qtt_top()
        teste_historico, nPrimeros = ler_historico_b1_b8("B8",usuario, num)

        if teste_historico == True:
            print_cache()
            escreve_historico_generica("B8",num,nPrimeros,usuario)
        else:
            nPrimeros = [] 
            nPrimeros.append(busca_8("NA_Sales", 6,num))
            nPrimeros.append(busca_8("EU_Sales", 7,num))
            nPrimeros_escrever = convert_tuple_list (nPrimeros)
            escreve_historico_generica("B8",num,nPrimeros_escrever,usuario)
        
        nPrimerosF = tuple (convert_list_tuple (nPrimeros))
        plot_linha(nPrimerosF[1], nPrimerosF[0])

    elif menu_op_2 == "7":
        escolha_busca("10")
        ano = print_ano()
        top = qtt_top()
        teste_historico, top_jogos = ler_historio_b10(usuario, ano, top)
        if teste_historico == True:
            print_cache()
            escreve_historico_10(ano,top,top_jogos,usuario)
        else:
            top_jogos = busca_10 (ano, top)
            escreve_historico_10(ano,top,top_jogos,usuario)
    
        plot_pizza_2(top_jogos, ano, top)

    elif menu_op_2 == "8":
        print_menu_avancado(usuario, cargo)
        
    elif menu_op_2 == "9":
        print_artiscos()
        print ("Volte Sempre.".center(120))
        print_artiscos()
        print_menu_1()
    
    
    print_menu_2(cargo,usuario)
        
print_menu_1()
