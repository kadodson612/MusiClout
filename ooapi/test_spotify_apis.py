from _spotify_interface import _spotify_interface
import unittest


class TestSpotifyApis(unittest.TestCase):
  """unit tests for Spotify OO API assignment"""
  """Note: this file uses spaces, not tabs """

  spotify = _spotify_interface()

  def reset_data(self):
    self.spotify.set_artist(1, "4iHNK0tOyZPYnBU7nGAgpQ")
    self.spotify.set_album(1, "7xStSCA0cJ3CMuZsd3Fct5")
    self.spotify.set_track(1, "0bYg9bo50gSsH3LtXe2SQn")

    self.spotify.delete_all_albums_user(1)
    self.spotify.delete_all_tracks_user(1)
    self.spotify.delete_all_artists_user(1)

    artists	= self.spotify.get_artists(1) 
    albums 	= self.spotify.get_albums(1)
    tracks 	= self.spotify.get_tracks(1)

    self.assertEqual(artists, {})
    self.assertEqual(albums, {})
    self.assertEqual(tracks, {})
	
  def test_get_and_set_albums(self):
    self.reset_data()
    self.spotify.set_album(1, "7xStSCA0cJ3CMuZsd3Fct5")
    albums = self.spotify.get_albums("1")
    self.assertEqual(list(albums.keys())[0],"7xStSCA0cJ3CMuZsd3Fct5")

  def test_get_album(self):
    self.reset_data()
    self.spotify.set_album(1, "7xStSCA0cJ3CMuZsd3Fct5")
    album = self.spotify.get_album(1, "7xStSCA0cJ3CMuZsd3Fct5")
    self.assertEqual(album["name"], "Falling (pluko Remix)")
	
  def test_delete_album(self):
    self.reset_data()
    self.spotify.set_album(1, "7xStSCA0cJ3CMuZsd3Fct5")
    self.spotify.delete_album(1, "7xStSCA0cJ3CMuZsd3Fct5")
    album = self.spotify.get_album(1, "7xStSCA0cJ3CMuZsd3Fct5")
    self.assertEqual(album, {})

  def test_set_album_info(self):
    self.reset_data()
    self.spotify.set_album(1, "7xStSCA0cJ3CMuZsd3Fct5")
    a = {"name": "Kelly Dodson"}
    self.spotify.set_album_info(1, "7xStSCA0cJ3CMuZsd3Fct5", a)
    albums = self.spotify.get_albums(1)
    self.assertEqual(albums["7xStSCA0cJ3CMuZsd3Fct5"]["name"],"Kelly Dodson")

  def test_get_and_set_tracks(self):
    self.reset_data()
    self.spotify.set_track(1, "0bYg9bo50gSsH3LtXe2SQn")
    tracks = self.spotify.get_tracks(1)
    self.assertEqual(list(tracks.keys())[0],"0bYg9bo50gSsH3LtXe2SQn")
  
  def test_get_track(self):
    self.reset_data()
    self.spotify.set_track(1, "0bYg9bo50gSsH3LtXe2SQn")
    track = self.spotify.get_track(1, "0bYg9bo50gSsH3LtXe2SQn")
    self.assertEqual(track["name"], "All I Want for Christmas Is You")
  
  def test_delete_track(self):
    self.reset_data()
    self.spotify.set_track(1, "0bYg9bo50gSsH3LtXe2SQn")
    self.spotify.delete_track(1, "0bYg9bo50gSsH3LtXe2SQn")
    track = self.spotify.get_track(1, "0bYg9bo50gSsH3LtXe2SQn")
    self.assertEqual(track, {})

  def test_set_track_info(self):
    self.reset_data()
    self.spotify.set_track(1, "0bYg9bo50gSsH3LtXe2SQn")
    a = {"name": "Kelly Dodson"}
    self.spotify.set_track_info(1, "0bYg9bo50gSsH3LtXe2SQn", a)
    tracks = self.spotify.get_tracks(1)
    self.assertEqual(tracks["0bYg9bo50gSsH3LtXe2SQn"]["name"],"Kelly Dodson")

  def test_get_and_set_artists(self):
    self.reset_data()
    self.spotify.set_artist(1, "4iHNK0tOyZPYnBU7nGAgpQ")
    artists = self.spotify.get_artists(1)
    self.assertEqual(list(artists.keys())[0],"4iHNK0tOyZPYnBU7nGAgpQ")

  def test_get_artist(self):
    self.reset_data()
    self.spotify.set_artist(1, "4iHNK0tOyZPYnBU7nGAgpQ")
    artist = self.spotify.get_artist(1, "4iHNK0tOyZPYnBU7nGAgpQ")
    self.assertEqual(artist["name"], "Mariah Carey")

  def test_delete_artist(self):
    self.reset_data()
    self.spotify.set_artist(1, "4iHNK0tOyZPYnBU7nGAgpQ")
    self.spotify.delete_artist(1, "4iHNK0tOyZPYnBU7nGAgpQ")
    artist = self.spotify.get_artist(1, "4iHNK0tOyZPYnBU7nGAgpQ")
    self.assertEqual(artist, {})

  def test_set_artist_info(self):
    self.reset_data()
    self.spotify.set_artist(1, "4iHNK0tOyZPYnBU7nGAgpQ")
    a = {"name": "Kelly Dodson"}
    self.spotify.set_artist_info(1, "4iHNK0tOyZPYnBU7nGAgpQ",a)
    artist = self.spotify.get_artist(1, "4iHNK0tOyZPYnBU7nGAgpQ")
    self.assertEqual(artist["name"], "Kelly Dodson")


if __name__ == "__main__":
    unittest.main()

