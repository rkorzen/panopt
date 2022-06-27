


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




