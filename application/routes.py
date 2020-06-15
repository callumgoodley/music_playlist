from flask import render_template, redirect, url_for, request
from application import app, db, bcrypt
from application.models import Song, Playlist, Users
from application.forms import SongForm, PlaylistForm, RegistrationForm, LoginForm, UpdateAccountForm
from flask_login import login_user, current_user, logout_user, login_required


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
                album = form.album.data
                )
        db.session.add(postData)
        db.session.commit()

        return redirect(url_for('playlist'))
    
    return render_template('addsong.html', title='addsong', form = form)

@app.route('/playlist', methods = ['GET', 'POST'])
def playlist():
    
    form = PlaylistForm()
    email = current_user.email
    userData = Users.query.filter(email==email).first()

    if form.validate_on_submit():
        postData = Playlist(
                name = form.name.data,
                user_id = userData.id
                )
        db.session.add(postData)
        db.session.commit()

    return render_template('playlist.html', title = 'Playlist', form = form)

@app.route('/playlist/<int:number>', methods = ['GET', 'POST'])
def individual_playlist(playlist_id):
    playlistData = Playlist.query.filter(id=playlist_id).all()
    return render_template('individual_playlist.html', title = 'Indiviual Playlist', playlist=playlistData)

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
