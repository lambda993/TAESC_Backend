# TAESC_Backend
## Description
This API aims to provide data for the Total Annihilation Escalation mod so that Units, Weapons, Sounds, Animations, ect that are present in the game are viewable in a detailed manner.
## Installation
Clone the repo using git, make sure you have python installed (version used here is 3.11.0).
Create a virtual environment using <sub>python -m venv .venv</sub>.
Install the required libraries using <sub>pip install -r requirements.txt</sub>.
Change settings.example.py so that is settings.py, configure database settings and secret key.
Run django migrations with the <sub>pyhon manage.py migrate</sub>.
Create superuser with <sub>python manage.py createsuperuser</sub>.
Run the development server with <sub>python manage.py runserver</sub>.
