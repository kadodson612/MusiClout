import json
import cherrypy
import requests

from _spotify_interface import _spotify_interface

class AlbumController(object):
	def __init__(self, spi=None):		
		if spi is None:
			self.spi = _spotify_interface()
		else:
			self.spi = spi

	def GET_ALBUMS(self,uid):
		output = {"result" : "success"}
		output["entries"] = []
		try:
			output["entries"] = self.spi.get_albums(uid)
		except Exception as ex:
			output["result"] = 'error'
			output["message"] = str(ex)
		
		return json.dumps(output)
	
	def POST_ALBUM_NAME(self, uid, name):
		output = {'result' : 'success'}
		try:
			album_id = self.spi.find_id_from_name(name, kind="album")
			if album_id is not None:
				self.spi.set_album(uid, album_id)
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

	def POST_ALBUM(self, uid, album_id):
		output = {"result" : "success"}
		try:
			self.spi.set_album(uid, album_id)
		except KeyError as ex:
			output["result"] = "error"
			output["message"] = "Key not found in dictionary"
		except Exception as ex:
			output["result"] = "error"
			output["message"] = str(ex)

		return json.dumps(output)

	def PUT_ALBUM(self, uid, album_id):
		output = {"result" : "success"}
		data = json.loads(cherrypy.request.body.read())
		try:
			self.spi.set_album_info(uid, album_id, data)	
		except KeyError as ex:
			output["result"] = "error"
			output["message"] = "Key not found in dictionary"
		except Exception as ex:
			output["result"] = "error"
			output["message"] = str(ex)
		
		return json.dumps(output)

	def DELETE_ALBUM_KEY(self, uid, album_id):
		output = {"result" : "success"}
		try:
			self.spi.delete_album(uid, album_id)
		except KeyError as ex:
			output["result"] = "error"
			output["message"] = "Key not found in dictionary"
		except Exception as ex:
			output["result"] = "error"
			output["message"] = str(ex)

		return json.dumps(output)

	def DELETE(self, uid):
		output = {"result" : "success"}
		try:
			self.spi.delete_all_albums(uid)
		except KeyError as ex:
			output["result"] = "error"
			output["message"] = "Key not found in dictionary"
		except Exception as ex:
			output["result"] = "error"
			output["message"] = str(ex)

		return json.dumps(output)

	def DELETE_ALBUMS(self):
		output = {"result" : "success"}
		try:
			self.spi.delete_all_albums()
		except KeyError as ex:
			output["result"] = "error"
			output["message"] = "Key not found in dictionary"
		except Exception as ex:
			output["result"] = "error"
			output["message"] = str(ex)

		return json.dumps(output)

		
			


			
