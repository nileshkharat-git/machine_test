# machine_test

## How to run machine?

```sh
$ git clone https://github.com/nileshkharat-git/machine_test.git
$ cd machine_test
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd project
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/clients/`.

## How to run DB design?

Following instuctions are for postgresql database

Step-1:
```sh
(env)$ sudo su postgres
(env)$ [sudo] password for "username":
```

Step-2:
After login into postgres create  'machine_test' database

```sh
postgres@user:/home/user$ psql
postgres=# create database machine_test;
CREATE DATABASE
```

Step-3:
Go to project directory path

```sh
(env)$ python manage.py makemigrations
# create migrations
(env)$ python manage.py migrate
# Apply migrations
```