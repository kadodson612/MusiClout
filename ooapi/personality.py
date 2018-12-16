import requests
import json
from collections import Counter
import ast


class Personality:
	def __init__(self, mdb):
		print("Initialize Personality Object")
		self.mdb = mdb
	def pers_pop(self):
		answer = {}
		answer['Personality'] = 'Pop: outgoing, but nervous. Try exploring some beachy EDM like Kygo or Odesza which will get you into less known artists like Griz. This will help you expand your music taste into less top 10 and more fun new music, making you a more likeable person, which will make you care less about what people think!'
		return json.dumps(answer)

	def pers_rock(self):
		answer = {}
		answer['Personality'] = 'Rock: easygoing, but selfish. Listen to some love songs and really tune into the lyrics. Ed Sheeran’s “Perfect” would be a good start. Listen to the pure love that people like Ed put into their songs, and think about how you are giving your love to others. Also, rock is not the only genre that uses real instruments! Listen to some jazz and heavy metal too, to get a feel for other genres with different uses of your favorite instruments. This musical diversity in your life will help you be more selfless and appreciate others’ loves for different genres.' 
		return json.dumps(answer)

	def pers_metal(self):
		answer = {}
		answer['Personality'] = 'Heavy metal: creative, but shy. Listen to some hip hop or drum & bass music. Then, feel the bass in your heart, stomach and soul. Move with the beat and you’ll start appreciating other genres more and their instruments and tempo. This new desire to listen to a very different genre will help you explore even more genres and appreciate all the different, beautiful sounds. Listening to stuff other than metal will make you more liked by others and therefore give you confidence to be a bit more outgoing!'
		return json.dumps(answer)

	def pers_jazz(self):
		answer = {}
		answer['Personality'] = 'Folk, Jazz, or Blues: deep thinkers, but unadventurous. Get out of your existential crisis or your awe-inspiring wonder for the world and go enjoy it. Listen to some Hip-Hop. Start with the artist, “Matt Citron.” He has the saxophone in many of his songs, still bringing that groovy vibe, but he will bring you current, relatable lyrics and a dope beat to connect you to other listeners and energize you to get out a little more.'
		return json.dumps(answer)

	def pers_hip(self):
		answer = {}
		answer['Personality'] = 'Hip Hop, Rap: extroverted, but annoying. Sit back and listen to some drum and bass. You’ll get the bumpin’ feel of Hip Hop, but you’ll be able to zone into the music a little more rather than shouting “Okay! Okay! Yeet! YEEET!” every ten seconds. This will bring you into yourself and help you with some soul-searching, pulling you away from the spotlight for a second so that you can find yourself before finding others.'
		return json.dumps(answer)

	def pers_country(self):
		answer = {}
		answer['Personality'] = 'Country: hardworking, but close-minded. Make a playlist that alternates rock and EDM. Between the lyrics, instrumentals and diverse sounds, your mind will open to the musical genius that isn’t country and you’ll never go back to country.' 
		return json.dumps(answer)

	def pers_classical(self):
		answer = {}
		answer['Personality'] = 'Classical: smart, but cocky. Take more musical risks and spice up your music taste by listening to EDM Funk, like Griz or The Floozies and feel that same love for sound that you do in classical, but with more of a groove than a snooze. If you enjoy the diversity of instruments in classical music, parallel that to the diversity of sound in new electronic songs. If you like the intensity, listen to a Deadmau5 song or live concert, his very long crescendos will have you at the edge of your seat feeling just like you’re in a story, like when  you listen to classical.'
		return json.dumps(answer)

	def pers_EDM(self):
		answer = {}
		answer['Personality'] = 'EDM: loving, but party too hard. Step away from the festivals a bit and listen to some classical music. You will love the story that classical tells in every song and it will allow you to step away from the party scene and back into a family-first vibe. Instantly your life will become more family-friendly. Now to bring the party back, but in a family-friendly way, listen to some groovy toons, like those by “Justice” and you will be able to enjoy what you have and the people around you, rather than going out to vibe with a bunch of wooks.' 
		return json.dumps(answer)


	def music_personality(self, uid):
		allGenres = []
		resp = {'result' : 'success'}
		# all artists of given user
		try:
			for key, values in self.mdb.artists[uid].items():
				value = ast.literal_eval(values["genres"])
				print("Value is " + str(value))
				
				if not len(value):
					continue
				if len(value) == 1:
					allGenres.append(value[0])
					continue
				for i in value:
					allGenres.append(i)
			# once I have big list of all genres of user's artists,
			# count up genres in histogram
			histo = Counter(allGenres)
			your_genre = histo.most_common(1)

			# Make your top genre all lowercase
			g = your_genre[0][0].lower()
			if 'pop' in g:
				return self.pers_pop()
			elif 'rock' in g:
				return self.pers_rock()
			elif 'metal' in g:
				return self.pers_metal()
			elif 'jazz' in g or 'blues' in g or 'folk' in g:
				return self.pers_jazz()
			elif 'hip' in g or 'rap' in g:
				return self.pers_hip() 
			elif 'country' in g:
				return self.pers_country()
			elif 'classical' in g:
				return self.pers_classical()
			elif 'electronic' in g or 'edm' in g:
				return self.pers_EDM()
			elif your_genre == '':
				resp['Personality'] = 'Add some favorite artists to your Library!'
				return json.dumps(resp)
			else:
				resp['Personality'] = 'You are a jack of all trades!'
				return json.dumps(resp)
		except Exception as ex:
			resp['result'] = 'error'
			resp['message'] = str(ex)

		return json.dumps(resp)


	
