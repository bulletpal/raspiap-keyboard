import os

devices = os.popen("bluetoothctl info 34:88:5D:81:35:E8").read()

print(devices.find("Connected:"))
