# events

## Installation
If pipenv and python 3.6 installed
```
$ git clone <repo url>
$ cd events
$ pipenv install
$ cd csea_events
$ pipenv shell
$ python manage.py runserver
```

Else
```
$ git clone <repo url>
$ cd events
$ pip install django
$ cd csea_events
$ python manage.py runserver
```
## Using in local network
- First clone this and migrate
- Create users
- In settings.py add the local IPv4 address of the pc in the allowed hosts
- run on local network as:
```
python manage.py runserver 0.0.0.0:8000
```
- Access on the network
