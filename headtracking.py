import requests
import json
import time

# Função para realizar a autenticação
def authenticate_user(username, password, auth_data):
    if username in auth_data and auth_data[username] == password:
        return True
    return False

# URL do Pastebin que contém o JSON de autenticação
pastebin_login_url = "https://pastebin.com/raw/URL_DO_JSON_DE_LOGIN"

# URL do Pastebin que contém o código Python
pastebin_code_url = "https://pastebin.com/raw/URL_DO_CODIGO_PYTHON"

# Faça uma solicitação GET para obter o JSON de autenticação
response = requests.get(pastebin_login_url)

# Verifique se a solicitação foi bem-sucedida
if response.status_code == 200:
    # Carregue o JSON de autenticação a partir da resposta
    auth_data = json.loads(response.text)

    while True:
        username = input("Digite seu nome de usuário: ")
        password = input("Digite sua senha: ")

        # Autenticar o usuário
        if authenticate_user(username, password, auth_data):
            print("Login bem-sucedido!")

            # Faça uma solicitação GET para obter o código Python
            response = requests.get(pastebin_code_url)

            # Verifique se a solicitação foi bem-sucedida
            if response.status_code == 200:
                # Carregue o código Python a partir da resposta
                python_code = response.text

                # Interrompa a execução atual
                break
            else:
                print("Não foi possível obter o código Python do Pastebin.")
        else:
            print("Login falhou. Por favor, verifique seu nome de usuário e senha.")

# O código Python obtido do Pastebin está armazenado na variável 'python_code'
# Você pode executar o código Python aqui
try:
    exec(python_code)
except Exception as e:
    print(f"Erro ao executar o código Python: {e}")
