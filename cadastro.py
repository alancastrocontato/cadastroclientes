import sqlite3, os, time
from datetime import date

conexao = sqlite3.Connection('db/banco.db')
cursor = conexao.cursor()

def criar_tabelas():

    cursor.execute('''CREATE TABLE IF NOT EXISTS clientes(
                      id INTEGER NOT NULL PRIMARY KEY,
                      nome VARCHAR(50) NOT NULL,
                      sobrenome VARCHAR(50) NOT NULL,
                      email VARCHAR(50),
                      cpf INTEGER,
                      rg INTEGER,
                      cnpj INTEGER,
                      telefone INTEGER,
                      celular INTEGER,
                      endereco VARCHAR(50),
                      bairro VARCHAR(50),
                      complemento VARCHAR(50),
                      cidade VARCHAR(50),
                      estado VARCHAR(50))''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS compras(
                      id INTEGER NOT NULL PRIMARY KEY,
                      produto VARCHAR(50) NOT NULL,
                      preco REAL NOT NULL,
                      data DATE NOT NULL)''')

criar_tabelas()


def carimbar_data():
    hoje = date.today()
    hoje_formatado = hoje.strftime('%d/%m/%Y')
    return (hoje_formatado)

def mostrar_hora():
    hora = time.strftime('%H:%M:%S')
    return print(hora)

def menu_principal():
    while True:
        print('****************************')
        print('**  -> MENU PRINCIPAL <-  **')
        print('**      [1] Clientes      **')
        print('**      [2] Relatórios    **')
        print('*************************')
        opcao = input('Escolha um número:')
        if opcao.isdigit():
            opcao = int(opcao)
            if opcao == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                return menu_clientes()
            elif opcao == 2:
                print(opcao)
                break
            else:
                print('*Essa opção não existe')
        else:
            print('*Digite apenas números')

def menu_clientes():
    print('*********************************')
    print('**     -> MENU CLIENTES <-     **')
    print('** [1] Cadastrar Novo Cliente  **')
    print('** [2] Consultar Clientes  **')
    print('** [3] Creditar Conta          **')
    print('** [4] Debitar  Conta          **')
    print('*************************')
    while True:
        opcao = input('Escolha um número:')
        if opcao.isdigit():
            if opcao == '1':
                os.system('cls' if os.name == 'nt' else 'clear')
                return cadastrar_cliente()
            elif opcao == '2':
                os.system('cls' if os.name == 'nt' else 'clear')
                return consultar_clientes()
            elif opcao == '3':
                os.system('cls' if os.name == 'nt' else 'clear')
                return creditar_conta()
            elif opcao == '4':
                print(opcao)
                break
            else:
                print('*Essa opção não existe')
        else:
            print('*Digite apenas números')

def cadastrar_cliente():
    print('Insira os dados abaixo:\n')
    nome = input('Nome:')
    sobrenome = input('Sobrenome:')
    email = input('Email:')
    cpf = int(input('CPF:'))
    rg = int(input('RG:'))
    cnpj = int(input('CNPJ:'))
    telefone = int(input('Telefone:'))
    celular = int(input('Celular:'))
    endereco = input('Endereco:')
    bairro = input('Bairro:')
    complemento = input('Complemento:')
    cidade = input('Cidade:')
    estado = input('Estado:')
    while True:
        opcao = input('Confirmar Cadastro? [S] para sim e [N] para não')
        if opcao.isdigit():
            print('*Não use números')
        elif opcao.isalpha():
            if opcao == 'S' or opcao == 's' or opcao == 'Sim' or opcao == 'sim':
                cursor.execute('''INSERT INTO clientes(nome,sobrenome,email,cpf,rg,cnpj,telefone,celular,endereco,bairro,complemento,cidade,estado) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                               (nome,sobrenome,email,cpf,rg,cnpj,telefone,celular,endereco,bairro,complemento,cidade,estado))
                conexao.commit()
                print('Cadastrado com Sucesso')
                time.sleep(2)
                print('Redirecionando para o menu Principal')
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                return menu_principal()
            elif opcao == 'N' or opcao == 'n' or opcao == 'Nao' or opcao == 'nao' or opcao == 'Não' or opcao == 'não':
                print('Não')
                break
            else:
                print('Essa opção não existe')
                break
        else: print('Essa opção não existe')


def creditar_conta():
        produto = input('Nome do Produto:')
        preco = float(input('Preço do Produto:'))
        while True:
            opcao = input('Confirmar Cadastro? [S] para sim e [N] para não')
            if opcao.isdigit():
                print('*Não use números')
            elif opcao.isalpha():
                if opcao == 'S' or opcao == 's' or opcao == 'Sim' or opcao == 'sim':
                    cursor.execute('''INSERT INTO compras(produto,preco,data) VALUES (?,?,?)''',(produto,preco,carimbar_data()))
                    conexao.commit()
                    print('Cadastrado com Sucesso')
                    time.sleep(2)
                    print('Redirecionando para o menu Principal')
                    time.sleep(1)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    return menu_principal()
                elif opcao == 'N' or opcao == 'n' or opcao == 'Nao' or opcao == 'nao' or opcao == 'Não' or opcao == 'não':
                    print('Não')
                    break
                else:
                    print('Essa opção não existe')
                    break
            else:
                print('Essa opção não existe')


"""
def consultar_clientes():
    while True:
    pesquisar = input('nome:')
    for row in cursor.execute('''SELECT * FROM clientes '''):
        if pesquisar in row:
            print('ID:{}\nNOME:{}\nSOBRENOME:{}'.format(row[0],row[1],row[2]))
        else:
            print('Nada Encontrado')

"""


menu_principal()
menu_clientes()
creditar_conta()







