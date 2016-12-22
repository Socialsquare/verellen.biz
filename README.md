verellen.biz
============

## Introduction

The product catalog and website of http://verellen.biz/

## Deploying changes

ssh into the VM, git pull and restart gunicorn, in a one-liner

`ssh ec2-user@verellen.biz "git -C ~/verellen/ pull && ~/start_gunicorn.sh"`

## Setup

#### Requirements
You need to have these installed on your development machine and on the server
- [python](https://www.python.org)
- [sqlite](https://www.sqlite.org/)
- [less](http://lesscss.org/)
- [virtualenv](https://virtualenv.pypa.io/en/stable/)

#### Command line

`cd` into the project root dir  
`virtualenv env` *initialise python 2.7 virtual environment*  
`. env/bin/activate` *start the virtual environment*  
`pip install -r requirements.txt` *install required python modules*  
`./verellen/manage.py syncdb` *initialise the database and create superuser*  
`./verellen/manage.py migrate` *migrate products, retailers, partner and content*  
`./verellen/manage.py runserver` *start the app*

You can now sign into the Django admin interface by going to `/admin`.

#### Frameworks and components used
- [Django 1.6](https://www.djangoproject.com) *python based web app framework*
- [Bootstrap 3.3](http://getbootstrap.com) *css framework*
- [jQuery 1.11.1](https://jquery.com/) *javascript library*

#### Run command

`cd` into the project root dir and run
`. env/bin/activate && ./manage.py runserver`
