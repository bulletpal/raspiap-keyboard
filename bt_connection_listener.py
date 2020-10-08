import os
import time

connected = False
lastconnected = False

while 1:
	device = os.popen("bluetoothctl info 34:88:5D:81:35:E8").read()
	linenumber = device.find("Connected:")
	if device[linenumber+11:linenumber+13] == "no":
		connected = False
	else:
		connected = True
	if lastconnected == False and connected == True:
		os.system("python3 /etc/tv-keyboard-ctrl/btctrl.py")
	lastconnected = connected
	time.sleep(1)
