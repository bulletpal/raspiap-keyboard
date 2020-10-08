import os

devices = os.popen("bluetoothctl devices").read()

print(devices)
