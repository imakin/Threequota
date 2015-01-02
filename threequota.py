#!/usr/bin/env python

import os
import re

useurllib = 1
usebuilder = 1
message = ""

try:
	import urllib
except:
	useurllib = 0
try:
	import gtk
	class threequota:

		def on_window_destroy(self, menuitem, data=None):
			gtk.main_quit()
			
		def on_window_activate_default(self, menuitem, data=None):
			print "test window activate default triggered"
		
		def on_button_ok_clicked(self, menuitem, data=None):
			gtk.main_quit()
			
		def __init__(self):
			self.gladefile = "builder.glade"
			self.builder = gtk.Builder()
			self.builder.add_from_file(self.gladefile)
			self.builder.connect_signals(self)
			self.window = self.builder.get_object("window")
			self.infotext = self.builder.get_object("tulisan")
			
			self.infotext.set_text(message)
			self.window.show()


except:
	usebuilder = 0

if __name__ == "__main__":
	f=open("/dev/null","r")
	data = ""
	try:
		if useurllib==1:
			f = urllib.urlopen("http://internet.tri.co.id")
		else:
			os.system("wget -O /tmp/jkl http://internet.tri.co.id/")
			f= open ("/tmp/jkl","r")
	except:
		print "error while fetching data"
		exit(1) #exit if error

	data = f.read()
	f.close()

	#ultra simple regex, 
	#bite and suck number/repeated digit (\d+) after "remain=", 
	kuota = re.findall(r'remain=(\d+)', data)
	
	if len(kuota)==0:
		print "Error while extracting data, perhaps your cell provider isn't Three"
		exit(1) #exit if error
	
	#kuota will contain regular quota and (maybe) kenyang download
	#reverse and opo, one by one
	kuota.reverse()
	reguler = kuota.pop() 	
	message = 'Quota left: \nRegular: ' + reguler + 'MB'
	
	if len(kuota) > 0:
		kenyang = kuota.pop()
		message += '\nKenyang Download: ' + kenyang + 'MB'

	if (usebuilder==1):
		main = threequota()
		gtk.main()
	else:
		os.system("notify-send \"Info \" \" "+ message +" \" ")
