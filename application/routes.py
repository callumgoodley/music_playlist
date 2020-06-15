from flask import render_template, redirect, url_for
from application import app, db
from application.models import Song, Playlist
from application.forms import SongForm, PlaylistForm

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title = 'Home')

@app.route('/addsong', methods = ['GET', 'POST'])
def addsong():
    form = SongForm()
    if form.validate_on_submit():
        postData = Song(
                title = form.title.data,
                artist = form.artist.data,
                album = form.album.data,
                genre = form.genre.data,
                year = form.genre.data
                )
        db.session.add(postData)
        db.session.commit()

        return redirect(url_for('playlist'))
    
    return render_template('addsong.html', title='addsong', form = form)

@app.route('/playlist', methods = ['GET', 'POST'])
def playlist():
    form = PlaylistForm()
    if form.validate_on_submit():
        postData = Playlist(
                name = form.name.data
                )
        db.session.add(postData)
        db.session.commit()

    return render_template('playlist.html', title = 'Playlist', form = form)
