import web, string, os

#Comment out the following line for more detailed debug messages.
web.config.debug = False


#Database class allows easier control of the data
#I don't expect this to read much as it was rushed and
#doesn't adhere much to the specs (RE: Avoid database type applications)
class Database:

	#On initializing replace default values
	def __init__(self, db_data):
		self.db_data = db_data
		self.db_type = 'mysql'
		self.data = None
		self.db = None
	
	#It supports both Mysql
	def Create_DB(self):
		try:
			self.data = string.split(self.db_data, ',')
			self.db = web.database(dbn=self.db_type, host=self.data[0],user=self.data[1], pw=self.data[2], db=self.data[3])
			#Creating table to store mp3s and playlist data
			self.db.query('CREATE TABLE rpi (id INT(10) NOT NULL PRIMARY KEY AUTO_INCREMENT, libname VARCHAR(100), artist VARCHAR(100), album VARCHAR(100), name VARCHAR(100), location VARCHAR(200));')
			self.db.query('CREATE TABLE playlist (id INT(10) NOT NULL PRIMARY KEY AUTO_INCREMENT, sid INT(10), loc VARCHAR(200));')
		except Exception, e:
			#print (e)
			print ('\033[31mNote:Problem creating MySQL Database or table already Exists.\033[0m')
		
	#Stores and mp3 metadata 
	def Store_mp3(self,data):
		self.db.insert('rpi',libname=data['libname'],artist=data['artist'],album=data['album'], 
				name=data['name'], location=data['location'])
			
	#Returns the size user Table.
	def dbsize(self):
		size = self.db.query('SELECT COUNT(id) as size from rpi')
		return size[0].size

	#returns the size of the playlist
	def plsize(self):
		size = self.db.query('SELECT COUNT(id) as size from playlist')
		return size[0].size

	#search library for music
	def Search(self, s):
		vicid = dict(seo=s+'%')
		thelist = self.db.select('rpi', vicid, where="artist like $seo OR album like $seo OR name like $seo")
		return thelist

	#retrive location of a song
	def getLoc(self, sid):
		s = dict(songid = sid)
		locations = self.db.select('rpi', s, what="location,id", where="id = $songid")
		return locations	

	#Add to playlist
	def addPlaylist(self, sid):
		s = list(self.getLoc(sid))
		self.db.insert('playlist', loc=s[0].location, sid=s[0].id)
		return "Successful"

	#get Playlist
	def getPlaylist(self):
		playlist = self.db.query("SELECT * FROM playlist order by id LIMIT 1")
		return playlist

	#Get library names
	def libs(self):
		liblist = self.db.query("SELECT libname from rpi group by libname ASC;")
		return liblist

	#drop both databases
	def emptyDB(self):
		self.db.query('DROP TABLE rpi;')
		self.db.query('DROP TABLE playlist')
		return ""

	#delete first entry in playlist
	def delFirstPl(self):
		self.db.query('DELETE from playlist order by id LIMIT 1')
		return ""
