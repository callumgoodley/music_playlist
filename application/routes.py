from flask import render_template, redirect, url_for, request
from application import app, db, bcrypt
from application.models import songs_playlist, Song, Playlist, Users
from application.forms import SongForm, PlaylistForm, UpdatePlaylistForm, RegistrationForm, LoginForm, UpdateAccountForm
from flask_login import login_user, current_user, logout_user, login_required


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title = 'Home')

@app.route('/playlist', methods = ['GET', 'POST'])
def playlist():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    
    playlists = Playlist.query.filter_by(user_id = current_user.id)
    form = PlaylistForm()
    id = current_user.id

    if form.validate_on_submit():
        postData = Playlist(
                name = form.name.data,
                user_id = id
                )
        db.session.add(postData)
        db.session.commit()

    return render_template('playlist.html', title = 'Playlist', form = form, playlists=playlists)

@app.route('/playlist/<number>', methods = ['GET', 'POST'])
@login_required
def individual_playlist(number):
    form = SongForm()
    playlist = Playlist.query.filter_by(id=number).first()
    song_exists = Song.query.filter_by(title=form.title.data).filter_by(artist=form.artist.data).filter_by(album=form.album.data).first() 
    
    if not current_user.is_authenticated:
        return redirect(url_for('login'))

    if form.validate_on_submit():
        song_to_add = Song(
                title = form.title.data,
                artist = form.artist.data,
                album = form.album.data
                )
        if song_exists:
            song_exists.songs_playlist.append(playlist)
        else:
            song_to_add.songs_playlist.append(playlist)
            db.session.add(song_to_add)

        db.session.commit()

    return render_template('individual_playlist.html', title = 'Indiviual Playlist', form=form, playlist=playlist)

@app.route('/change_playlist_name/<number>', methods = ['GET', 'POST'])
@login_required
def change_playlist_name(number):

    form = UpdatePlaylistForm()

    playlist = Playlist.query.filter_by(id=number).first()

    if not current_user.is_authenticated:
        return redirect(url_for('login'))

    if form.validate_on_submit():
        playlist.name = form.name.data
        db.session.commit()
        return redirect(url_for("individual_playlist", number = number))
    elif request.method == 'GET':
        form.name.data = playlist.name

    return render_template('change_playlist_name.html', title = 'Change Playlist Name', form=form, playlist=playlist)



@app.route('/delete_playlist/<number>', methods = ['GET', 'POST'])
@login_required
def delete_playlist(number):

    if not current_user.is_authenticated:
        return redirect(url_for('login'))

    playlist = Playlist.query.filter_by(id=number).first()

    db.session.delete(playlist)
    db.session.commit()

    return redirect(url_for('playlist')) 

@app.route('/delete_song/<number>', methods = ['GET', 'POST'])
@login_required
def delete_song(number):
    if not current_user.is_authenticated:
        return redirect(url_for('login'))

    
    song = Song.query.filter_by(id=number).first() 

    db.session.delete(song)
    db.session.commit()
         
    return redirect(url_for('playlist'))

@app.route('/register', methods = ['GET', 'POST'])
def register():

    form = RegistrationForm()
    if current_user.is_authenticated:
        return redirect(url_for('playlist'))

    if form.validate_on_submit():
        hash_pw = bcrypt.generate_password_hash(form.password.data)

        user = Users(first_name=form.first_name.data, last_name=form.last_name.data, email = form.email.data, password = hash_pw)

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('login'))

    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if current_user.is_authenticated:
        return redirect(url_for('playlist'))

    if form.validate_on_submit():
        user=Users.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('playlist'))
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        current_user.email = form.email.data
        db.session.commit()
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
        form.email.data = current_user.email
    return render_template('account.html', title='Account', form=form)

@app.route("/account/delete", methods=["GET", "POST"])
@login_required
def account_delete():

    if not current_user.is_authenticated:
        return redirect(url_for('login'))

    user = current_user.id
    user_posts = Posts.query.filter_by(user_id=user).all()
    for post in user_posts:
        db.session.delete(post)
    account = Users.query.filter_by(id=user).first()
    logout_user()
    db.session.delete(account)
    db.session.commit()
    return redirect(url_for('register'))

