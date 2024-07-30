<!-- ABOUT THE PROJECT -->
## About The Project

RIK proovitöö 2024 - Taisi Telve

<!-- GETTING STARTED -->
## Getting Started

For development, you will need Python 3.6 or higher, pip, venv, and PostgeSQL installed in your environment.


# Install the latest version of PostgreSQL.
    $ sudo apt-get update
    $ sudo apt-get install postgresql

Please note for sake of ease, this project is set to work with the default configurations of PostgreSQL on a local installation.


## Installation

    $ git clone https://github.com/brennanbrown/django-project.git
    $ cd django-project

### Virtual Environment (`venv`)

While there are a few ways to achieve a programming environment in Python, we’ll be using the venv module here, which is part of the standard Python 3 library. Install venv by typing:

    $ sudo apt install python3-venv

Creating and entering a new virtual environment:

    $ python3 -m venv env
    $ . env/bin/activate
    $ pip install -r requirements.txt

### Creating the database and data

Assuming You already have created the postgres database and added the db name and user to settings.py

    $ python3 manage.py makemigrations
    $ python3 manage.py migrate
    $ python manage.py loaddata initial_data.json

### Running the project

    $ python3 manage.py runserver

Once the server has started up, you can visit it at [localhost:8000/](localhost:8000/), or [127.0.0.1:8000/](127.0.0.1:8000/).