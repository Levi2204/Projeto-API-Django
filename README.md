# Projeto-API-Django

Este é o backend refatorado do projeto de Achados e Perdidos. A aplicação foi reescrita utilizando o framework Django (substituindo a antiga versão em Flask), mantendo a mesma estrutura de front-end.

## Tecnologias Utilizadas

- **Backend**: Python, Django
- **Banco de Dados**: PostgreSQL (com `psycopg2`)
- **Frontend**: HTML5, CSS3, JavaScript (Fetch API) e Bootstrap

## Estrutura do Projeto

- `core/`: Configurações principais do projeto Django (settings, urls).
- `api/`: Aplicativo Django contendo os modelos, views e rotas de API.
- `frontend/`: Cópia dos arquivos front-end utilizados para interagir com a API.
- `db.sqlite3`: Banco de dados default (não utilizado, pois foi configurado o PostgreSQL).

## Modelos de Dados

O banco de dados utilizado é o `ProjetoBD` e contém as tabelas abaixo (gerenciadas pelo Django via migrations):

### ObjetoPerdido
- `id_objeto`: Inteiro, Auto Incremento (Chave Primária)
- `nome_objeto`: Texto (255 caracteres)
- `cor`: Texto (100 caracteres)
- `data_perdido`: Texto (50 caracteres)

### ObjetoAchado
- `id_objetoA`: Inteiro, Auto Incremento (Chave Primária)
- `nome_objeto_achado`: Texto (255 caracteres)
- `cor_achado`: Texto (100 caracteres)
- `nome_pessoa`: Texto (255 caracteres)
- `cpf`: Texto (14 caracteres)
- `contato`: Texto (200 caracteres)

## Instalação e Execução

### Pré-requisitos
- Python 3.x
- PostgreSQL

### Configuração do Banco de Dados

1. Certifique-se de que o PostgreSQL está rodando em sua máquina (localhost:5432).
2. O banco de dados `ProjetoBD` deve estar criado. O projeto tenta acessar o banco utilizando as credenciais `postgres` e senha `senha123`.

### Configurando o Backend (API)

1. Entre no diretório do novo projeto:
   ```bash
   cd Projeto-API-Django
   ```
2. Ative o ambiente virtual e instale as dependências caso não as tenha:
   ```bash
   source venv/bin/activate
   pip install django psycopg2-binary django-cors-headers
   ```
3. Execute as migrações (se necessário recriar as tabelas):
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
4. Inicie o servidor Django:
   ```bash
   python manage.py runserver
   ```
   O servidor rodará na porta `8000` (http://localhost:8000/).

### Executando o Frontend

O front-end não requer a execução de um servidor específico.
1. Abra a pasta `Projeto-API-Django/frontend`.
2. Dê um duplo clique no arquivo `index.html` para abri-lo no seu navegador.
3. Todas as requisições (como cadastrar e listar objetos) serão feitas automaticamente para `http://localhost:8000/`.
