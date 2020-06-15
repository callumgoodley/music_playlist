from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from application.models import Users
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user

class SongForm(FlaskForm):
    title = StringField('title', 
            validators = [
                DataRequired(),
                Length(min=2, max=30)
                ]
            )
    artist = StringField('artist', 
            validators = [
                DataRequired(),
                Length(min=2, max=30)
                ]
            )
    album  = StringField('album',
            validators = [
                DataRequired(),
                Length(min=2, max=30)
                ]
            )
    genre = StringField('genre', 
            validators = [
                DataRequired(),
                Length(min=2, max=30)
                ]
            )
    year = StringField('year', 
            validators = [
                DataRequired(),
                Length(min=4, max=4)
                ]
            )
    submit = SubmitField('add song!')

class RegistrationForm(FlaskForm):
    
    first_name = StringField('First Name',
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ]
    )
    last_name = StringField('Last Name',
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ]
    )
    email = StringField('Email',
        validators = [
            DataRequired(),
            Email()
        ]
    )
    password = PasswordField('Password',
        validators = [
            DataRequired(),
        ]
    )
    confirm_password = PasswordField('Confirm Password',
        validators = [
            DataRequired(),
            EqualTo('password')
        ]
    )
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        user = Users.query.filter_by(email=email.data).first()

        if user:
            raise ValidationError('Email already in use')

class LoginForm(FlaskForm):
    email = StringField('Email',
        validators=[
            DataRequired(),
            Email()
        ]
    )

    password = PasswordField('Password',
        validators=[
            DataRequired()
        ]
    )

    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
    first_name = StringField('First Name',
        validators=[
            DataRequired(),
            Length(min=4, max=30)
        ])
    last_name = StringField('Last Name',
        validators=[
            DataRequired(),
            Length(min=4, max=30)
        ])
    email = StringField('Email',
        validators=[
            DataRequired(),
            Email()
        ])
    submit = SubmitField('Update')

    def validate_email(self,email):
        if email.data != current_user.email:
            user = Users.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Email already in use')

class PlaylistForm(FlaskForm):
    name = StringField('Name',
            validators = [
                DataRequired(),
                Length(min=1, max = 50)
            ])
    submit = SubmitField('Create Playlist')


