#!/usr/bin/env python
"""Utilitário de linha de comando para tarefas administrativas no PostgreSQL."""
import os
import sys
import logging
import psycopg2
from dotenv import load_dotenv  # carregar as variáveis de ambiente

def connect_to_postgres():
    """Conecta ao banco de dados PostgreSQL usando as variáveis de ambiente."""
    # Carrega as variáveis de ambiente do arquivo .env
    load_dotenv()

    try:
        # Obtém as credenciais do banco de dados a partir do .env
        connection = psycopg2.connect(
            dbname=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT')
        )
        logging.info("Conexão com PostgreSQL estabelecida com sucesso.")
        return connection

    except psycopg2.DatabaseError as error:
        logging.error(f"Erro ao conectar ao PostgreSQL: {error}")
        sys.exit(1)

def execute_query(connection, query):
    """Executa uma consulta SQL no banco de dados PostgreSQL."""
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        logging.info("Consulta executada com sucesso.")
        cursor.close()
    except psycopg2.Error as error:
        logging.error(f"Erro ao executar a consulta: {error}")
        connection.rollback()

def main():
    """Executa tarefas administrativas no PostgreSQL de forma segura."""
    connection = connect_to_postgres()

    # Exemplo: Consulta que deseja executar (substitua pelo que precisar)
    query = "SELECT NOW();"  # Exemplo de consulta para pegar a data e hora atual do servidor
    execute_query(connection, query)

    # Fechar a conexão após as operações
    connection.close()
    logging.info("Conexão com PostgreSQL fechada.")

if __name__ == '__main__':
    # Configura o logging para exibir mensagens de erro e info no console
    logging.basicConfig(level=logging.INFO)

    # Garante que o script seja executado diretamente
    if os.path.basename(sys.argv[0]) == os.path.basename(__file__):
        main()
    else:
        logging.error("O script não está sendo executado no contexto correto.")

