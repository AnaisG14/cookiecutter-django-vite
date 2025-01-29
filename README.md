# cookiecutter-django
création d'un site django avec Vite et Bootstrap. Possibilité d'ajouter wagtail.

### Installer cookiecutter si besoin
    $ pip install cookiecutter

### Lancer cookiecutter
    $ cookiecutter gh:AnaisG14/cookiecutter-django-vite
Des questions seront posées et votre projet sera créé.

### Préparer l'environnement virtuel
Placer vous dans le dossier créé puis activer l'environnement virtuel

    $ cd projectName
    $ mkdir .venv
    $ pipenv install
    $ pipenv shell

### Ajouter les variables d'environnement dans le fichier .env
DEBUG=True
SECRET_KEY=SecretKey
ALLOWED_HOSTS=127.0.0.1,localhost

### Faire les migrations django
    $ python manage.py migrate

### Préparer les dépendances frontend
    Lire le README.md du dossier frontend

