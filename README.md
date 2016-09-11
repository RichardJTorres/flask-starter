Flask Starter
======
A simple boilerplate flask app. This app is intended to be flexible enough to kickstart any type of web application. 

It includes the following boilerplate features:
* A .gitignore file
* A basic layout template with bootstrap and jquery loaded from public CDN
* A set of `Config` objects 
* A `Procfile` and `runtime.txt` for deploying to heroku
* A basic test setup built with `unittest`. This can be replaced with the framework of your choice.

To remain flexible, this project intentionally does not include: 
* An ORM. 
* An asyncronous task/job queue
* A frontend framework

Requirements
------
* [virtualenv](http://www.virtualenv.org/en/latest/)

Installation
------
```bash
$ git clone git@github.com:RichardJTorres/flask-starter.git
$ cd flask-starter
$ pyvenv-3.5 env
$ source env/bin/activate
(env)$ pip install -r requirements.txt
(env)$ export APP_SETTINGS="config.DevelopmentConfig"
(env)$ python app.py
```

Test
------
```bash
$ source env/bin/activate
(env)$ python tests.py
