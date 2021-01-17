
# Supermarket sales scraper

# Requirements
Before running this project you will need
- MongoDB Database
- Chromedriver installed

# Installation & Set up
I suggest first setting up a virtualenv `python3 -m venv venv` and activating it `venv/Scripts/actiavte.bat`.
```
pip install -r requirements.txt
```
Install all requirements with pip
```
cp .env.example .env
```
copy .env.examply to .env and set all the variables needed


# Migrations
```
python manage.py makemigrations
```
```
python manage.py migrate
```

# Run project
```
python manage.py runserver
```


# Deploy project
### Note
This project was deployed with Heroku since it was free, however if you have the option I would suggest using Docker for such a project. 

### Heroku deployment
Here is the guideline for deploying this app on Heroku. It's needed to have a account for this.

```
heroku login
``` 
Login to your heroku account

```
heroku create <projectname>
heroku git:remote -a <projectname>
```
create and set the git remote to the project

```
heroku local
```
Test if the app is running with local settings

```
heroku config:set KEY=VALUE
```
Set all the .env variables for heroku

```
git push heroku HEAD:master
```


# Project structure
### scrapers
In this directory the scrapers can be found, you can run them individually by calling main() in the respective file and running `python <filname>.py`

### api
In the api folder all the configuration can be found for the rest API. This is using the Django rest framework.

### SalesCompare
In the SalesCompare the general settings can be found. The most important file of this folder is the `settings.py`. 
