from sql alchemy import *
from sqlalchemy.engine.url import URL

import settings

def db_connect():
	"""
	Given: DB connection using settings from settings.py
	Returns: sqlalchemy engine instance
	"""
	return create_engine(URL(**settings.DATABASE))