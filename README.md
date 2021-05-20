# Official Website of CDCRC, IIT Ropar 

## About

The following repository contains the source code of the official website of Career Development and Corporate Relations Center, IIT Ropar.

## Development setup
Before proceeding further, ensure that you have python3 installed on your computer! Incase you don't you can download python3 from [here](https://www.python.org/downloads/).

1. Clone the repo and change the directory.
2. Now install all dependencies.
```bash
pip install -r requirements.txt
```
3. Change the directory into `src/`.
```bash
cd src/
```
4. Now, run the following command to make migrations corresponding to the models in the project.
```bash
python manage.py makemigrations
```
5. Migrate the changes into the database.
```bash
python manage.py migrate
```
6. Now, run the development server with the following command.
```bash
python manage.py runserver
```
7. Congrats! Now you are all set to contribute! 🎉🎉

