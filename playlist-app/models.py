"""models.py"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Playlist(db.Model):
    __tablename__ = 'playlist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255))

    # Define the relationship with the Song model
    songs = db.relationship('Song', secondary='playlist_song', backref='playlists')

class Song(db.Model):
    __tablename__ = 'song'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    artist = db.Column(db.String(100), nullable=False)

class PlaylistSong(db.Model):
    
    __tablename__ = 'playlist_song'

    playlist_id = db.Column(db.Integer, db.ForeignKey('playlist.id'), nullable=False, primary_key=True)
    song_id = db.Column(db.Integer, db.ForeignKey('song.id'), nullable=False, primary_key=True)

    def __init__(self, playlist_id, song_id):
        self.playlist_id = playlist_id
        self.song_id = song_id


# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""
    db.app = app
    db.init_app(app)