 Gestionnaire de Vidéothèque

# Description

Le Gestionnaire de Vidéothèque est une application qui permet de gérer une collection de films. Les fonctionnalités incluent l'ajout de films, la recherche de films, le prêt et le retour de films.


# Gestionnaire de Vidéothèque

# Description
Le Gestionnaire de Vidéothèque est une application qui permet de gérer une collection de films. Les fonctionnalités incluent l'ajout de films, la recherche de films, le prêt et le retour de films.

# Structure du Projet

videotheque_manager/

├── videotheque/

│ ├── init.py


│ ├── film.py

│ ├── videotheque.py

├── tests/

│ ├── init.py

│ ├── test_film.py

│ ├── test_videotheque.py

│ ├── test_integration.py

├── requirements.txt

└── README.md

# création et activation de l'environnement virtuel
python -m venv venv
venv/Scripts/activate

# installation des dependances : requirement.txt

pip install pipreqs
pipreqs ./

# execution tes tests avec unittest
# python -m unittest discover -s tests
pour executer tous les test

python -m unittest test.test_film
pour executer le fichier test_film