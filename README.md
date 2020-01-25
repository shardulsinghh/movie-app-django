Django React Application Documentation

# Steps to run locally:
* Clone Repository
* Install dependancies for Django
* Set up MySQLShell in background, using terminal or XAMPP
* Specify Database PORT and Params in settings.py file
* Run:
`python dbload.py` \
to populate Database (Only required to do once)
* Run `python manage.py makemigrations`, if there are migrations to be made run `python manage.py migrate`
* Run "python manage.py runserver" (App runs on localhost:8000, by default)
* Create superuser using `python manage.py createsuperuser`

## Exposed APIs:

# This build API exposes the following routes for CRUD operations on a MySQL database:
 - /api - GET, POST, GET all objects and POST new objects on this path
 - /api/:id - GET, POST, PUT, DELETE,  Primary Key ID parameter passed into query string and allows us to get unique object from Database if exists
 - /admin - CRUD Operations on existing table values and Users, can be used to modify or update the Database
 
 Hence the API can perform GET, POST, PUT, DELETE, i.e., all CRUD features using Django Rest Framework.
 
 The Databse Tables have been set up as a ManyToMany Relationship between Movies and Genres.
 
 Futher Improvements we can make:
 * Authentication Using Token
 * Django Sessions
