# cookiecutter-django
création d'un site django avec Vite et Bootstrap. Possibilité d'ajouter wagtail.

### Installer cookiecutter
    $ pipenv install cookiecutter

### Lancer cookiecutter
    $ cookiecutter gh:AnaisG14/cookiecutter-django-vite
    Des questions seront posées et votre projet sera créé.

### Préparer l'environnement virtuel
    $ mkdir .venv
    $ pipenv install
    $ pipenv shell

### Faire les migrations django
    $ python manage.py makemigrations
    $ python manage.py migrate

### Préparer les dépendances frontend
    Lire le README.md du dossier frontend

