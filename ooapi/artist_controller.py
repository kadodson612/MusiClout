import json
import cherrypy
import requests

from _spotify_interface import _spotify_interface

class ArtistController(object):
	def __init__(self, spi=None):
		if spi is None:
			self.spi = _spotify_interface()
		else:
			self.spi = spi
			
	#event handlers for resource requests
	
	def GET_ARTISTS(self, uid):
		output = {'result': 'success'}
		output["entries"] = []
		try:
			output["entries"] = self.spi.get_artists(uid)
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = 'There was an error processing the request.'

		return json.dumps(output)

	def POST_ARTIST_NAME(self, uid, name):
		output = {'result' : 'success'}
		try:
			artist_id = self.spi.find_id_from_name(name, kind="artist")
			print(artist_id)
			if artist_id is not None:
				self.spi.set_artist(uid, artist_id)
			else:
				output['result'] = 'error'
				output['message'] = 'Invalid search'
		except KeyError as ex:
			output['result'] = 'error'
			output['message'] = 'Key not found in dictionary.'
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex) #provides information about the error
	
		return json.dumps(output)

	def POST_ARTIST(self, uid, artist_id):
		output = {'result': 'success'}
		try:
			self.spi.set_artist(uid, artist_id)
		except KeyError as ex:
			output['result'] = 'error'
			output['message'] = 'Key not found in dictionary.'

		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex) #provides information about the error

		return json.dumps(output)  
	
	def PUT_ARTIST(self, uid, artist_id):
		output = {'result': 'success'}   
		try:
			data = json.loads(cherrypy.request.body.read())
			self.spi.set_artist_info(uid, artist_id, data)
		except KeyError as ex:
			output['result'] = 'error'
			output['message'] = 'Key not found in dictionary.'
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex) #provides information about the error

		return json.dumps(output)  


	def DELETE_ARTIST_KEY(self, uid, artist_id):
		output = {'result': 'success'}
		try:
			self.spi.delete_artist(uid, artist_id)
		except KeyError as ex:
			output['result'] = 'error'
			output['message'] = 'Key not found in dictionary.'
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex) #provides information about the error
		return json.dumps(output)

	def DELETE_ARTISTS(self):
		output = {'result': 'success'}
		try:
			self.spi.delete_all_artists()
		except KeyError as ex:
			output['result'] = 'error'
			output['message'] = 'Key not found in dictionary.'
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex) #provides information about the error
		return json.dumps(output)



	# DELETE_ALL_ARTISTS

