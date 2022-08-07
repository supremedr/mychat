from .base import *

DEBUG = True

# Configure Django App for Heroku.
import django_heroku
django_heroku.settings(locals())

