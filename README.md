# projeto-medicar

Projeto desenvolvido para um processo seletivo. Esse sistema é para uma clínica chamada Medicar, a ideia geral é auxiliar os clientes na marcação de consultas e gerenciar seu corpo médico.

Nesse projeto foi utilizado o sistema operacional Windows 10, com a IDE PyCharm Community. Mas você pode utilizar o ambiente que o for mais conveniente.

# Configurações
## Passo 1:

Faça o clone do repositório e entre na pasta do projeto:

```
$ git clone https://github.com/Wermeson/projeto-medicar.git
$ cd projeto-medicar
```

## Passo 2:
Instale as dependências do projeto:

```
$ pip install -r requirements.txt
```

## Passo 3:
Como foi utilizado o banco de dados Postgres, você deve criar um database postgres.

## Passo 4:
Dentro da pasta do projeto entre na pasta "medicar" e crie o arquvio ".env". Nessa pasta, já existe um arquivo modelo chamado ".env.sample". Faça uma cópia desse arquivo ".env.sample" para ".env".

Abra o arquivo .env e substitua as seguintes informações: user, password, database e host(se for banco local, coloque localhost ou 127.0.0.1).

## Passo 5:
Dentro da raiz do projeto execute o comando para criar as tabelas do banco de dados:

```
$ python manage.py migrate
```

## Passo 6:
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

