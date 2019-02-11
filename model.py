"""Models and database functions for Vibez project."""
from flask_sqlalchemy import SQLAlchemy
from collections import defaultdict

# This is the connection to the PostgreSQL database; we're getting this through the Flask-
# SQLAlchemy helper library. On this, we can find the 'session' object, where we do most 
# of our interactions (like committing, etc.)

db = SQLAlchemy()

#Model definitions

class User(db.Model):
    """User of Vibez website."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fname = db.Column(db.String(50), nullable=False)
    lname = db.Coumn(db.String(50), nullable=False)
    email = db.Column(db.String(60), nullable=False)
    password = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return f"<User user_id={self.user_id} email={self.email}>"


class Playlist(db.Model):
    """Individual user playlists"""

    __tablename__ = "playlists"

    playlist_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False )
    playlist_name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        """Provide helpful representation when printed."""
        
        return f"<Playlist playlist_id={self.playlist_id} playlist_name = {self.playlist_name}>"
    
    user = db.relationship("User", backref="playlist")

    
class Song(db.Model):
    """Songs on Vibez website"""

    __tablename__ = "songs"

    song_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    track_title = db.Column(db.String(200), nullable=False)
    artist = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        """Provide helpful representation when printed"""

        return f"<Song song_id={self.song_id} track ={self.track_title} artist = {self.artist}>"

    playlists = db.relationship("Playlist", secondary="songs_playlists", backref="songs")

class SongPlaylist(db.Model):
    """Middle table between Song and Playlist class"""

    __tablename__ = "songs_playlists"

    song_playlist_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    song_id = db.Column(db.Integer, db.ForeignKey('songs.song_id'), nullable=False)
    playlist_id = db.Column(db.Integer, db.ForeignKey('playlists.playlist_id'), nullable=False)

def connect_to_db(app):
    """Connect the database to our Flask app."""

    #Configure to use our PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)

if __name__ == "__main__":
    #As a convenience, if we run this module interactively, it wil leave
    #you in a state of being able to work with the database directly.

    from server import app

    connect_to_db(app)
    print("Connected to DB.")