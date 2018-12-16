import cherrypy
from movies import MovieController
from users import UserController
from votes import VoteController
from ratings import RatingController
from reset import ResetController

from _movie_database import _movie_database

def start_service():
	dispatcher = cherrypy.dispatch.RoutesDispatcher()

	#instantiate mdb
	mdb_o = _movie_database()

	#instantiate controllers
	movieController = MovieController(mdb=mdb_o)
	userController = UserController(mdb=mdb_o)
	voteController = VoteController(mdb=mdb_o)
	ratingController = RatingController(mdb=mdb_o)
	resetController = ResetController(mdb=mdb_o)
	#TODO
	dispatcher.connect('movie_get_mid', controller=movieController, action='GET_MID', conditions=dict(method=['GET']))

	#configuration
	conf = {
		'global': {
			'server.socket_host': 'student04.cse.nd.edu',
			'server.socket_port': '52052', #change this

			},
		'/': {
			'request.dispatch': dispatcher,
			}
		}
	cherrypy.config.update(conf)
	app = cherrypy.tree.mount(None, config=conf)
	cherrypy.quickstart(app)


	if __name__ == '__main__':
		start_service()


