from pynput import keyboard
from time import sleep

p1_move = False
p2_move = False

def press_callback(key):
	if key.char == "q":
		return False
	global p1_move,p2_move
	if not p1_move:
		if key.char == 'a':
			p1_move = 'rock'
		elif key.char == 's':
			p1_move = 'paper'
		elif key.char == 'd':
			p1_move = 'scissors'
	if not p2_move:
		if key.char == 'j':
			p2_move = 'rock'
		elif key.char == 'k':
			p2_move = 'paper'
		elif key.char == 'l':
			p2_move = 'scissors'
	print("\n"*50)
	if p1_move and p2_move:
		return False

def play():
	global p1_move,p2_move
	p1_move = False
	p2_move = False
	l = keyboard.Listener(on_press=press_callback)
	l.start()
	print("\n\n\nReady!")
	print()
	l.join()
	print(f"\n\n\nPlayer 1 played {p1_move} and Player 2 played {p2_move}")


while True:
	play()
