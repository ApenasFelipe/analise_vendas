#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import logging
from dotenv import load_dotenv  # carregar as variáveis de ambiente

def main():
    """Executa tarefas administrativas de forma segura."""
    
    # Carrega as variáveis de ambiente do .env
    load_dotenv()

    # Pega DJANGO_SETTINGS_MODULE da variável de ambiente (seguro)
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', os.getenv('DJANGO_SETTINGS_MODULE', 'vendas_proj.settings'))

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        logging.error("Falha ao importar o Django. Verifique se o Django está instalado e o ambiente virtual está ativo.")
        raise ImportError(
            "Não foi possível importar o Django. Você tem certeza de que ele está instalado e disponível no seu "
            "PYTHONPATH? Você esqueceu de ativar um ambiente virtual?"
        ) from exc

    try:
        execute_from_command_line(sys.argv)
    except Exception as exc:
        logging.error(f"Ocorreu um erro ao executar o comando: {exc}")
        raise

if __name__ == '__main__':
    # Garante que o script seja executado diretamente
    if os.path.basename(sys.argv[0]) == os.path.basename(__file__):
        main()
    else:
        logging.error("O script não está sendo executado no contexto correto.")
        
