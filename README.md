# cookiecutter-django
création d'un site django avec Vite et Bootstrap. Possibilité d'ajouter wagtail.

### Installer cookiecutter si besoin
    $ pip install cookiecutter

### Lancer cookiecutter
    $ cookiecutter gh:AnaisG14/cookiecutter-django-vite
Des questions seront posées et votre projet sera créé.

### Se placer dans le dossier créé
    $ cd projectName

### Créer le fichier .env et y ajouter les variables d'environnement
DEBUG=True

SECRET_KEY=SecretKey

ALLOWED_HOSTS=127.0.0.1,localhost

### Préparer l'environnement virtuel

    $ mkdir .venv
    $ pipenv install
    $ pipenv shell

### Faire les migrations django et créer un superuser
    $ python manage.py migrate
    $ python manage.py createsuperuser

### Préparer les dépendances frontend
Se placer dans le dossier frontend

    $ cd frontend
    $ npm install

### Tester en local
#### Lancer le serveur front depuis le dossier frontend
    $ npm run start
#### Lancer l'application django depuis le dossier de l'application
    $ python manage.py runserver

