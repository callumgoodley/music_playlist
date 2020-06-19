#! /bin/bash
. /home/callumgoodley/music_playlist/venv/bin/activate

/home/callumgoodley/music_playlist/venv/bin/gunicorn --chdir=/home/callumgoodley/music_playlist --workers=4 --bind=0.0.0.0:5000 app:app
#python3 /home/callumgoodley/music_playlist/app.py
