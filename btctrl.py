#!/usr/bin/python3

from evdev import InputDevice, categorize, ecodes
import os
import urllib.parse

keyboard = InputDevice('/dev/input/event0')

shift=False
ctrl=False
caps=False


print(keyboard)

ip_address = "localhost"

with open('/etc/tv-keyboard-ctrl/found_ip') as f:
	ip_address = f.readline()[:-1]

def nonlitaction(term):
	os.system("curl -d '' \"http://" + ip_address + ":8060/keypress/" + term + "\"")

def action(term):
	if caps:
		os.system("curl -d '' \"http://" + ip_address + ":8060/keypress/Lit_" + urlencode(term.upper()) + "\"")
	else:
		os.system("curl -d '' \"http://" + ip_address + ":8060/keypress/Lit_" + urlencode(term) + "\"")

def urlencode(term):
	return urllib.parse.quote(term)

for event in keyboard.read_loop():
	if event.type == ecodes.EV_KEY:
		if event.value == 1:
			'''if event.code == 42: #leftshift
				shift=True
			if event.code == 54: #rightshift
				shift=True
			if event.code == 58:
				if caps:
					caps=False
				else:
					caps=True
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
			if event.code == 41:
				if shift:
					action("~")
				else:
					action("`")
			if event.code == 2:
				if shift:
					action("!")
				else:
					action("1")
			if event.code == 3:
				if shift:
					action("@")
				else:
					action("2")
			if event.code == 4:
				if shift:
					action("#")
				else:
					action("3")
			if event.code == 5:
				if shift:
					action("$")
				else:
					action("4")
			if event.code == 6:
				if shift:
					action("%")
				else:
					action("5")
			if event.code == 7:
				if shift:
					action("^")
				else:
					action("6")
			if event.code == 8:
				if shift:
					action("&")
				else:
					action("7")
			if event.code == 9:
				if shift:
					action("*")
				else:
					action("8")
			if event.code == 10:
				if shift:
					action("(")
				else:
					action("9")
			if event.code == 11:
				if shift:
					action(")")
				else:
					action("0")
			if event.code == 12:
				if shift:
					action("_")
				else:
					action("-")
			if event.code == 13:
				if shift:
					action("+")
				else:
					action("=")
			if event.code == 26:
				if shift:
					action("[")
				else:
					action("{")
			if event.code == 27:
				if shift:
					action("]")
				else:
					action("}")
			if event.code == 43:
				if shift:
					action("|")
				else:
					action("\\")
			if event.code == 39:
				if shift:
					action(":")
				else:
					action(";")
			if event.code == 40:
				if shift:
					action("\"")
				else:
					action("'")
			if event.code == 51:
				if shift:
					action("<")
				else:
					action(",")
			if event.code == 52:
				if shift:
					action(">")
				else:
					action(".")
			if event.code == 53:
				if shift:
					action("?")
				else:
					action("/")
			if event.code == 57:
				action(" ")
			if event.code == 105:
				nonlitaction("Left")
			if event.code == 106:
				nonlitaction("Right")
			if event.code == 103:
				nonlitaction("Up")
			if event.code == 108:
				nonlitaction("Down")
			if event.code == 14:
				nonlitaction("Backspace")
			if event.code == 28:
				nonlitaction("Enter")'''
			print(event.code)
		if event.value == 0:
			if event.code == 42: #leftshift
				shift=False
			if event.code == 54: #rightshift
				shift=False
