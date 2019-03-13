# Vibez

Vibez is a web application that utilizes Spotify's API to generate playlists based on a user's choice of genre and a minimum and maximum range of danceability levels (0 - 1).

## Table of Contents
* [Overview](#overview)<br/>
* [Tech Stack](#techstack)<br/>
* [Setup/Installation](#installation)<br/>
* [Demo](#demo)<br/>
* [Future Features](#features)

<a name="overview"/></a>
## Overview
Once a user logs into their account and generates a new playlist, Vibez gathers and stores the playlist's history in a PostgreSQL database along with information for three audio features: music genre, minimum danceability, and maximum danceability. Playlists are generated after requesting pertinent info from Spotify's API. Once the backend receives Spotify's JSON, Vibez integrates the JSON into the frontend using the Amplitude.js library to showcase its lists of songs and its accompanying shuffle, skip, adjustable volume, scroll, and other convenient functions. In order to display a page of stored playlists, Vibez assimilates interactive, complex visuals rendered by code that is extracted and heavily refactored from the D3.js library. Both Amplitude.js and D3.js require heavy use of jQuery, Javascript, CSS, and HTML. Accessing a stored playlist works similarly to generating a new playlist, except a different Spotify API endpoint is requested.

<a name="techstack"/></a>
## Tech Stack
**Frontend:** Javascript (AJAX, JSON), JQuery, Jinja, HTML, CSS, Bootstrap</br>
**Backend:** Python, Flask, SQLAlchemy, PostgreSQL<br/>
**Libraries:** D3.js, Amplitude.js<br/>
**APIs:** Spotify<br/>

<a name="installation"/></a>
## Setup/Installation
Get Client ID and Client Secret from [Spotify](https://developer.spotify.com/) and save them to a file `config.py`:
```
client_id=YOUR_KEY
client_secret=YOUR_KEY
```
On local machine, go to directory where you want to work and clone Vibez repository:
```
$ git clone https://github.com/surferJen/vibez.git
```
Create a virtual environment in the directory:
```
$ virtualenv env
```
Activate virtual environment:
```
$ source env/bin/activate
```
Install dependencies:
```
$ pip install -r requirements.txt
```
Create database:
```
$ createdb playlists
```
Create your database tables:
```
$ python3 model.py
```
Create .gitignore file:
```
$ touch .gitignore
```
Access .gitignore file in terminal to ignore config.py file:
```
$ nano .gitignore
```
Store config.py file in .gitignore file:
```
config.py
```
Run the app:
```
$ python3 server.py
```
Open localhost:5000 on browser.

<a name="demo"/></a>
## Demo
**Register a Vibez account:**
<br/><br/>
![Registration](/static/img/README/register.png)
<br/>

**Log in to Vibez account:**
<br/><br/>
![Login](/static/img/README/login.png)
<br/>

**View collection of playlists and select unique playlist to play on following page:**
<br/><br/>
![View Playlists and Select](/static/img/README/select_playlists.png)
<br/>

**View playlist and select song to play as well as shuffle and skip through and adjust volume of songs:**
<br/><br/>
![View and Play Songs](/static/img/README/old_songs.png)
<br/>

**Generate a new playlist (automatically adds to saved playlists page) by selecting genre and minimum and maximum danceability:**
<br/><br/>
![Generate New Playlist](/static/img/README/generate_playlist.png)
<br/>

**View newly generated playlist and select song to play as well as shuffle and skip through and adjust volume of songs:**
<br/><br/>
![View and Play Songs](/static/img/README/new_songs.png)
<br/>

<a name="features"/></a>
## Future Features
* Allow OAuth authentication for user to save playlists directly to their Spotify account
* Allow user to delete playlists from their playlists page
* Give user ability to share playlists with other users of Vibez account 