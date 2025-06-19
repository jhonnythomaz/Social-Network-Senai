# Rede Social - Projeto Django

Este é um projeto de uma rede social completa desenvolvida com Python e o framework Django.

## Funcionalidades

*   Sistema completo de Autenticação (Cadastro, Login, Logout).
*   Criação de Posts com texto e imagem.
*   Feed de notícias que exibe posts do usuário e de seus amigos.
*   Perfis de Usuário individuais.
*   Sistema de Amizade com envio e aceitação/rejeição de convites.
*   Sistema de Likes em postagens.
*   Sistema de Comentários em postagens.
*   Sistema de Notificações para interações (likes, comentários, convites).
*   Interface estilizada com Bootstrap 5.

## Como Rodar o Projeto

Siga os passos abaixo para configurar e executar o projeto em sua máquina local.

### Pré-requisitos

*   Python 3.8+
*   Git

### Passos para Instalação

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/jhonnythomaz/Social-Network-Senai.git
    cd Social-Network-Senai
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    # Para Windows
    python -m venv venv
    .\venv\Scripts\activate

    # Para macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure as variáveis de ambiente:**
    *   Copie o arquivo de exemplo `.env.example` para um novo arquivo chamado `.env`.
    *   No arquivo `.env`, gere ou adicione uma `SECRET_KEY` para o Django.

5.  **Aplique as migrações do banco de dados:**
    ```bash
    python manage.py migrate
    ```

6.  **Crie um superusuário** para acessar a área administrativa:
    ```bash
    python manage.py createsuperuser
    ```

7.  **Execute o servidor de desenvolvimento:**
    ```bash
    python manage.py runserver
    ```

8.  Abra seu navegador e acesse `http://127.0.0.1:8000/`.