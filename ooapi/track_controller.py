import json
import cherrypy
import requests

from _spotify_interface import _spotify_interface

class TrackController(object):
	def __init__(self, spi=None):
			if spi is None:
				self.spi = _spotify_interface()
			else:
				self.spi = spi

	def GET_TRACKS(self, uid):
		output = {"result" : "success"}
		output["entries"] = {}
		try:
			output["entries"] = self.spi.get_tracks(uid)
		except Exception as ex:
			output["result"] = 'error'
			output["message"] = str(ex)

		return json.dumps(output)

	def POST_TRACK_NAME(self, uid, name):
		output = {'result' : 'success'}
		try:
			track_id = self.spi.find_id_from_name(name, kind="track")
			if track_id is not None:
				self.spi.set_track(uid, track_id)
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
	
	def POST_TRACK(self, uid, track_id):
		output = {"result" : "success"}
		
		try:
			self.spi.set_track(uid, track_id)
		except KeyError as ex:
			output["result"] = "error"
			output["message"] = "Key not found in dictionary"
		except Exception as ex:
			output["result"] = "error"
			output["message"] = str(ex)

		return json.dumps(output)

	def PUT_TRACK(self, uid, track_id):
		output = {"result" : "success"}
		data = json.loads(cherrypy.request.body.read())
		try:
			self.spi.set_track_info(uid, track_id, data)
		except KeyError as ex:
			output["result"] = "error"
			output["message"] = "Key not found in dictionary"
		except Exception as ex:
			output["result"] = "error"
			output["message"] = str(ex)

		return json.dumps(output)

	def DELETE_TRACK_KEY(self, uid, track_id):
		output = {"result" : "success"}
		try:
			self.spi.delete_track(uid, track_id)
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
			self.spi.delete_all_tracks(uid)
		except KeyError as ex:
			output["result"] = "error"
			output["message"] = "Key not found in dictionary"
		except Exception as ex:
			output["result"] = "error"
			output["message"] = str(ex)

		return json.dumps(output)
			
	def DELETE_TRACKS(self):
		output = {"result" : "success"}
		try:
			self.spi.delete_all_tracks()
		except KeyError as ex:
			output["result"] = "error"
			output["message"] = "Key not found in dictionary"
		except Exception as ex:
			output["result"] = "error"
			output["message"] = str(ex)

		return json.dumps(output)

			

