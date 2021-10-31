import mysql.connector
from mysql.connector import Error
from time import sleep


def conectar():
    try:
        global con
        con = mysql.connector.connect(host='localhost',database='Loja',password='',user='root')
    except Error as erro:
        print("Erro de conexão")

def consulta(idProd):
    try:
        conectar()
        consultar_SQL = ('SELECT * FROM produtos WHERE idProd = ' + idProd)
        cursor = con.cursor()
        cursor.execute(consultar_SQL)
        linhas = cursor.fetchall()

        for linha in linhas:
            print("ID: ", linha[0])
            print("Produto: ", linha[1])
            print("Preço: ", linha[2])
    except Error as erro:
        print("Falha ao consultar a tabela: {}".format(erro))
    finally:
        if (con.is_connected()):
            cursor.close()
            con.close()
def cadastrar(nome, preco):
    try:
        conectar()
        cursor = con.cursor()
        cadastro_produto = "INSERT INTO produtos (nome, preco) values (%s, %s)"
        valores = (nome, preco)
        cursor.execute(cadastro_produto, valores)
        con.commit()
        print("Cadastrando...")
        sleep(1)
        print("Cadastrado com sucesso")
        
    except Error as erro:
        print("Falaha ao cadastrar produto: {}".format(erro))
    finally:
        if (con.is_connected()):
            con.close()
            cursor.close()
def atualizar(declaracao):
    try:
        conectar()
        altera_preco = declaracao
        cursor = con.cursor()
        cursor.execute(altera_preco)
        con.commit()
        print("Alterando Preço...")
        sleep(1)
        print("Preço alterado com sucesso!")
    except Error as erro:
        print("Falha ao inserir os dados na tabela: {}".format(erro))
    finally:
        if (con.is_connected):
            cursor.close()
            con.close()

def produtos():
    try:
        conectar()
        cursor = con.cursor()
        Todos_Produtos = "SELECT nome, preco FROM produtos"
        cursor.execute(Todos_Produtos)

        for (nome, preco) in cursor:
            print(nome,preco)

    except Error as erro:
        print("Não foi possivel selecionar os produtos: {}".format(erro))
    finally:
        if (con.is_connected()):
            cursor.close()
            con.close()
if __name__ == '__main__':


    print("Bem vindo ao Banco de dados dos produtos cadastrados!")
    print("Para cadastrar um produto digite as informações a seguir e para atualizar os preços insira o ID produto que quer alterar")

    escolha = input("Deseja Alterar Preço ou Cadastrar produto ? [1] Cadastrar Produto [2] Atualizar Preço [3] Produtos cadastrados atualmente [4] Sair do Sistema: ")

    while escolha == ("1") or escolha == ("2") or escolha == ("3") or escolha == ("4"):
        if escolha == "1":
            print("Bem vindo ao campo de cadastro de produtos, para cadastrar insira as inforções do novo produto abaixo:")
            nome = input("\nNome Produto:")
            preco = input("\nPreço Produto:")
            cadastrar(nome, preco)

        elif escolha == "2":

            print("\nDigite o ID do produto a ser alterado: ")
            idProd = input("ID do Produto: ")

            consulta(idProd)

            print("\nEntre com o novo PREÇO do produto: ")
            precoProd = input("Preço: ")

            declaracao = "UPDATE produtos SET preco = " + precoProd + " where idProd = " + idProd

            atualizar(declaracao)

            print("\nDeseja consultar a nova atualização ? [S] [N]: ")
            continua = input("")
            if continua == "S":
                consulta(idProd)
            else:
                print("Finalizando sistema...")
                sleep(1)
                print("Até a proxima!")
                break
        elif escolha == "3":
            
            produtos()
        elif escolha == "4":
            print("Finalizando Sistema...")
            sleep(1)
            break
        else:
            print("Comando Errado, digite novamente.")
        escolha = input("Deseja Alterar Preço ou Cadastrar produto ? [1] Cadastrar Produto [2] Atualizar Preço [3] Produtos cadastrados atualmente [4] Sair do Sistema: ")
