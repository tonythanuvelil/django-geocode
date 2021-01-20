# django-geocode
* clone this repository and run the following commands
```
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```

### apis
* login: api/token/ - method **GET**
* signup: api/users/ - method **POST**
* create orders: api/orders/ - method **POST**, params - ```{"house_name": "foo", "latitude": 23.999, "longitude": 19.0038}```
* list order: api/orders/ - method **GET**

> Note: Instead of google geo code api, I have used opensource MapQuestApi -  https://developer.mapquest.com/
> Please try to use lat and long in North American region for best results
