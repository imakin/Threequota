#!/usr/bin/env python

import os
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
	data = f.read()
	f.close()

	if data[ data.find("/dataImg/getRadius?remain="): data[data.find("/dataImg/getRadius?remain="):].find(">")+data.find("/dataImg/getRadius?remain=")][data[ data.find("/dataImg/getRadius?remain="): data[data.find("/dataImg/getRadius?remain="):].find(">")+data.find("/dataImg/getRadius?remain=")].find("=")+1:-1]=="":
		print "error while fetching data"
		
	message = "Quota left: "+ data[ data.find("/dataImg/getRadius?remain="): data[data.find("/dataImg/getRadius?remain="):].find(">")+data.find("/dataImg/getRadius?remain=")][data[ data.find("/dataImg/getRadius?remain="): data[data.find("/dataImg/getRadius?remain="):].find(">")+data.find("/dataImg/getRadius?remain=")].find("=")+1:-1] +" MB"

	if (usebuilder==1):
		main = threequota()
		gtk.main()
	else:
		os.system("notify-send \"Info \" \" "+ message +" \" ")
