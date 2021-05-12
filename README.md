# projetoifto
Projeto destinado a realização da atividade do curso FIC do IFTO

# criando o projeto
# criando env
python -m venv minhaenv

# ativando env
cd minhaenv

Scripts\activate

#instalando pacotes
pip install Django
python -m pip install --upgrade pip

# mostrar o que tem instalado
pip freeze

# Saindo da pasta
cd..

# criando projeto
cd hospitais
django-admin startproject hospitais .

# acessando  diretorio
cd hospitais
dir

# executando projeto
cd .. #saindo da pasta do projeto
python manage.py runserver

# caso necessário fazer migrates
python manage.py migrate

# Acessando do  admin
http://127.0.0.1:8000/admin

# Criando super usuário
## abre um novo cmd acessa o diretório da minhaenv
python manage.py createsuperuser

# Obs.: Realizar migrate (python manage.py migrate) para aplicar as atualizações para o banco de dados! Para o cadastro do superuser funcionar corretaemnte, me voltando a mensagem de cadastro com sucesso (Superuser created successfully)

Username (leave blank to use 'aluisio'): aluisiodev
Email address:
Password: 
Password (again): 

http://127.0.0.1:8000/admin/
login: 
senha: 

# inicializando  app
cd hospitais
python manage.py startapp hospitalapp
