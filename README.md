# AmazonClone
Clone the repository 
``` 
git clone https://github.com/divyekalra1/AmazonClone.git 
```
Setup and activate a python3 virtual environment using venv
```
python3 -m venv env
source env/bin/activate
```
Install dependencies
```
pip3 install -r requirements.txt
```
Migrate database
```
cd django_prj
python manage.py migrate
```
Run Server
```
python manage.py runserver
```
