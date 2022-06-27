


# Tworzenie projektu

## Utworz katalog dla projektu

mkdir nazwa_projektu

## Przejdz do katalogu

cd nazwa_projektu

## utworz wirtualne srodowisko

python -m venv venv --prompt nazwa

## aktywuj wirtualne srodowisko

linux:
source venv/bin/activate

windows
venv\Scripts\activate

## instalacja django

pip install django

## utworzenie requirements.txt

pip freeze > requirements.txt


## utworzenie projektu

np. polecenie:
django-admin startproject nazwa

utworzy

nazwa
    nazwa
        settings.py
        ...
    manage.py


a polecenie 

django-admin startproject nazwa .

nazwa
    settings.py
    ...
manage.py


## uruchomienie projektu (developerskie)

python manage.py runserver

po tym wchodzimy na adres 

127.0.0.1:8000/

## Commit

git add .
git commit -m "message"

git push origin master

## heroku

### zaloguj sie do heroku

heroku login

### Utworzenie projektu heroku

heroku create

heroku create panopt-yana

### utwórz Procfile

web: python manage.py runserver 0.0.0.0:$PORT

### zainstaluj django-heroku

https://github.com/heroku/django-heroku

dodaj do requirements django-heroku

pip install -r requirements.txt

### konfiguracja django-heroku

Dodanie w settings.py na koncu kodu:

import django_heroku
django_heroku.settings(locals())

### Utworzymy plik .env

w nim tworzymy SECRET_KEY=jakis losowy ciag znakow

### ustawiamy zmienna srodowiskowa na heroku

heroku config:set SECRET_KEY=ciagznakow