"Vibez"
from pprint import pformat
import os

import requests

from jinja2 import StrictUndefined

from flask import Flask, render_template, request, flash, redirect, session
from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db, User, Song, Playlist

import spotify

app = Flask(__name__)

#This secret key is required to use FLask sesssions and the debug toolbar
app.secret_key = "youcandothisjen"

#The line of code below will raise an error when you use an undefined variable in Jinja2 (
# instead of failing)
app.jinja_env.undefined = StrictUndefined



@app.route("/")
def index():
    """Homepage"""

    return render_template("homepage.html")

@app.route('/register')
def register_form():
    """Show form for user signup"""

    return render_template("register_form.html")

@app.route('/register', methods=['POST'])
def register_process():
    """Process registration"""

    #Get form variables
    fname = request.form["fname"]
    lname = request.form["lname"]
    email = request.form["email"]
    password = request.form["password"]
    
    new_user = User(fname=fname, lname=lname, email=email, password=password)

    db.session.add(new_user)
    db.session.commit()

    flash(f"User {fname} has been added.")
    return redirect(f"/users/{new_user.user_id}")

@app.route('/login')
def login_form():
    """Show login form."""

    return render_template("login_form.html")

@app.route('/login', methods=['POST'])
def login_process():
    """Process login"""

    #Get form variables
    email = request.form["email"]
    password = request.form["password"]

    user = User.query.filter_by(email=email).first()

    if not user:
        flash("No such user")
        return redirect("/login")
    
    if user.password != password:
        flash("Incorrect password")
        return redirect("/login")
    
    session["user_id"] = user.user_id

    flash("Logged in")
    return redirect(f"/users/{user.user_id}")

@app.route('/logout')
def logout():
        """Log out."""

        del session["user_id"]
        flash("Logged Out.")
        return redirect("/")
    
@app.route("/users")  #A route to check out other user's playlists
def user_list():
        """Show list of users"""

        users = User.query.all()
        return render_template("user_list.html", users=users)
    
@app.route("/users")
def user_playlists(user_id):
    """Show info about user's playlists."""

@app.route("/create")
def create_playlist():
    """Create playlist by selecting genre, danceability, and speechiness"""


    return render_template("create_playlist.html")

# @app.route("/create", methods=['POST'])
# def create_playlist():
#     """Save playlist to user personal profile"""

# #     genre = request.args.get("genre")
# #     min_danceability = request.args.get("minDanceability")
# #     max_danceability = request.args.get("maxDanceability")


# #     #save as session so you can later see page of newly generated playlist
# #     session["genre"] = genre
# #     session["minimum_danceability"] = min_danceability
# #     session["maximum_danceability"] = max_danceability


#     #permanently save the generated playlist into database


@app.route("/generateplaylist")
def generate_playlist():
    #get information input into html page
    
#     spotify_info = spotify.base_playlist(spotify.generate_token(), session["genre"], session["minimum_danceability"], 
#     session["maximum_danceability"])

    spotify_info = spotify.base_playlist(spotify.generate_token(), 'hip-hop', 0.5, 0.8)


    return render_template("generate_playlist.html", spotify_info = spotify_info)

    #generate playlist based on these search queries
    


@app.route("/playlists")
def playlists():
    """Show list of playlists"""

    playlist = Playlist.query.order_by('title').all()
    return render_template("playlist.html", playlist=playlist)





if __name__ == "__main__":
# We have to set debug=True here, since it has to be True at the point
# that we invoke the DebugToolbarExtension

#Do not debug for demo
        app.debug = True

        connect_to_db(app)

#Use the DebugToolbar
        DebugToolbarExtension(app)

        app.run(host="0.0.0.0")



