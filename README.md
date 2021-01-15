
# Supermarket sales scraper



# Installation & Set up
```
pip install -r requirements.txt
```

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
