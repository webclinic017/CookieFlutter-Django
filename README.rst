Octopod Spork 🐙
===================

Please sign the petition_ for a spork emoji 

.. _petition: https://www.change.org/p/apple-we-as-a-union-ad-people-need-a-spork-emoji-now


.. image:: https://img.shields.io/github/workflow/status/pydanny/cookiecutter-django/CI/master
    :target: https://github.com/pydanny/cookiecutter-django/actions?query=workflow%3ACI
    :alt: Build Status

.. image:: https://readthedocs.org/projects/cookiecutter-django/badge/?version=latest
    :target: https://cookiecutter-django.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://img.shields.io/badge/cookiecutter-Join%20on%20Slack-green?style=flat&logo=slack
    :target: https://join.slack.com/t/cookie-cutter/shared_invite/enQtNzI0Mzg5NjE5Nzk5LTRlYWI2YTZhYmQ4YmU1Y2Q2NmE1ZjkwOGM0NDQyNTIwY2M4ZTgyNDVkNjMxMDdhZGI5ZGE5YmJjM2M3ODJlY2U

.. image:: https://www.codetriage.com/pydanny/cookiecutter-django/badges/users.svg
    :target: https://www.codetriage.com/pydanny/cookiecutter-django
    :alt: Code Helpers Badge

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/ambv/black
    :alt: Code style: black

Powered by Cookiecutter_, Octopod Spork is a framework for jumpstarting
production-ready Django projects quickly.


Overview
---------
Octopod Spork is a spin off of Cookiecutter Django. It is customized for my workflow and includes features such as gis tools, web scraping tools, data science tools, celery voulumes, and a bare bones react app.

Usage
------

First, get Cookiecutter. Trust me, it's awesome::

    $ pip install "cookiecutter>=1.7.0"

Now run it against this repo::

    $ cookiecutter https://github.com/julianwagle/octopod-spork

You'll be prompted for some values. Provide them, then a project will be created for you.

Finally, move to the root directory and enter the following:

    $ docker-compose -f local.yml up
    
You should now be able to navigate to either port 8000/api for a DRF auth interface or port 3000 for a React based front-end. Enjoy!

