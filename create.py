from application import db
from application.models import Playlist, Users, Song, songs

db.drop_all()
db.create_all()
