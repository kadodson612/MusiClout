# Paradigms Final Project

## Members

1. Edoardo Bianchi (ebianchi@nd.edu)
2. Kelly Dodson (kdodson@nd.edu)
3. Chandler Crane (ccrane2@nd.edu)
4. Lauren Whalen (lwhalen2@nd.edu)

## Project Description

This project uses the Spotify API to allow users to create lists of their favorite artists, albums,
and songs, providing those artists, albums or songs are on Spotify. It also provides a host of information
about the members of each of these lists. The project will use these lists to generate a music personality profile
along with the user's "clout" score, and it can generate a playlist of recommended songs.

## Server

To run the server, run this command in the /ooapi folder: 

`alias python3=/afs/nd.edu/user14/csesoft/2017-fall/anaconda3/bin/python3`

`python3 main.py`

To see API documentation about the different endpoints offered and their functionality, please visit:


    https://docs.google.com/spreadsheets/d/1OztSsBcycN-YcCGQ-jNgQt3kvYdmfxj2u84kPy9LMys/edit?usp=sharing 
    
## Clients

### Web Client

To run the client, start the server as shown above.

To add artists, tracks, or albums to your personality, use the Clout Search feature. 

To show your personality, click on the purple "Get Personality" button.

You can delete parts of your personality by clicking the trash can button to the right of an item.

![](https://media.giphy.com/media/5YiPHtqw0VWK6oYwKt/200w_d.gif)


We used a template to complete the web client. See the credits at the bottom.

#### Web Client Tests

To test the web client, we:

-verified all buttons by clicking them and observing their actions

-verified that data persists after refresh

-verified that the personality paragraph shows up if >= 1 artist is listed on the user's profile

### Extra Credit Client

To run the client, first start the server (see above).

In another terminal window, run these commands in the /ooapi folder:

 `alias python3.5=/afs/nd.edu/user14/csesoft/2017-fall/python3.5/bin/python3`
 
 `python3.5 extracredit.py`
 
 The main page shows your username and music personality advice.
 
 Click the Profile feature in the actions menu to view your username and favorite music.
 
 Click the set user feature to log into a new user.
 
 Click the add artists, tracks, and albums feature to add new Spotify IDs for your favorite music.
 
 #### Extra Credit Client Tests

To test the web client, we:

-verified all buttons by clicking them and observing their actions

-verified that the personality paragraph shows up if >= 1 artist is listed on the user's profile

-verified that changing the username properly changes the personality and Profile

-verified that all popup buttons and information are correct

-Tested all menu actions. If there is an error inserting your fave music, an error message pops up.

## Python functions


### Artists

"get_artist" returns all information for a given artist liked by the user

"get_artists" returns all artists liked by a given user

Given artist ID, "set_artist," like a post request, adds artist to user's liked artists using the Spotify API as a data source.

"set_artist_info" changes key and value pair, like a put request, updating info about the artist from Spotify

"delete_artist" deletes one of the artists in the user's liked artists list

"delete_all_artists" deletes all of the artists in the user's liked artists list

### Albums

"get_albums" returns all albums liked by the user (with a uid)

"get_album" returns an album with a particular album_id liked by the user

"set_album," adds an album along with its artists, id, label, name, popularity, etc. using the Spotify API as a data source.

"set_album_info" changes key and value pair, like a put request, updating info about the album from Spotify

"delete_album" deletes one of the albums with a specified album ID from the user's liked albums list

"delete_all_albums" deletes all of the albums in the user's liked albums list

### Tracks

"get_tracks" returns all tracks liked by the user (with a uid)

"get_track" returns an tracks with a particular track_id liked by the user

"set_track," adds a track along with its information to user's liked track list using the Spotify API as a data source.

"set_track_info" changes key and value pair, like a put request, updating info about the track from Spotify

"delete_track" deletes one of the tracks with a specified track ID from the user's liked tracks list

"delete_all_tracks" deletes all of the tracks in the user's liked tracks list


## Tests

Run the plain Python function unit tests by running:

`alias python3=/afs/nd.edu/user14/csesoft/2017-fall/anaconda3/bin/python3`

`python3 test_spotify_apis.py`

### Tests for plain Python functions: 
The tests below test and verify the functionality of all the aforementioned functions.

-reset_data

-test_get_and_set_albums

-test_get_album

-test_delete_album

-test_set_album_info

-test_get_and_set_tracks

-test_get_track

-test_delete_track

-test_set_track_info

-test_get_and_set_artists

-test_get_artist

-test_delete_artist

-test_set_artist_info

### Tests for Server API endpoints:

First, start running the server using main.py. Then, run the server API endpoint tests with:

`alias python3=/afs/nd.edu/user14/csesoft/2017-fall/anaconda3/bin/python3`

`python3 test_server.py`

The server tests below verify the functionality of the server.


-reset_data

-is_json

-test_artists_get

-test_albums_get

-test_tracks_get

-test_artist_post

-def test_album_post

-def test_track_post

-def test_artist_put

-def test_album_put

-def test_track_put

## Credits

For our web client, we used a template called DashGum.
Copyright 2014 by Carlos Alvarez.
Developer Website: Alvarez.is

