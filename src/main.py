import sqlite3
import pandas as pd

# Caminho para o arquivo SQLite
file_path = 'E:/Projetos/analise_vendas/data/dataset.sqlite'  # Atualize conforme necessário

try:
    # Conexão ao banco de dados
    connectSQLite = sqlite3.connect(file_path)
    
    # 1. Consulta pra pegar o método de pagamento mais usado
    query_pagamento_mais_usado = ''' 
        SELECT payment_type, COUNT(*) as total_usos
        FROM order_payments
        GROUP BY payment_type
        ORDER BY total_usos DESC
        LIMIT 1;
    '''
    
    df_pagamento_mais_usado = pd.read_sql_query(query_pagamento_mais_usado, connectSQLite)
    
    if not df_pagamento_mais_usado.empty:
        pagamento_mais_usado = df_pagamento_mais_usado['payment_type'][0]
        print(f"O tipo de pagamento mais usado é: {pagamento_mais_usado}")
        
        # 2. Consulta segura a partir de parametros, matando o SQL Injection
        query_valor_medio = ''' 
            SELECT payment_type, AVG(payment_value) as valor_medio
            FROM order_payments
            WHERE payment_type = ?;
        '''
        
        # 3. Passar os valores de forma segura
        df_valor_medio = pd.read_sql_query(query_valor_medio, connectSQLite, params=(pagamento_mais_usado,))
        
        if not df_valor_medio.empty:
            valor_medio = df_valor_medio['valor_medio'][0]
            print(f"O valor médio gasto com {pagamento_mais_usado} é: R$ {valor_medio:.2f}")
        else:
            print(f"Não foram encontrados registros para o tipo de pagamento: {pagamento_mais_usado}")
    else:
        print("Nenhum tipo de pagamento foi encontrado.")
    
except sqlite3.Error as e:
    # Tratamento de erros de conexão ou execução de consultas de valores
    print(f"Erro ao acessar o banco de dados: {e}")
    
finally:
    # 4. Garantir que a conexão seja fechada
    if connectSQLite:
        connectSQLite.close()
