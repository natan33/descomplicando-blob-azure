from dotenv import load_dotenv
import os

# Carrega as variáveis do arquivo .env
load_dotenv()

# Acessando as variáveis
class Config:
    stora_account_key = os.getenv('ACCOUNT_KEY')
    account_url = os.getenv('AZURE_STORAGE_URL')
    connection_string = os.getenv("CONNECTION_STRING")
    container_name = os.getenv("CONTAINER_STRING")