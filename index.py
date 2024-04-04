import mysql.connector

# Configuração de conexão
host = 'localhost'
user = 'Aluno'
password = 'kfoew95j94j9d/'
database = 'cadastro'

# Conectar ao banco de dados
try:
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    if connection.is_connected():
        print("Conexão estabelecida com sucesso!")

    # Inputs para os dados do cliente
    nome = input("Digite o nome do cliente: ")
    endereco = input("Digite o endereço do cliente: ")
    cidade = input("Digite a cidade do cliente: ")
    cep = input("Digite o CEP do cliente: ")
    
    # Exemplo de execução de uma consulta para inserir dados na tabela clientes
    cursor = connection.cursor()
    insert_query = (
        "INSERT INTO clientes (Nome, Endereço, Cidade, CEP) "
        "VALUES (%s, %s, %s, %s)"
    )
    client_data = (nome, endereco, cidade, cep)
    cursor.execute(insert_query, client_data)
    connection.comit()
    print("Dados do cliente inseridos com sucesso.")
    
except mysql.connector.Error as e:
    print("Erro ao conectar ao banco de dados:", e)
    
finally:
    # Fechar a conexão
    if 'connection' in locals():
        connection.close()
    print("Conexão encerrada.")
