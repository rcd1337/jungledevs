## Stack:

Python 3.9.7
Django 3.1.5
djangorestframework 3.12.2
psycopg2 2.8.6
gunicorn

## Setup:

inside `/jungledevs`:

- py -m venv env
- source env/Scripts/activate ('bin' instad of 'Scripts' if using Linux)
- docker-compose up
- docker-compose exec web python manage.py migrate
- docker-compose exec web python manage.py runserver

## Routes

Login and registration:

`/api/login/`

`/api/sign-up/`

Administrator restricted APIs (CRUD): 

`/api/admin/authors/`

`/api/admin/articles/`

`/api/admin/authors/:id/`

`/api/admin/articles/:id/`

List articles:

`/api/articles/` (all articles)

`/api/articles/?category=:slug` (shows only given category)

Article details:

`/api/articles/:id/`

## Notes

- Issue: "author" is lacking the nested descriptions of "id" "name" and "picture".