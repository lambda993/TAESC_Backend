# TAESC_Backend
## Description
This API aims to provide data for the Total Annihilation Escalation mod so that Units, Weapons, Sounds, Animations, ect that are present in the game are viewable in a detailed manner.
## Installation
Clone the repo using git, make sure you have python installed (version used here is 3.11.0).
Create a virtual environment using **python -m venv .venv**.
Install the required libraries using **pip install -r requirements.txt**.
Change settings.example.py so that is settings.py, configure database settings and secret key.
Run django migrations with the **pyhon manage.py migrate**.
Create superuser with **python manage.py createsuperuser**.
Run the development server with **python manage.py runserver**.
