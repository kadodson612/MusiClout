import cherrypy
import json
from _movie_database import _movie_database

class MovieController(object):
	def __init__(self, mdb=None):
		if mdb is None:
			self.mdb = _movie_database()
		else:
			self.mdb = mdb

		self.mdb.load_movies('ml-1m/movies.dat')
		self.load_posters('ml-1m/images.dat') #TODO: create this method

	def GET_MID(self, movie_id):
		output = {'result': 'success'}
		movie_id = int(movie_id)

		try:
			movie = self.mdb.get_movie(movie_id)
			if movie is not None:
				output['id'] = movie_id
				output['title'] = movie[0]
				output['genre'] = movie[1]
				output['img'] = self.get_poster_by_mid(movie_id)
			else:
				output['result'] = 'error'
				output['message'] = 'Movie not found.'

		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)

		return json.dumps(output)

	def get_poster_by_mid(self, mid):
		#TODO get the poster information
		if mid in self.posters.keys()
			return self.posters(mid)
		else:
			return '/default.jpg'

	def load_posters(self, posters_file):
		self.posters = {}
		f = open(posters_file)
		for line in f:
			line = line.strip().split('::')
			#TODO string parsing
			self.posters[mid] = m_img
		f.close()
