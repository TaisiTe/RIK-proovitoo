<!-- ABOUT THE PROJECT -->
## About The Project

RIK proovitöö 2024 - Taisi Telve
(Töö on arendatud Windows platvormil, vabandan! Readme-s toodud käsud on mõeldud siiski Ubuntule.)

<!-- GETTING STARTED -->
## Getting Started

For development, you will need Python 3.6 or higher, pip, venv, and PostgeSQL installed in your environment.

# Install the latest version of Python3 and PostgreSQL.
    $ sudo apt-get update
    $ sudo apt-get install python3 postgresql

Please note for sake of ease, this project is set to work with the default configurations of PostgreSQL on a local installation.

## Installation

    $ git clone https://github.com/TaisiTe/RIK-proovitoo.git
    $ cd RIK-proovitoo

### Virtual Environment (`venv`)

Creating and entering a new virtual environment:

    $ python3 -m venv venv
    $ . venv/bin/activate
    $ pip install -r requirements.txt

### Creating the database and data

Assuming the postgres database has been created and the db name and user have been added to settings.py

    $ python3 manage.py makemigrations
    $ python3 manage.py migrate

For creating initial data (5 companies and 8 shareholders) run:

    $ python3 manage.py loaddata initial_data.json

### Running the project

    $ python3 manage.py runserver

Once the server has started up, you can visit it at [localhost:8000/companies](localhost:8000/companies), or [127.0.0.1:8000/companies](127.0.0.1:8000/companies).

### Django admin

For using Django admin please first set username and password using:

    $ python3 manage.py createsuperuser

Then access the admin at localhost:8000/admin

Happy exploring!