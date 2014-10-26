#!/usr/bin/env python

import os

os.system("wget -O /tmp/jkl http://internet.tri.co.id/")
f= open ("/tmp/jkl","r")
data = f.read()
f.close()


message = "Kuota 3 tersisa "+ data[ data.find("/dataImg/getRadius?remain="): data[data.find("/dataImg/getRadius?remain="):].find(">")+data.find("/dataImg/getRadius?remain=")][data[ data.find("/dataImg/getRadius?remain="): data[data.find("/dataImg/getRadius?remain="):].find(">")+data.find("/dataImg/getRadius?remain=")].find("=")+1:-1] +" MB"

os.system("notify-send \"Makin info \" \" "+ message +" \" ")
