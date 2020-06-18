from application import db
from application.models import Playlist, Song, Users, songs_playlist

db.drop_all()
db.create_all()
