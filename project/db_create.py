# project/db_create.py

from views import db
from models import Task
from datetime import date

# crete the database and the db table
db.create_all()

# insert data
db.session.add(Task('Finish this tutorial', date(2017, 3, 24), 10, 1))
db.session.add(Task('Finish Real Python', date(2017, 6, 24), 10, 1))

# commit the changes
db.session.commit()

