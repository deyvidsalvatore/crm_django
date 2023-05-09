# Imagem de base com python e pip
FROM python:3.9-slim-buster

# Define variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Instala dependências do sistema
RUN apt-get update \
    && apt-get -y install default-libmysqlclient-dev gcc \
    && apt-get clean

# Cria e define o diretório de trabalho
WORKDIR /app

# Copia os arquivos do projeto para o diretório de trabalho
COPY . /app/

# Baixa o MySQL 8 e roda na porta 3306 com a senha "100senha"
RUN apt-get update \
    && apt-get -y install mysql-server \
    && service mysql start \
    && mysql -u root -e "ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '100senha';" \
    && sed -i 's/127.0.0.1/0.0.0.0/g' /etc/mysql/mysql.conf.d/mysqld.cnf \
    && service mysql restart \
    && mysql -u root -p100senha -e "CREATE DATABASE crm_django"

# Cria ambiente virtual e instala dependências
RUN python -m venv env \
    && . env/bin/activate \
    && pip install --upgrade pip \
    && pip install -r requirements.txt

# Executa o script mydb.py
RUN . env/bin/activate \
    && python mydb.py

# Roda o migrate e o servidor
CMD . env/bin/activate \
    && python manage.py migrate \
    && python manage.py runserver 0.0.0.0:8000
