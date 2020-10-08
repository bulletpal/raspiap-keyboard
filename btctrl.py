from evdev import InputDevice, categorize, ecodes
import os

keyboard = InputDevice('/dev/input/event0')

shift=False

print(keyboard)

ip_address = "localhost"

with open('/etc/tv-keyboard-ctrl/found_ip') as f:
	ip_address = f.readline()[:-1]

def action(term):
	os.system("curl -d '' \"http://" + ip_address + ":8060/keypress/Lit_" + term + "\"")

for event in keyboard.read_loop():
	if event.type == ecodes.EV_KEY:
		if event.value == 1:
			if event.code == 42:
				shift=True
			if event.code == 54:
				shift=True
			if event.code == 16:
				if shift:
					action("Q")
				else:
					action("q")
			if event.code == 17:
				if shift:
					action("W")
				else:
					action("w")
			if event.code == 18:
				if shift:
					action("E")
				else:
					action("e")
			if event.code == 19:
				if shift:
					action("R")
				else:
					action("r")
			if event.code == 20:
				if shift:
					action("T")
				else:
					action("t")
			if event.code == 21:
				if shift:
					action("Y")
				else:
					action("y")
			if event.code == 22:
				if shift:
					action("U")
				else:
					action("u")
			if event.code == 23:
				if shift:
					action("I")
				else:
					action("i")
			if event.code == 24:
				if shift:
					action("O")
				else:
					action("o")
			if event.code == 25:
				if shift:
					action("P")
				else:
					action("p")
			if event.code == 30:
				if shift:
					action("A")
				else:
					action("a")
			if event.code == 31:
				if shift:
					action("S")
				else:
					action("s")
			if event.code == 32:
				if shift:
					action("D")
				else:
					action("d")
			if event.code == 33:
				if shift:
					action("F")
				else:
					action("f")
			if event.code == 34:
				if shift:
					action("G")
				else:
					action("g")
			if event.code == 35:
				if shift:
					action("H")
				else: 
					action("h")
			if event.code == 36:
				if shift:
					action("J")
				else:
					action("j")
			if event.code == 37:
				if shift:
					action("K")
				else:
					action("k")
			if event.code == 38:
				if shift:
					action("L")
				else:
					action("l")
			if event.code == 44:
				if shift:
					action("Z")
				else:
					action("z")
			if event.code == 45:
				if shift:
					action("X")
				else:
					action("x")
			if event.code == 46:
				if shift:
					action("C")
				else:
					action("c")
			if event.code == 47:
				if shift:
					action("V")
				else:
					action("v")
			if event.code == 48:
				if shift:
					action("B")
				else:
					action("b")
			if event.code == 49:
				if shift:
					action("N")
				else:
					action("n")
			if event.code == 50:
				if shift:
					action("M")
				else:
					action("m")
		if event.value == 0:
			if event.code == 42:
				shift=False
			if event.code == 54:
				shift=False
