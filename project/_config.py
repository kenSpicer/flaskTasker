import os

# grab the folder where this script lives
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flaskTaskerII.db'
USERNAME = 'admin'
PASSWORD = 'admin'
WTF_CSRF_ENABLED = True
SECRET_KEY = '^.D\n\xbc\xd1\xd7P\x81*oY\x0cF\x00\x9flF\x14\xb6!\x0b;\xdc'

# define the full path for the database
DATABASE_PATH = os.path.join(basedir, DATABASE)
