import requests
import json

class _spotify_interface:
	def __init__(self):
		# Lists of favorite albums
		self.albums = {}
		self.artists = {}
		self.tracks = {}
		headers = self.get_auth_token()

	def get_auth_token(self):	
		body = {"grant_type" : "client_credentials"}
		#TODO: PUT YOUR SPOTIFY TOKEN HERE
		posthead = {"Content-Type" : "application/x-www-form-urlencoded", "Authorization" : "Basic TOKEN-HERE"}
		r = requests.post("https://accounts.spotify.com/api/token",data=body,headers=posthead)
		auth = json.loads(r.content.decode())
		token = auth['access_token']
		headers = {"Authorization" : "Bearer " + token}
		return headers

	def get_albums(self, uid):
		uid = str(uid)
		if uid in self.albums.keys():
			return self.albums[uid]
		return None

	def get_album(self, uid, album_id):
		uid = str(uid)
		if str(uid) in self.albums:
			if str(album_id) in self.albums[str(uid)]:
				return self.albums[str(uid)][str(album_id)]

		return None

	def set_album(self, uid, album_id):
		uid = str(uid)
		headers = self.get_auth_token()
		r = requests.get("https://api.spotify.com/v1/albums/" + str(album_id),headers=headers)
		data = json.loads(r.content.decode())
		artists = [a["name"] for a in data["artists"]]

		if str(uid) not in self.albums:
			self.albums[str(uid)] = {}
				
		if str(album_id) not in self.albums[str(uid)]:
			self.albums[str(uid)][str(album_id)] = {}

		if len(artists) > 1:
			artists = ",".join(artists)
		else:
			artists = artists[0]

		self.albums[str(uid)][str(album_id)] = {
			"artists" : artists,
			"id" : str(data["id"]),
			"label" : str(data["label"]),
			"name" : str(data["name"]),
			"popularity" : int(data["popularity"]),
			"release" : str(data["release_date"]),
			"total_tracks" : int(data["total_tracks"]),
			"album_type" : str(data["type"])
		}
	
	def set_album_info(self, uid, album_id, a):
		uid = str(uid)
		if not len(a.keys()):
			print("Please enter valid dictionary")

		elif len(a.keys()) < 2:
			self.albums[uid][str(album_id)][list(a.keys())[0]] = list(a.values())[0]

		elif str(album_id) in self.albums[str(uid)]:
			for k,v in a:
				self.albums[str(uid)][str(album_id)][str(k)] = v
		else:
			self.albums[str(uid)][str(album_id)] = {}

	def delete_album(self, uid, album_id):
		uid = str(uid)
		if str(uid) in self.albums:
			if str(album_id) in self.albums[str(uid)]:
				del self.albums[str(uid)][str(album_id)]

	def delete_all_albums_user(self, uid):
		uid = str(uid)
		if str(uid) in self.albums:
			self.albums[str(uid)] = {}

	def delete_all_albums(self):
		self.albums = {}

	def get_tracks(self, uid):
		uid = str(uid)
		if str(uid) in self.tracks.keys():
			return self.tracks[str(uid)]
		return None
				
	def get_track(self, uid, track_id):
		uid = str(uid)
		if str(uid) in self.tracks:
			if str(track_id) in self.tracks[str(uid)]:	
				return self.tracks[str(uid)][str(track_id)]

		return None
	
	def set_track(self, uid, track_id):
		uid = str(uid)
		headers = self.get_auth_token()
		r = requests.get("https://api.spotify.com/v1/tracks/" + str(track_id), headers=headers)
		data = json.loads(r.content.decode())
		
		artists = [ a["name"] for a in data["artists"] ] 

		if(len(artists) > 1):
			artists = ','.join(artists)
		else:
			artists = artists[0]				

		if str(uid) not in self.tracks:
			self.tracks[str(uid)] = {}
		
		if str(track_id) not in self.tracks[str(uid)]:
			self.tracks[str(uid)][str(track_id)] = {}
		
		self.tracks[str(uid)][str(track_id)] = {
			"artists" : artists,
			"id" : data["id"],
			"name" : data["name"],
			"release" : data["album"]["release_date"],
			"explicit" : data["explicit"],
			"popularity" : data["popularity"]
		}

	def set_track_info(self, uid, track_id, a):
		uid = str(uid)
		if not len(a.keys()):
			print("Please enter valid dictionary")

		elif len(a.keys()) < 2:
			self.tracks[uid][str(track_id)][list(a.keys())[0]] = list(a.values())[0]

		elif str(track_id) in self.tracks[str(uid)]:
			for k,v in track:
				self.tracks[str(uid)][str(track_id)][str(k)] = v
		else:
			self.tracks[str(uid)][str(track_id)] = {}

	def delete_track(self, uid, track_id):
		uid = str(uid)
		if str(uid) in self.tracks:
			if str(track_id) in self.tracks[str(uid)]:
				del self.tracks[str(uid)][str(track_id)]

	def delete_all_tracks_user(self, uid):
		uid = str(uid)
		if str(uid) in self.tracks:
			self.tracks[str(uid)] = {}

	def delete_all_tracks(self):
		self.tracks = {}

	def get_artists(self, uid):
		uid = str(uid)
		if uid in self.artists.keys():
			return self.artists[str(uid)]
		return None

	def get_artist(self, uid, artist_id):
		uid = str(uid)
		if uid in self.artists:
			if artist_id in self.artists[str(uid)]:
				return self.artists[str(uid)][str(artist_id)]

		return None

	def set_artist(self, uid, artist_id):	
		uid = str(uid)
		headers = self.get_auth_token()
		r = requests.get("https://api.spotify.com/v1/artists/" + str(artist_id), headers=headers) # headers
		data = json.loads(r.content.decode())
  
		if str(uid) not in self.artists:
			self.artists[str(uid)] = {}

		if str(artist_id) not in self.artists[str(uid)]:
			self.artists[str(uid)][str(artist_id)] = {}

		self.artists[str(uid)][str(artist_id)] = {
				"name":		str(data["name"]),
				"followers": 	str(data["followers"]["total"]),
				"genres": 	str(data["genres"]),
				"id": 		str(data["id"]),
				"popularity": 	int(data["popularity"])
		}
		
	def set_artist_info(self, uid, artist_id, a):
		uid = str(uid)
		if str(artist_id) in self.artists[str(uid)]:
			if not len(a.keys()):
				print("Please enter valid dictionary")
			elif len(a.keys()) < 2:
				self.artists[uid][str(artist_id)][list(a.keys())[0]] = list(a.values())[0]
			else:
				for k,v in a:
					self.artists[str(uid)][str(artist_id)][str(k)] = v
		else:
			self.artists[str(uid)][str(artist_id)] = {}

	def delete_artist(self, uid, artist_id):
		uid = str(uid)
		if str(uid) in self.artists:
			if str(artist_id) in self.artists[str(uid)]:
				del self.artists[str(uid)][str(artist_id)]

	def delete_all_artists_user(self, uid):
		uid = str(uid)
		if str(uid) in self.artists:
			self.artists[str(uid)] = {}

	def delete_all_artists(self):
		self.artists = {}

	def find_id_from_name(self, name, kind):
		headers = self.get_auth_token()
		params = {}
		if kind == "artist":
			params = {"type" : "artist"}
		elif kind == "album":
			params = {"type" : "album"}
		elif kind == "track":
			params = {"type" : "track"}
		else:
			print("Not a valid type: {} (artist, album, or track)".format(str(kind)))
			return None

		params['q'] = name
			
		s = requests.get("https://api.spotify.com/v1/search", headers=headers, params=params)
		
		if kind == "artist":
			results = json.loads(s.content.decode())["artists"]["items"]
		elif kind == "album":	
			results = json.loads(s.content.decode())["albums"]["items"]
		elif kind == "track":
			results = json.loads(s.content.decode())["tracks"]["items"]


		url = ""
		for item in results:
			if item["name"].lower() == name.lower():
				url = item["external_urls"]["spotify"]

		# Find id
		name_id = url.split("/")[4]

		return name_id

	def get_audio_features(self, track_id):
		headers = get_auth_token()
		r = requests.get("https://api.spotify.com/v1/audio-features/" + track_id, headers=headers)
		data = json.loads(r.content.decode())
		features = {
			"danceability" : data["danceability"],
			"energy" : data["energy"],
			"loudness" : data["loudness"],
			"speechiness" : data["speechiness"],
			"acousticness" : data["acousticness"],
			"instrumentalness" : data["instrumentalness"],
			"liveness" : data["liveness"],
			"valence" : data["valence"],
			"tempo" : data["tempo"]
		}

		return features
		
if __name__ == "__main__":
	spi = _spotify_interface()
	name_id = spi.find_id_from_name("Kanye West", kind="artist")
	
		
