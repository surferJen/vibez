# Vibez

Vibez is a web application that utilizes Spotify's API to generate playlists based on a user's choice of genre and a minimum and maximum range of danceability levels (0 - 0.1).

## Table of Contents
* [Overview](#overview)<br/>
* [Tech Stack](#techstack)<br/>
* [Setup/Installation](#installation)<br/>
* [Demo](#demo)<br/>
* [Future Features](#future)

<a name="overview"/></a>
## Overview
Once a user logs into their account and generates a new playlist, Vibez gathers and stores the playist's history in a PostgreSQL database along with information for three audio features: music genre, minimum danceability, maximum danceability. Playlists are generated requesting pertinent info from Spotify's API. Once the backend receives Spotify's JSON, Vibez integrates the JSON into the Amplitude.js library to showcase its lists of songs and its accompanying shuffle, fast-forward, rewind, scroll, and other convenient functions. In order to display a page of stored playlists, Vibez assimilates interactive, complex visuals rendered by code that is extracted and heavily refactored from the D3.js library. Both Amplitude.js and D3.js require heavy use of jQuery, Javascript, CSS, and HTML. Accessing a stored playlist works similarly as generating a new playlist, except a different Spotify endpoint is requested.

<a name="techstack"/></a>
## Tech Stack
**Frontend:** Javascript (AJAX, JSON), jQuery, Jinja, HTML, CSS, Bootstrap</br>
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
$ git clone https://github.com/jaegotsumcheeks/vibez.git
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
**Log in through Spotify and create your playlist by selecting a mood:**
<br/><br/>
![Homepage](/static/images/readme/homepage.gif)
<br/>

**Once created, play your playlist through Spotify Web Player or through Moodify:**
<br/><br/>
![Selecting Mood](/static/images/readme/created.gif)
<br/>

**View playlist and select song to play as well as skip through songs:**
<br/><br/>
![View and Play Playlist](/static/images/readme/playlist-player.gif)
<br/>

<a name="features"/></a>
## Future Features
* Fine tune algorithm that selects songs
* Give user's the ability to view all their past mood playlists
* Option to preview playlist and then save it