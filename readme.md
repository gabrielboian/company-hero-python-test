# COMPANY HERO TEST - VAGA DJANGO
Um app simples feito com django e restframework

## Começando

### Pré-requisitos
Para usar esse projeto é necessário que você tenha um pré conhecimento em Python e Django. É útil também entender sobre RestFramework.
É importante também que você se sinta confortável com a linha de comando, uma vez que a maioria das ações é realizada pelo terminal.

No seu diretório de desenvolvimento digite os seguintes comandos:
```
mkdir nome-do-seu-diretorio
git clone --link-do-repositório--
virtualenv -p python3 env
```

### Instalação
No diretório criado:
Inicie a máquina virtual:
```
source env/bin/activate
```

Entre no diretório da aplicação e em caso de ambiente de desenvolvimento digite o seguinte:
```
git checkout dev
pip install -r requirements.txt
```
Em caso de ambiente de produção:
```
git checkout prod
pip install -r requirements.txt
```
### LEMBRE-SE
Em ambiente de desenvolvimento deve-se usar variáveis de ambiente. É importante manter todos os dados sensíveis longe da aplicação

### Rodando o projeto
Depois de realizado todos os requisitos anteriores você deve ter em sua máquina o POSTGRESQL que foi o banco de dados utilizado nesse projeto.
Existem algumas maneiras de rodar o banco, desde serviços online gratuitos, também como localmente tanto no seu computador quanto em um Container usando Docker.

Nesse caso eu usei Docker e o que você deve fazer é simples caso queira:
```
docker run -it nome-do-seu-banco -p 5432:5432 -e POSTGRES_PASSWORD=sua-senha -d postgres
```
Após o container iniciar
```
docker exec -it postgres /bin/bash
psql --username postgres
CREATE DATABASE django \g
CREATE USER django \g
ALTER USER django WITH SUPERUSER;
```
Pronto, agora seu banco de dados está criado e você pode rodar a aplicação no POSTGRESQL junto com o Docker.

Agora basta você rodar o comando:
```
python manage.py runserver
```

## API ENDPOINTS
O acesso dessa aplicação é feito completamente via REST API, então você pode utilizar o seu API Client preferido.
Existes dois pontos de entrada principais:
api/users/
api/company/

Dentro de usuários temos 2 caminhos a seguir:

O primeiro é apenas '/' - Methods disponíveis:

POST(para criar um usuário): JSON deve ser:
```json
"email": "your-email-here", - UNIQUE
"password": "your-password-here"
```
Esses são os parametros requeridos. Mas ele aceita mais como:
```json
"email": "your-email-here",
"password": "your-password-here",
"first_name": "your-name",
"last_name" : "your-name"
```

GET(Retorna uma lista de todos os usuários cadastrados)

PUT(Atualiza um usuário adicionando a ele uma empresa.):
```json
"email" : "the system will check if email exists",
"companies": "the system will check if the company exists"
```

O segundo caminho é "/list-companies/username" onde o usuário deve ser um usuário existente, previamente cadastrado - Methods disponíveis:
GET (É o único método disponível, retornando o usuário e as empresas ligadas a ele, você deve trocar "USERNAME" pelo EMAIL do usuário que deseja receber as informações)

Dentro de empresas nós também temos dois caminhos:
O primeiro é apenas '/' - Methods disponíveis:

POST(Para criar uma empresa):
```json
"cnpj": "number-of-cnpj",
"name" : "the-company-name" - UNIQUE
```

GET (Retorna uma lista de todas as empresas existentes)

O segundo caminho é "/users" - Methods disponíveis:

GET(Aqui usamos query params para ficar mais simples de fazer a busca) - Query params devem ser nesse modelo: "/users?company=COMPANY NAME".
Nessa opção retorna os usuários ligados a uma empresa.

# COMPANY HERO TEST - ENGLISH
A simple app made with Django and RestFramework.

## Starting

### Prerequisites
To be able to use this app it's important for you that you have some previous knowledge using Python and Django.
Also it's important that you know something about REST API and some previous knowledge with RestFramework

On your directory:
```
mkdir name-folder
git clone --link-of-the-project-repositorie--
virtualenv -p python3 env
```

### Installation
On the directory start your virtual environment
```
source env/bin/activate
```

Move to the main directory of the app and change the branch if you gonna test this app locally:
```
git checkout dev
pip install -r requirements.txt
```
In case of deployment environment:
```
git checkout prod
pip install -r requirements.txt
```
### REMEMBER
In deployment environment it's important that you user variables for your sensitive informations.

### Running the project
After you did all previous steps now you are able to run the project.
On this project I have used POSTGRESQL as my DB, so if you want to use one alternative it's running using docker.

I will show how if you want:
```
docker run -it db-name -p 5432:5432 -e POSTGRES_PASSWORD=your-pass -d postgres
```
After the container starts:
```
docker exec -it postgres /bin/bash
psql --username postgres
CREATE DATABASE django \g
CREATE USER django \g
ALTER USER django WITH SUPERUSER;
```
And now you are good to go. Your DB is up and running.

Now you just have to enjoy the app running the command below:
```
python manage.py runserver
```

## API ENDPOINTS
The access to this application is made from REST API, so you feel free to use your preferred API Client.
We have two main paths:
api/users/
api/company/

Inside of users we have:
The first one is just a '/' - Methods avaliable:

POST(to create an user): JSON must be like:
```json
"email": "your-email-here", - UNIQUE
"password": "your-password-here"
```

The above parameters they required but you are able to send some more informations like:
```json
"email": "your-email-here",
"password": "your-password-here",
"first_name": "your-name",
"last_name" : "your-name"
```

GET(Return a list of all users in DB)

PUT(You will use this endpoint to add a company to an user.):
```json
"email" : "the system will check if email exists",
"companies": "the system will check if the company exists"
```

The second path is "/list-companies/username" where the user must exists to fully function - Methods Available:
GET (It's the only method available to her where in USERNAME you have to put the EMAIL of the user you want to get)

Inside of company we have also two paths:
The first one is just a '/' - Methods avaliable:

POST(to create a company):
```json
"cnpj": "number-of-cnpj",
"name" : "the-company-name" - UNIQUE
```

GET (Retrieve all companies in DB)

The second path is "/users" - Methods avaliable:

GET(Here I preferred to use query params) - Query params must be like: "/users?company=COMPANY NAME".
Using this option we get all users linked to a company.

I'm still improving my english so I'm sorry about some wrong word. Thank you and I hope you enjoy.


## Author
* **Gabriel Boian**
* [Github](https://github.com/gabrielboian)
* [Linkedin](https://www.linkedin.com/in/gabriel-boian-9360b4189/)

## License

This project is licensed under the MIT License
