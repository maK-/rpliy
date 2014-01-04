#!/usr/bin/python
#-*- coding: iso-8859-15 -*-
import web
import os, sys, time, re
from db import Database
from random import randint
from ID3 import *
import pygame.mixer as mixer

#Defining Accessible Web Addresses
urls = ('/','Index', '/favicon.ico','Fav', '/Search','Search', '/css','Style', '/rpi.png','Rpi', '/script.js', 'Script', 
			'/playlist/add/(.*)', 'Playlist_add', '/jQuery.js', 'JQuery', '/playlist', 'Playlist', '/cmd/(.*)', 'Command',
			'/empty', 'Empty')

#Overwriting the run function to use a different port.
#Display server host IP address/port combo.
class rpliyWeb(web.application):
	def run(self, host, port=8080, *middleware):
		func = self.wsgifunc(*middleware)
		print('\nrpliy - Raspberry Pi Python Player'+
			'\n------------------------------\n')
		return web.httpserver.runsimple(func, (host, port))

#Handles Get request to server root.
class Index:
	def GET(self):
		main = web.template.frender('templates/main.html')
		return main(str(host),str(port))	

class Command:
	def GET(self, cmd):
		mixer.init(44100)
		mixer.music.set_volume(1.0)
		p = paused
	#I feel it would have been too robust or unsuitable
	#to use a Command pattern in this scenario
		if(cmd == "play"):
			songloc = list(mydb.getPlaylist())
			if(songloc):
				mixer.music.load(songloc[0].loc)
				mixer.music.play(0)

		if(cmd == "pause"):
			if(p):
				mixer.music.unpause()
				p = False
			else:
				mixer.music.pause()
				p = True
		if(cmd == "next"):
			delfirst = mydb.delFirstPl()
			nextsong = list(mydb.getPlaylist())
			if(nextsong):
				mixer.music.load(nextsong[0].loc)
				mixer.music.play(0)
		if(cmd == "stop"):
			mixer.music.stop()
		return cmd

#Empty the playlist
class Empty:
	def GET(self):
		i = mydb.emptyDB()
		return 'Playlist & Database Emptied'

#Find songs or artists.
class Search:
	def GET(self):	
		user_data = web.input()
		z = []
		blah = True
		try:
			libname = mydb.libs()
			z = list(mydb.Search(user_data.s))
		except AttributeError, e:
			data = '<h2>No Search terms provided!</h2>'
			blah = False
		if(blah):
			data = '<br /><table><tr><th>ID</th><th>Title</th><th>Artist</th><th>Album</th><th></th></tr>'
		for i in range(0, len(z)):
			data += '<tr id="entry'+str(z[i].id)+'"><td>'+str(z[i].id)+'</td><td>'+str(z[i].name)+'</td>'
			data += '<td>'+str(z[i].artist)+'</td><td>'+str(z[i].album)+'</td>'
			data += '<td><button onclick="fireEvent('+str(z[i].id)+');">ADD</button></td></tr>'
		data += '</table>'

		search = web.template.frender('templates/search.html')
		return search(str(host),str(port), str(data))

class Playlist_add:
	def GET(self, song_id):
		addpl = mydb.addPlaylist(song_id)
		return addpl

#view Playlist and controls
class Playlist:
	def GET(self):
		playlist = []
		isdata = True
		try:
			sizeof = mydb.plsize()
		except AttributeError, e:
			data = "<h2>Nothing in Playlist!</h2>"
			isdata = False
		if(isdata):
			data = '<h2>Number of entries in playlist: '+str(sizeof)+' </h2>'
			data += '<table><tr><td><button onclick="play()">Play</button></td>';
			data += '<td><button onclick="pause()">Pause</button></td>';
			data += '<td><button onclick="next()">Next</button></td>';
			data += '<td><button onclick="stop()">Stop</button></td>';
			data += '</tr></table>'
		play = web.template.frender('templates/playlist.html')
		return play(str(host), str(port), str(data))

