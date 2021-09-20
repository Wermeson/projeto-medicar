# projeto-medicar

Projeto desenvolvido para um processo seletivo da Intmed(https://github.com/Intmed-Software/desafio/blob/master/backend/README.md). Esse sistema é para uma clínica chamada Medicar, a ideia geral é auxiliar os clientes na marcação de consultas e gerenciar seu corpo médico.

Nesse projeto foi utilizado o sistema operacional Windows 10. Mas você pode utilizar o ambiente que o for mais conveniente. 
A versão do Python utilizada foi 3.9.5.

# Configurações
## Passo 1:

Faça o clone do repositório e entre na pasta do projeto:

```
$ git clone https://github.com/Wermeson/projeto-medicar.git
$ cd projeto-medicar
```

## Passo 2:
Crie o ambiente virtual (venv). 
```
$ python -m venv nome_da_virtualenv
```
## Passo 3:
Ative a sua env:

No linux:
```
$ source nome_da_virtualenv/bin/activate
```
No Windows:
```
$ nome_da_virtualenv/Scripts/activate
```

## Passo 4:
Com sua venv ativada, instale as dependências do projeto:

```
$ pip install -r requirements.txt
```

## Passo 5:
Nesse projeto foi utilizado o banco de dados Postgres, então você deve criar um database postgres.

Abra seu SGBD e execute o comando:
```
CREATE DATABASE NOME_DO_SEU_DATABASE
```

## Passo 6:
Dentro da pasta do projeto entre na pasta "medicar" e crie o arquvio ".env". Nessa pasta, já existe um arquivo modelo chamado ".env.sample". Faça uma cópia desse arquivo ".env.sample" para ".env".

No linux:
```
$ cp .env.sample .env
```
No Windows:
```
$ copy .env.sample .env
```
Abra o arquivo .env e substitua as seguintes informações: user, password, database e host(se for banco local, coloque localhost ou 127.0.0.1).

## Passo 7:
Dentro da raiz do projeto execute o comando para criar as tabelas do banco de dados:

```
$ python manage.py migrate
```

## Passo 8:
Crie um usuário passar acessar o admin:
```
$ python manage.py createsuperuser
```

Se estiver utilizando o gitbash acrescente o winpty:
```
$  winpty python manage.py createsuperuser
```

## Pronto!!!
Após todos esses passos o seu ambiente está configurado. Execute o comando abaixo para iniciar seu servidor e acesse a url http://127.0.0.1:8000/admin
```
$ python manage.py runserver
```

# Funcionalidades

## Interface administrativa

A interface administrativa contém as funcionalidades a seguir:

### Cadastrar Especialidades
É possível cadastrar as especialidades médicas (ex: CARDIOLOGIA, PEDIATRIA) que a clínica atende fornecendo as seguintes informações:

* **Nome:** nome da especialidade médica (obrigatório)

### Cadastrar Médicos
É possível cadastrar os médicos que podem atender na clínica fornecendo as seguintes informações:

* **Nome:** Nome do médico (obrigatório)
* **CRM:** Número do médico no conselho regional de medicina (obrigatório)
* **E-mail:** Endereço de e-mail do médico
* **Telefone:** Telefone do médico
* **Especialidade:** Especialidade na qual o médico atende

### Cadastrar Agenda
É possível criar uma agenda para um médico em um dia específico fornecendo as seguintes informações:

* **Médico:** Médico que será alocado (obrigatório)
* **Dia:** Data de alocação do médico (obrigatório)
* **Horários:** Lista de horários na qual o médico deverá ser alocado para o dia especificado (obrigatório)

## API
Com exceção dos endpoints de login e cadastro de usuário ('/users/'), todos os endpoints da API são protegidos por autenticação e necessitam receber token via cabeçalho HTTP `Authorization`. Veja um exemplo de requisição:

```
GET /especialidades/
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```

### Recursos da API:
- /users/ (post) 
- /login/ (post)
- /especialidades/ (get)
- /medicos/ (get)
- /agendas/ (get)
- /consultas/ (get,post,delete)

### /users/
Informe o username, password e email(opcional)

#### Requisição:

```
POST /users/
{
  "username": francisco,
  "password": "fr123456",
  "email": francisco@teste.com
}
```

#### Retorno:
```
{
    "username": "francisco",
    "email": "francisco@teste.com"
}
```

### /login/
Informe o username e password

#### Requisição:
```
POST /login/
{
    "username": "francisco",
    "password": "fr123456"
}
```

#### Retorno:
```
{
    "token": "10c69008c6a992197a0515b9dfb60dd87f5eef97"
}
```

### /especialidades/
#### Listar Especialidades
#### Requisição:
```
GET /especialidades/
```

#### Retorno:
```
[
    {
        "id": 1,
        "nome": "CARDIOLOGIA"
    },
    {
        "id": 2,
        "nome": "PEDIATRIA"
    },
    {
        "id": 3,
        "nome": "GINECOLOGIA"
    },
    {
        "id": 4,
        "nome": "CLÍNICO GERAL"
    }
]
```
#### Filtros
* Nome da especialidade (termo de pesquisa)

```
GET /especialidades/?search=ped
```


### /medicos/
#### Listar Médicos
#### Requisição:
```
GET /medicos/
```
#### Retorno:
```
[
    {
        "id": 1,
        "crm": 3087,
        "nome": "Tony Tony Chopper",
        "especialidade": {
            "id": 2,
            "nome": "PEDIATRIA"
        }
    },
    {
        "id": 2,
        "crm": 3711,
        "nome": "Drauzio Varella",
        "especialidade": {
            "id": 2,
            "nome": "PEDIATRIA"
        }
    },
    {
        "id": 3,
        "crm": 2544,
        "nome": "Gregory House",
        "especialidade": {
            "id": 1,
            "nome": "CARDIOLOGIA"
        }
    }
]
```
#### Filtros

* Identificador de uma ou mais especialidades
* Nome do médico (termo de pesquisa)

```
GET /medicos/?search=maria&especialidade=1&especialidade=3
```

### /agendas/
#### Listar Agendas Disponíveis
#### Requisição:
```
GET /agendas/
```
#### Retorno:
```
[
    {
        "id": 7,
        "medico": {
            "id": 3,
            "crm": 2544,
            "nome": "Gregory House",
            "especialidade": {
                "id": 1,
                "nome": "CARDIOLOGIA"
            }
        },
        "dia": "2021-09-19",
        "horarios": [
            "08:00:00",
            "09:00:00",
            "10:00:00",
            "12:00:00"
        ]
    },
    {
        "id": 8,
        "medico": {
            "id": 1,
            "crm": 3087,
            "nome": "Tony Tony Chopper",
            "especialidade": {
                "id": 2,
                "nome": "PEDIATRIA"
            }
        },
        "dia": "2021-09-19",
        "horarios": [
            "17:00:00",
            "19:00:00",
            "20:00:00"
        ]
    }
]
```
#### Filtros
* Identificador de um ou mais médicos
* Identificador de uma ou mais especialidades
* Intervalo de data

```
GET /agendas/?medico=1&especialidade=2&data_inicio=2020-01-01&data_final=2020-01-05
```

### /consultas/
#### Listar Consultas
#### Requisição GET:
```
GET /consultas/
```
#### Retorno GET:
```
[
    {
        "id": 7,
        "dia": "2021-09-19",
        "horario": "11:00:00",
        "data_agendamento": "2021-09-18T17:18:51.870568-03:00",
        "medico": {
            "id": 3,
            "crm": 2544,
            "nome": "Gregory House",
            "especialidade": {
                "id": 1,
                "nome": "CARDIOLOGIA"
            }
        }
    }
]
```
#### Adicionar Consulta
#### Requisição POST:
```
POST /consultas/
{
  "agenda_id": 8,
  "horario": "17:00"
}
```
#### Retorno POST:
```
{
    "id": 11,
    "dia": "2021-09-19",
    "horario": "17:00:00",
    "data_agendamento": "2021-09-18T20:56:52.937000-03:00",
    "medico": {
        "id": 1,
        "crm": 3087,
        "nome": "Tony Tony Chopper",
        "especialidade": {
            "id": 2,
            "nome": "PEDIATRIA"
        }
    }
}
```

#### Desmarcar uma Consulta
#### Requisição DELETE:
```
DELETE /consultas/11
```
#### Retorno DELETE:
Não há retorno (vazio)