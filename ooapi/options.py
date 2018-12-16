import json
import cherrypy

class OptionsController(object):
	def __init__(self):
		print("Options controller initializing")
	
	def OPTIONS(self, *args, **kwargs):
		return ""


