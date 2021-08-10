CookieFlutter Django 🍪✂️ 
===========================

.. image:: https://img.shields.io/github/workflow/status/pydanny/cookiecutter-django/CI/master
    :target: https://github.com/pydanny/cookiecutter-django/actions?query=workflow%3ACI
    :alt: Build Status

.. image:: https://www.codetriage.com/pydanny/cookiecutter-django/badges/users.svg
    :target: https://www.codetriage.com/pydanny/cookiecutter-django
    :alt: Code Helpers Badge

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/ambv/black
    :alt: Code style: black


Overview
---------
CookieFlutter Django is a spin off of Cookiecutter Django. It is customized for my workflow and includes features such as gis tools, web scraping tools, data science tools, celery voulumes, and a flutter frontend.


Usage (Backend)
---------------

First, get Cookiecutter. Trust me, it's awesome::

    $ pip install "cookiecutter>=1.7.0"

Now run it against this repo::

    $ cookiecutter https://github.com/julianwagle/cookieflutter-django

You'll be prompted for some values. Provide them, then a project will be created for you.

Finally, move to the root directory and enter the following::

    $ docker-compose -f local.yml up
    
By default, this app comes with an authentication interface running as both a standard JQuery interface and as a DRF interface, soon to be migrated to a SPA.

For a list of DRF endpoints you can view the docs here: https://dj-rest-auth.readthedocs.io/en/latest/api_endpoints.html
    
There is one caveat to this dual interface: it is uncertain which user authentication email verification url should be standard in the emails sent to user. 

I currently have the default set to the DRF authentication method which will soon be implemented into an SPA. 

However, keep in mind that if you want to use the standard templated interface, you shouuld replace the '/dj-rest-auth/account-confirm-email/' in the emails sent with '/email-verification'.

If you want to change this setting permanently simply navigate to {{cookiecutter.project_slug}}/users/adapters and swap the commented line with the line above it


Usage (Frontend)
----------------

If you want to fire up the Flutter frontend, you'll have to first, have isntalled all the necessary packages and configured your local machine. 

For more on that you can follow these docs: https://flutter.dev/docs/get-started/install

Once you've got your machine set up you can run the following in the frontend dir::

        $ flutter channel master
        $ flutter upgrade
        $ flutter pub get
        $ flutter run


Troubleshooting
---------------

IF you opt in to both Celery AND PostGIS, the first time you start this up, celerybeat may not properly insert a colomn into the database. However, the second time it will all work fine.


Todo List
---------

I've still got to finish integrating the front-end with the authentication on the back end. 

Finally, I'll adjust the production settings accordingly to allow for seamless push to production.

