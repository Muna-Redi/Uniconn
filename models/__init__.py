#!/usr/bin/python3

from flask import Flask
from models.engine.db import DBStore


app = Flask(__name__)

storage = DBStore()

storage.reload()

import views
