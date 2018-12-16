import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import requests
import json
#Kelly Dodson

class MusicQT(QMainWindow):
	def __init__(self):
		super(MusicQT, self).__init__()
		self.setWindowTitle("Music Personality")
		self.central = MusicCentral(parent = self)
		self.central.showGUI()
		self.setCentralWidget(self.central)
		self.filemenu = self.menuBar().addMenu("File")
		self.usermenu = self.menuBar().addMenu("User")
		fileExitAction = QAction("Exit", self)
		profileAction = QAction("View Profile", self)
		setUserAction = QAction("Set User", self)
		setUserArtist = QAction("Add Favorite Artists", self)
		setUserTrack = QAction("Set Favorite Songs", self)
		setUserAlbum = QAction("Set Favorite Albums", self)
		self.filemenu.addAction(fileExitAction)
		self.usermenu.addAction(profileAction)
		self.usermenu.addAction(setUserAction)
		self.usermenu.addAction(setUserArtist)
		self.usermenu.addAction(setUserTrack)
		self.usermenu.addAction(setUserAlbum)
		self.connect(fileExitAction, SIGNAL("triggered()"), self.exit_program)
		self.connect(profileAction, SIGNAL("triggered()"), self.profile)
		self.connect(setUserAction, SIGNAL("triggered()"), self.user)
		self.connect(setUserArtist, SIGNAL("triggered()"), self.artist)
		self.connect(setUserTrack, SIGNAL("triggered()"), self.track)
		self.connect(setUserAlbum, SIGNAL("triggered()"), self.album)

		#Style
		self.setStyleSheet(open("extracredit.qss", "r").read())
		self.setAutoFillBackground(True)

	
	def exit_program(self):
		app.quit()

	def user(self):
		text, ok = QInputDialog.getText(self, 'Input Dialog', 'User ID:')
		if ok:
			try:
				str(text)

			except Exception as e:
				print("Try Again. This is not a valid username.")

			self.central.uid = str(text)
			self.central.getUser()
			self.central.getPersonality()
			print("Changed uid to: " + str(text))

	def artist(self):
		text, ok = QInputDialog.getText(self, 'Input Dialog', 'New fave artist Spotify ID:')
		success = False
		if ok:
			try:
				str(text)

			except Exception as e:
				print("Try Again. This is not a valid ID.")
			
			r1 = requests.post(self.central.SITE_URL + str(self.central.uid) + '/artists/' + str(text))
			resp1 = json.loads(r1.content.decode())
			if resp1["result"] == "success":
				print("Added new artist")
				self.central.getUser()
				self.central.getPersonality()
				success = True

			if success:
				choice = QMessageBox.question(self, 'Success',"1 new favorite artist was added.", QMessageBox.Ok)
				if choice == QMessageBox.Ok:
					pass
			else: 
				choice = QMessageBox.question(self, 'Error',"There was an error adding the artist. Please try again.", QMessageBox.Ok)
				if choice == QMessageBox.Ok:
					pass

	def track(self):
		text, ok = QInputDialog.getText(self, 'Input Dialog', 'New fave Track Spotify ID:')
		success = False
		if ok:
			try:
				str(text)

			except Exception as e:
				print("Try Again. This is not a valid ID.")
			
			r1 = requests.post(self.central.SITE_URL + str(self.central.uid) + '/tracks/' + str(text))
			resp1 = json.loads(r1.content.decode())
			if resp1["result"] == "success":
				print("Added new track")
				self.central.getUser()
				self.central.getPersonality()
				success = True

			if success:
				choice = QMessageBox.question(self, 'Success',"1 new favorite track was added.", QMessageBox.Ok)
				if choice == QMessageBox.Ok:
					pass
			else: 
				choice = QMessageBox.question(self, 'Error',"There was an error adding the track. Please try again.", QMessageBox.Ok)
				if choice == QMessageBox.Ok:
					pass

	def album(self):
		text, ok = QInputDialog.getText(self, 'Input Dialog', 'New fave album Spotify ID:')
		success = False
		if ok:
			try:
				str(text)

			except Exception as e:
				print("Try Again. This is not a valid ID.")
			
			r1 = requests.post(self.central.SITE_URL + str(self.central.uid) + '/albums/' + str(text))
			resp1 = json.loads(r1.content.decode())
			if resp1["result"] == "success":
				print("Added new album")
				self.central.getUser()
				self.central.getPersonality()
				success = True

			if success:
				choice = QMessageBox.question(self, 'Success',"1 new favorite album was added.", QMessageBox.Ok)
				if choice == QMessageBox.Ok:
					pass
			else: 
				choice = QMessageBox.question(self, 'Error',"There was an error adding the album. Please try again.", QMessageBox.Ok)
				if choice == QMessageBox.Ok:
					pass


	def profile(self):
		print("User Profile")
		r1 = requests.get(self.central.SITE_URL + str(self.central.uid) + '/artists/')
		r2 = requests.get(self.central.SITE_URL + str(self.central.uid) + '/albums/')
		r3 = requests.get(self.central.SITE_URL + str(self.central.uid) + '/tracks/')
		resp1 = json.loads(r1.content.decode())
		resp2 = json.loads(r2.content.decode())
		resp3 = json.loads(r3.content.decode())
		msg = QMessageBox()

		fave_artists = []
		fave_albums = []
		fave_tracks = []
			
		for k,v in resp1["entries"].items():
			fave_artists.append(v["name"])
		for k,v in resp2["entries"].items():
			fave_albums.append(v["name"])
		for k,v in resp3["entries"].items():
			fave_tracks.append(v["name"])
			
		fave_artists = fave_artists[0:5]
		fave_artist_string = ','.join(a for a in fave_artists)

		fave_albums = fave_albums[0:5]
		fave_album_string = ','.join(a for a in fave_albums)

		fave_tracks = fave_tracks[0:5]
		fave_track_string = ','.join(a for a in fave_tracks)	

		msg.setText("User Profile:\nUsername: " + str(self.central.uid) + "\nArtists: " + fave_artist_string  + "\nAlbums: " + fave_album_string + "\nTracks: " + fave_track_string)
		retval = msg.exec_()

	
