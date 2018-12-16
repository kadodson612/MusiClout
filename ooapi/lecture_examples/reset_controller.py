import cherrypy
import json

from _movie_database import _movie_database

class ResetController(object):
	def __init__(self, mdb=None):
		if mdb is None:
			self.mdb = _movie_database()
		else:
			self.mdb = mdb

	def PUT_INDEX(self):
		output = {'result': 'success'}
		data = json.loads(cherrypy.request.body.read())
		try:
			self.mdb.load_movies('ml-1m/movies.dat')
			self.mdb.load_users('ml-1m/users.dat')
			self.mdb.load_ratings('ml-1m/ratings.dat')
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)
		return json.dumps(output)

	def PUT_MID(self, movie_id):
		#TODO
		output = {'result': 'success'}
		mid = int(movie_id)

		try:
			data = json.loads(cherrypy.request.body.read())
			mdb_tmp = _movie_database()
			mdb_tmp.load_movies('ml-1m/movies.dat')
			mdb = mdb_tmp.get_movie(mid)
			self.mdb.set_movie(mid, movie) #also set genre 

