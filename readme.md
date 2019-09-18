# Reimnet Blog
A Blog for simple CRUD operations.


## GETTING STARTED
## Requirement
 open "requirements.txt" to know packages installed and dependencies used

### Steps to recreating superuser
1. Delete all files and folders within the migration folder, except the `__init__.py` file.
2. Open terminal and run the following commands:
    - `python manage.py makemigrations posts`
    - `python manage.py posts`
    - `python manage.py migrate`
    - `python manage.py createsuperuser`

##Data Seeding
used the fixtures method to provide models with initial data, Json precisely.
-To import data into models from fixtures, run the command
    * python manage.py loaddata <fixture-name>
-To export data from models into fixtures, run the command
    * python manage.py dumpdata app-name > app-name/fixtures/<fixture-name>
