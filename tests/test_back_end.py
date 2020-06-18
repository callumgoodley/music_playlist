import unittest

from flask import url_for
from flask_testing import TestCase

from application import app, db, bcrypt
from application.models import Users, Playlist, Song
from os import getenv

class TestBase(TestCase):

    def create_app(self):

        # pass in configurations for test database
        config_name = 'testing'
        app.config.update(SQLALCHEMY_DATABASE_URI=getenv('TEST_DB_URI'),
                SECRET_KEY=getenv('MY_SECRET_KEY'),
                WTF_CSRF_ENABLED=False,
                DEBUG=True
                )
        return app

    def setUp(self):

        db.session.commit()
        db.drop_all()
        db.create_all()

        hashed_pw = bcrypt.generate_password_hash('johnsmith')
        user_one = Users(first_name="john", last_name="smith", email="johnsmith@gmail.com", password=hashed_pw)

        hashed_pw_2 = bcrypt.generate_password_hash('callumgoodley')
        user_two = Users(first_name="callum", last_name="goodley", email="callumgoodley@gmail.com", password=hashed_pw_2)


        db.session.add(user_one)
        db.session.add(user_two)
        db.session.commit()

    def tearDown(self):

        db.session.remove()
        db.drop_all()

class TestViews(TestBase):
    def test_homepage_view(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
    
    def test_playlistpage_view(self):
        res1 = self.client.post(
                    '/login',
                    data=dict(
                        email="callumgoodley@gmail.com",
                        password="callumgoodley"
                        ),
                    follow_redirects=True
                    )
        self.assertEqual(res1.status_code, 200)
        
        res2 = self.client.get(url_for('playlist'))
        
        self.assertEqual(res2.status_code, 200)
    
    def test_individualplaylistpage_view(self):
        res1 = self.client.post(
                    '/login',
                    data=dict(
                        email="callumgoodley@gmail.com",
                        password="callumgoodley"
                        ),
                    follow_redirects=True
                    )
        self.assertEqual(res1.status_code, 200)

        res2 = self.client.get(url_for('individual_playlist', number = 1))
        
        self.assertEqual(res2.status_code, 200) 
