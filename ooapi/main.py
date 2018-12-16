#code
import cherrypy
import json
import sys
from _spotify_interface import _spotify_interface
from artist_controller import ArtistController
from album_controller import AlbumController
from track_controller import TrackController
from personality import Personality
from options import OptionsController

def CORS():
    #allow requests from any origin
    cherrypy.response.headers["Access-Control-Allow-Origin"] = "*"
    cherrypy.response.headers["Access-Control-Allow-Methods"] = "GET, PUT, POST, DELETE, OPTIONS"
    cherrypy.response.headers["Access-Control-Allow-Credentials"] = "*"

def start_service():
    interface = _spotify_interface()
    artistcon = ArtistController(interface)
    albumcon = AlbumController(interface)
    trackcon = TrackController(interface)
    personalitycon = Personality(interface)
    optionsController = OptionsController()

    #set up defaultUser username
    interface.set_track("defaultUser", "0bYg9bo50gSsH3LtXe2SQn")
    interface.set_track("defaultUser", "1xzBco0xcoJEDXktl7Jxrr")
    interface.set_album("defaultUser", "61ulfFSmmxMhc2wCdmdMkN")
    interface.set_artist("defaultUser","4iHNK0tOyZPYnBU7nGAgpQ")
    interface.set_artist("defaultUser", "6LuN9FCkKOj5PcnpouEgny")

    #create a dispatcher
    dispatcher = cherrypy.dispatch.RoutesDispatcher()

    dispatcher.connect('spotify_get_artists', '/:uid/artists/', controller=artistcon, action='GET_ARTISTS', conditions=dict(method=['GET']) )
    dispatcher.connect('spotify_post_artist', '/:uid/artists/:artist_id', controller=artistcon, action='POST_ARTIST', conditions=dict(method=['POST']) )
    dispatcher.connect('spotify_post_artist_name', '/:uid/artists/name/:name', controller=artistcon, action='POST_ARTIST_NAME', conditions=dict(method=['POST']) )
    dispatcher.connect('spotify_put_artist', '/:uid/artists/:artist_id', controller=artistcon, action='PUT_ARTIST', conditions=dict(method=['PUT']) )
    dispatcher.connect('spotify_delete_artist', '/:uid/artists/:artist_id', controller=artistcon, action='DELETE_ARTIST_KEY', conditions=dict(method=['DELETE']) )
    dispatcher.connect('spotify_delete_artists', '/artists/', controller=artistcon, action='DELETE_ARTISTS', conditions=dict(method=['DELETE']) )


    dispatcher.connect('spotify_get_albums', '/:uid/albums/', controller=albumcon, action='GET_ALBUMS', conditions=dict(method=['GET']) )
    dispatcher.connect('spotify_post_album_name', '/:uid/albums/name/:name', controller=albumcon, action='POST_ALBUM_NAME', conditions=dict(method=['POST']) )
    dispatcher.connect('spotify_post_album', '/:uid/albums/:album_id', controller=albumcon, action='POST_ALBUM', conditions=dict(method=['POST']) )
    dispatcher.connect('spotify_put_album', '/:uid/albums/:album_id', controller=albumcon, action='PUT_ALBUM', conditions=dict(method=['PUT']) )
    dispatcher.connect('spotify_delete_album', '/:uid/albums/:album_id', controller=albumcon, action='DELETE_ALBUM_KEY', conditions=dict(method=['DELETE']) )
    dispatcher.connect('spotify_delete_albums', '/albums/', controller=albumcon, action='DELETE_ALBUMS', conditions=dict(method=['DELETE']) )

    dispatcher.connect('spotify_get_tracks', '/:uid/tracks/', controller=trackcon, action='GET_TRACKS', conditions=dict(method=['GET']) )
    dispatcher.connect('spotify_post_tracks', '/:uid/tracks/:track_id', controller=trackcon, action='POST_TRACK', conditions=dict(method=['POST']) )
    dispatcher.connect('spotify_post_track_name', '/:uid/tracks/name/:name', controller=trackcon, action='POST_TRACK_NAME', conditions=dict(method=['POST']) )
    dispatcher.connect('spotify_put_track', '/:uid/tracks/:track_id', controller=trackcon, action='PUT_TRACK', conditions=dict(method=['PUT']) )
    dispatcher.connect('spotify_delete_track', '/:uid/tracks/:track_id', controller=trackcon, action='DELETE_TRACK_KEY', conditions=dict(method=['DELETE']) )
    dispatcher.connect('spotify_delete_tracks', '/tracks/', controller=trackcon, action='DELETE_TRACKS', conditions=dict(method=['DELETE']) )

    dispatcher.connect('personality_by_id', '/:uid/personality', controller=personalitycon, action='music_personality', conditions=dict(method=['GET']) )

    #OPTIONS requests for dispatcher. 
    dispatcher.connect('artist_options','/:uid/artists/', controller=optionsController , action='OPTIONS' , conditions=dict(method=['OPTIONS']))
    dispatcher.connect('artist_id_options','/:uid/artists/:artist_id', controller=optionsController , action='OPTIONS' , conditions=dict(method=['OPTIONS']))
    
    dispatcher.connect('album_options','/:uid/albums/', controller=optionsController , action='OPTIONS' , conditions=dict(method=['OPTIONS']))
    dispatcher.connect('album_id_options','/:uid/albums/:album_id', controller=optionsController , action='OPTIONS' , conditions=dict(method=['OPTIONS']))
    
    dispatcher.connect('track_options','/:uid/tracks', controller=optionsController , action='OPTIONS' , conditions=dict(method=['OPTIONS']))
    dispatcher.connect('track_id_options','/:uid/tracks/:track_id', controller=optionsController , action='OPTIONS' , conditions=dict(method=['OPTIONS']))



    #TODO
    #configuration for server
    conf = {
            'global' : {
                    'server.socket_host' : 'YOUR-DOMAIN',
                    'server.socket_port' : YOUR-PORT,
                },
            '/' : { 'request.dispatch' : dispatcher,
		    'tools.CORS.on': True,
		    },
            }
    #update config
    cherrypy.config.update(conf)
    app = cherrypy.tree.mount(None, config=conf)
    cherrypy.quickstart(app)


if __name__ == '__main__':
    cherrypy.tools.CORS = cherrypy.Tool('before_finalize', CORS)
    start_service()
