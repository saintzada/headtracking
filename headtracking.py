import json
import time
import requests
import uuid

# Estrutura para rastrear os tokens de autenticação
active_tokens = set()

def generate_token():
    return str(uuid.uuid4())  # Gere um token único usando UUID

def authenticate_user(username, password, auth_data):
    if username in auth_data and auth_data[username] == password:
        return True
    return False

pastebin_login_url = "https://pastebin.com/raw/fArbGgkR"  # Substitua pelo seu URL
pastebin_code_url = "https://pastebin.com/raw/gF7tyWCf"

response = requests.get(pastebin_login_url)

if response.status_code == 200:
    auth_data = json.loads(response.text)
    
    while True:
        username = input("User: ")
        password = input("Pass: ")

        if authenticate_user(username, password, auth_data):
            # Verifique se o usuário já está autenticado
            if username in active_tokens:
                print("User is already logged in on another device.")
                continue
            
            # Gere um token de autenticação exclusivo
            token = generate_token()
            active_tokens.add(username)
            
            print(f"Wait a few seconds, you are logged. Your token: {token}")
            
            # Solicite o código Python após a autenticação bem-sucedida
            response_code = requests.get(pastebin_code_url)
            
            if response_code.status_code == 200:
                python_code = response_code.text
                break
            else:
                print_red_title("ERROR 555.")
        else:
            print_red_title("User or pass was incorrect.")

try:
    exec(python_code)
except Exception as e:
    print(f"Error: {e}")

# Remova o token do usuário quando a sessão terminar
active_tokens.remove(username)
