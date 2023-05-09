# CRM Django

Este é um projeto simples de CRM (Customer Relationship Management) usando Django.

## Configuração

Siga os seguintes passos para configurar e executar o projeto:

### Pré-requisitos

- [Python 3.6+](https://www.python.org/downloads/)
- [MySQL 8+](https://dev.mysql.com/downloads/mysql/)
- [pip](https://pip.pypa.io/en/stable/installing/)

### Docker
```
    docker build -t crm_django .
```

### Instalação (Sem docker)

1. Clone o repositório:

```
    git clone https://github.com/deyvidsalvatore/crm_django.git
    cd crm_django
```
2. Crie um ambiente virtual e ative-o:
```
    python -m venv env
    source env/bin/activate
```

3. Instale as dependências do projeto:
```
    pip install -r requirements.txt
```
4. Configure o banco de dados no settings.py
```
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'crm_django',
        'USER': 'root',
        'PASSWORD': '100senha',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```
5. Faça as migrações e depois rode
```
    python manage.py migrate
    python manage.py runserver
```
6. Acesse o aplicativo em `https://localhost:8080/`
