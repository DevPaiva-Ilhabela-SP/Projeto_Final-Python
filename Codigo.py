from faker import Faker #estou importando as bibliotecas faker requst e json
import requests
import json

Faker = Faker('pt_BR') #estou colocando o faker em um modo brasileiro

def create_persona() -> dict: #estou criando um def para guardar o ususario faker

    data = {
        'username' : Faker.user_name(),
        'email': Faker.email(),
        'password': Faker.password(),
        'phone': Faker.phone_number(),
        'address': Faker.address(),
        'cpf': Faker.cpf()
    }
    return data
 
persona = create_persona()

url = 'https://desafiopython.jogajuntoinstituto.org/api/users/' # URL para enviar os dados do usuário

headers = {
    'Content-Type': 'application/json' #estou afimando para o servidor que o que ele receber estara em formato json
}

response = requests.post(url, headers=headers, data=json.dumps(persona)) #estou pedindo para enviar as informaçoes para o servidor

if response.status_code >= 200 and response.status_code < 299:
    print("    ")
    print("Status code 200")
    print('Dados enviados com sucesso!')
    print("    ")
else:
    print(f'Falha ao enviar dados. Status code: {response.status_code}')

print(persona)

url_2 = 'https://desafiopython.jogajuntoinstituto.org/api/users/login/' #url para fazer login

login_data = {
    'email': persona["email"],
    'password': persona["password"] #estou especificando o que eu quero que ele puche para fazer login
}

print(login_data)

login_response = requests.post(url_2, json=login_data)

if login_response.status_code >= 200 and login_response.status_code < 300:
    print("    ")
    print('Login bem-sucedido!')
    print("Status code 200")
    print("    ")
    print(f'Login Response: {login_response.json()}')
    response_json = login_response.json()
    
    nome_arquivo = 'chave do usuario'
    with open(nome_arquivo, 'w') as arquivo: #abrir arquivo json na escrita 'w'
        json.dump(response_json, arquivo, indent=4)
else:
    print('A senha ou o email está incorreto, tente novamente.')