import json
import time
import requests
import uuid


active_tokens = set()

def generate_token():
    return str(uuid.uuid4())  

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
        username = input("User: ")
        password = input("Pass: ")

        if authenticate_user(username, password, auth_data):
          
            if username in active_tokens:
                print("User is already logged in on another device.")
                continue
            
         
            token = generate_token()
            active_tokens.add(username)
            
            print(f"Wait a few seconds, you are logged. Your token: {token}")
            
           
            response_code = requests.get(pastebin_code_url)
            
            if response_code.status_code == 200:
                python_code = response_code.text
                break
            else:
                print("ERROR 555.")
        else:
            print("User or pass was incorrect.")

try:
    exec(python_code)
except Exception as e:
    print(f"Error: {e}")

# Remova o token do usuário quando a sessão terminar
active_tokens.remove(username)
