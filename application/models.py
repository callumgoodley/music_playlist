from application import db, login_manager
from flask_login import UserMixin
from datetime import datetime



class Users(db.Model, UserMixin):
    
    @login_manager.user_loader
    def load_user(id):
        return Users.query.get(int(id))

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(500), nullable=False)
    playlist_id = db.relationship('Playlists', backref='added by', lazy=True)

    def __repr__(self):
        return ''.join([
            'User ID: ', str(self.id), '\r\n',
            'Email: ', self.email, '\r\n',
            'Name: ', self.first_name, ' ', self.last_name
        ])

songs = db.Table('songs',
        db.Column('song_id', db.Integer, db.ForeignKey('song.id'), primary_key= True),
        db.Column('playlist_id', db.Integer, db.ForeignKey('playlist.id'), primary_key=True))

class Playlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    songs = db.relationship('Playlist', secondary=songs, lazy='subquery',
            backref=db.backref('playlists', lazy=True))

class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    artist = db.Column(db.String(100), nullable=False)
    album = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    year = db.Column(db.String(4), nullable=False)