#Display the favicon
class Fav:
	def GET(self):
		f = open("static/favicon.ico", 'rb') 
		favicon = f.read()
		f.close()
		return favicon		

#Style sheet
class Style:
	def GET(self):
		f = open("static/style.css", "rb")
		css = f.read()
		f.close()
		return css

#Javascript file containg js functions
class Script:
	def GET(self):
		f = open("static/script.js", 'rb')
		js = f.read()
		f.close()
		return js

#Jquery
class JQuery:
	def GET(self):
		f = open("static/jQuery.js")
		jq = f.read()
		f.close()
		return jq 

#Logo
class Rpi:
	def GET(self):
		f = open("static/rpi.png")
		img = f.read()
		f.close()
		return img
		
#---------------Main Program----------------
if __name__ == "__main__":

	def subchars(thestring):
		s = re.sub('[^0-9a-zA-Z]+', ' ', thestring)
		return s
	
	#Find all mp3 files on a specified device
	def findmp3(media):
		cmd = 'find '+media+' -type f -iname *.mp3'
		z = list(os.popen(cmd))
		return z
	
	#print header.
	def pheader():
		print("----------------------------------------------------")
		print("\033[032m    .~~.   .~~.")
		print("   '. \ ' ' / .'\033[031m")
		print("    .~ .~~~..~.    \033[037m              |_)       \033[031m")
		print("   : .~.'~'.~. :   \033[037m    __| __ \  | | |   |\033[031m")
		print("  ~ (   ) (   ) ~  \033[037m   |    |   | | | |   | \033[031m")
		print(" ( : '~'.~.'~' : ) \033[037m  _|    .__/ _|_|\__, | \033[031m")
		print("  ~ .~ (   ) ~. ~  \033[037m       _|        ____/  \033[031m")
		print("   (  : '~' :  )   \033[037m Raspberry Pi Python Player\033[031m")
		print("    '~ .~~~. ~'")
		print("        '~'\033[0m")
		print("----------------------------------------------------\n")
		return 0


	#Take single argument (location of USB or music folder)
	isq = False
	try:
		mp3s_loc = sys.argv[1]
		if(mp3s_loc == '-q'):
			isq = True
	except IndexError, e:
		if(isq == False):
			pheader()
			print("\033[31mError:\033[0m Folder containing mp3's not provided...")
			print("Run \033[037m./rpliy $folder\033[0m to build mp3 list...")
			print("Use -q flag to use default settings.\n")
			exit()
		else:
			print("Loading Default settings...\n")
	
	#---------------------------------------------------
	# Start Main Program
	#---------------------------------------------------
	pheader() #print header
	time.sleep(1)

	#Create Mysql Database
	mydb = Database('localhost,root,p00p,mak')
	mydb.Create_DB()

	#identifiable info of library	
	if(isq == False):
		mp3s = findmp3(mp3s_loc)
		libname = raw_input("Choose a name for your imported library: ")
		data = {}
		for i in mp3s:
			print(i)
			id3 = ID3(i.strip())
			#Inserting id3 info into database.
			try:
				if(id3['ARTIST']):
					data['artist'] = subchars(str(id3['ARTIST']))
				else:	data['artist'] = 'Undefined'

				if(id3['ALBUM']):
					data['album'] = subchars(str(id3['ALBUM']))
				else:	data['album'] = 'Undefined'
			
				if(id3['TITLE']):
					data['name'] = subchars(str(id3['TITLE']))
				else:	data['name'] = 'Undefined'
			
				if(libname):
					data['libname'] = subchars(str(libname))
				else:	data['libname'] = 'None'
			
				data['location'] = str(i.strip())
		
				store = mydb.Store_mp3(data)
			except KeyError, e:
				continue
			
		print ('Total Songs: '+str(len(mp3s)))
		print ('Songs added to the '+libname+' library')



	#return a list of mp3 files.
	port = 80
	host = '192.168.1.1'	
	paused = False
	
	#Run the web app
	rpi = rpliyWeb(urls, globals())
	rpi.run(host,port)
	print '\n Goodbye!'