class MusicCentral(QWidget):
	def __init__(self, parent=None):
		super(MusicCentral, self).__init__(parent)
		self.uid = "defaultUser"
		self.userLabel = QLabel()
		self.personalityLabel = QLabel()
		self.personalityLabel.setWordWrap(True)    
		self.SITE_URL = 'http://student04.cse.nd.edu:52052/'

	def getPersonality(self):
		r = requests.get(self.SITE_URL + str(self.uid) + '/personality')
		resp = json.loads(r.content.decode())
		self.personality = str(resp['Personality'])
		self.personalityLabel.setText(self.personality)

	def getUser(self):
		self.userLabel.setText(str(self.uid))

	def showGUI(self):
		self.getUser()
		self.getPersonality()
		self.verticalLayout = QBoxLayout(2)
		self.personalityLabel.setAlignment(Qt.AlignCenter)
		self.userLabel.setAlignment(Qt.AlignCenter)
		self.pic = QLabel(self)
		self.pic.setPixmap(QPixmap("./images/person.png").scaled(100, 100,Qt.KeepAspectRatio, Qt.FastTransformation))
		self.pic.show()
		self.pic.setAlignment(Qt.AlignCenter)
		#adding a visual button
		self.exitbutton = QPushButton("Exit")

		layout = QHBoxLayout() # layout is not a member
		layout.addWidget(self.personalityLabel)
		self.verticalLayout.addWidget(self.userLabel)
		self.verticalLayout.addWidget(self.pic)
		self.verticalLayout.addWidget(self.personalityLabel)
		self.verticalLayout.addLayout(layout)
		self.setLayout(self.verticalLayout)
		# adding functionality for button
		#              agent                event           event handler/SLOT
		self.connect(self.exitbutton, SIGNAL("clicked()"), self.exit_program)

	def exit_program(self):
		app.quit()


if __name__ == "__main__":
	app = QApplication(sys.argv)
	gui = MusicQT()
	gui.show()
	sys.exit(app.exec_())

