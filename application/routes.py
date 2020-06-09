from flask import render_template, redirect, url_for
from application import app, db
from application.models import Songs
from application.forms import SongForm

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title = 'Home')

@app.route('/addsong')
def addsong():
    form = SongForm()
    if form.validate_on_submit():
        postData = Songs(
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

@app.route('/playlist')
def playlist():
    return render_template('playlist.html', title = 'Playlist')
