import os
import environ
from os.path import dirname

BASE_DIR = dirname(dirname(os.path.abspath(__file__)))

env = environ.Env()
environ.Env.read_env(BASE_DIR+"/.env")

DJANGO_ENV = env("DJANGO_ENV")

from .conf.production.settings import *
