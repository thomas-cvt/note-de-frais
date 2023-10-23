# Note de Frais

**Application Web de gestion de dépenses et de remboursements.**

L'utilisateur peut saisir ses opérations depuis l'interface d'administration.
Elles sont affichées sur la page principale. La seconde personne en charge du remboursement de la note de frais peut visualiser les détails, et effectuer un remboursement. Toutes les dépenses sont alors marquées comme remboursées et ne sont plus dues.

## Fonctions

- Ajouter des dépenses / revenus
- Classement par catégorie
- Calcul du total dû
- Effectuer un remboursement
- Affichage agréable et détaillé

## Installation

Clôner le dépôt dans un dossier :

```sh
git clone https://github.com/thomas-cvt/note-de-frais.git
```

Créer un environnement virtuel Python 3.10 au minimum :

```sh
python -m venv env
```

Installer les modules requis :

```sh
pip install -r requirements.txt
```

Ajouter les variables d'environnements nécessaires :

```sh
cd ./env
touch .env
```
Puis ajouter l'extrait ci-dessous en complétant les variables :

```sh
SECRET_KEY=
DB_HOST=
DB_NAME=
DB_PORT=3306
DB_USER=
DB_PASSWORD=
SERVERNAMES=*
```

Créer la base de données :

```sh
cd ..
python manage.py makemigrations
python manage.py migrate
```

Lancer le serveur de développement :

```sh
python manage.py runserver
```

- Vous pouvez accéder à l'application à cet URL : ```http://127.0.0.1:8000```

- Et à l'interface d'administration à cet URL : ```http://127.0.0.1:8000/admin```