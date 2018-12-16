import unittest
import requests
import json

class TestServer(unittest.TestCase):
	SITE_URL = 'http://student04.cse.nd.edu:52052'

	#URLs to get and store a user's favorite artists, albums, and tracks
	ARTIST_URL = SITE_URL + '/artists/'
	ALBUM_URL = SITE_URL + '/albums/'
	TRACK_URL = SITE_URL + '/tracks/'

	ARTIST_USER_URL = SITE_URL + '/1/artists/'
	ALBUM_USER_URL = SITE_URL + '/1/albums/'
	TRACK_USER_URL = SITE_URL + '/1/tracks/'

	#Delete/reset all data
	def reset_data(self):
		r = requests.delete(self.ARTIST_URL)
		resp = json.loads(r.content.decode())
		self.assertEqual(resp['result'], 'success')

		r = requests.delete(self.ALBUM_URL)
		resp = json.loads(r.content.decode())
		self.assertEqual(resp['result'], 'success')

		r = requests.delete(self.TRACK_URL)
		resp = json.loads(r.content.decode())
		self.assertEqual(resp['result'], 'success')

	def is_json(self, resp):
		try:
			json.loads(resp)
			return True
		except ValueError:
			return False

	#Test all basic GET functions
	def test_artists_get(self):
		self.reset_data()
		r = requests.get(self.ARTIST_USER_URL)
		self.assertTrue(self.is_json(r.content.decode()))
		resp = json.loads(r.content.decode())
		self.assertEqual(resp['result'], 'success')
	
	def test_albums_get(self):
		self.reset_data()
		r = requests.get(self.ALBUM_USER_URL)
		self.assertTrue(self.is_json(r.content.decode()))
		resp = json.loads(r.content.decode())
		self.assertEqual(resp['result'], 'success')

	def test_tracks_get(self):
		self.reset_data()
		r = requests.get(self.TRACK_USER_URL)
		self.assertTrue(self.is_json(r.content.decode()))
		resp = json.loads(r.content.decode())
		self.assertEqual(resp['result'], 'success')

	#Test all basic POST functions
	def test_artist_post(self):
		self.reset_data()
		r = requests.post(self.ARTIST_USER_URL + '/4iHNK0tOyZPYnBU7nGAgpQ', data=None)
		self.assertTrue(self.is_json(r.content.decode()))
		resp = json.loads(r.content.decode())
		self.assertEqual(resp['result'], 'success')
	
	def test_album_post(self):
		self.reset_data()
		r = requests.post(self.ALBUM_USER_URL + '/7xStSCA0cJ3CMuZsd3Fct5', data=None)
		self.assertTrue(self.is_json(r.content.decode()))
		resp = json.loads(r.content.decode())
		self.assertEqual(resp['result'], 'success')
	
	def test_track_post(self):
		self.reset_data()
		r = requests.post(self.TRACK_USER_URL + '/0bYg9bo50gSsH3LtXe2SQn', data=None)
		self.assertTrue(self.is_json(r.content.decode()))
		resp = json.loads(r.content.decode())
		self.assertEqual(resp['result'], 'success')

	#Test all basic PUT functions
	def test_artist_put(self):
		self.test_artist_post()
		data = json.dumps({"artists": "Kelly Dodson"})
		r = requests.put(self.ARTIST_USER_URL + '/4iHNK0tOyZPYnBU7nGAgpQ', data=data)
		self.assertTrue(self.is_json(r.content.decode()))
		resp = json.loads(r.content.decode())
		self.assertEqual(resp['result'], 'success')
 
		#Determine if PUT request worked
		r = requests.get(self.ARTIST_USER_URL)
		resp = json.loads(r.content.decode())

	def test_album_put(self):
		self.test_album_post()
		data = json.dumps({"artists": "Kelly Dodson"})
		r = requests.put(self.ALBUM_USER_URL + '/7xStSCA0cJ3CMuZsd3Fct5', data=data)
		self.assertTrue(self.is_json(r.content.decode()))
		resp = json.loads(r.content.decode())
		self.assertEqual(resp['result'], 'success')
		
		r = requests.get(self.ALBUM_USER_URL)
		resp = json.loads(r.content.decode())
		self.assertEqual(resp['entries']['7xStSCA0cJ3CMuZsd3Fct5']['artists'], 'Kelly Dodson')

	def test_track_put(self):
		self.test_track_post()
		data = json.dumps({"artists": "Kelly Dodson"})
		r = requests.put(self.TRACK_USER_URL + '/0bYg9bo50gSsH3LtXe2SQn', data=data)
		self.assertTrue(self.is_json(r.content.decode()))
		resp = json.loads(r.content.decode())
		self.assertEqual(resp['result'], 'success')

		r = requests.get(self.TRACK_USER_URL)
		resp = json.loads(r.content.decode())
		self.assertEqual(resp['entries']['0bYg9bo50gSsH3LtXe2SQn']['artists'], 'Kelly Dodson')
		
if __name__ == "__main__":
        unittest.main()

