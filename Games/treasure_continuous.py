import random
from pynput import keyboard

size = 15
player = "Y"
blank = " "
treasure_symbol = "H"

def print_board(board):
	for row in board:
		print(row)

def move(coordinates, direction, size):
	if direction == "a" and coordinates[1] >0:
		coordinates[1]-=1
	elif direction == "d" and coordinates[1] < size-1:
		coordinates[1]+=1
	elif direction == "s" and coordinates[0] < size - 1:
		coordinates[0]+=1
	elif direction == "w" and coordinates[0] > 0:
		coordinates[0]-=1
	elif direction == "":
		pass


def show(a_board,a_coordinates):
	print()
	a_board[a_coordinates[0]][a_coordinates[1]]=player
	print_board(a_board)
	print("Enter a direction (asdw)")
	a_board[a_coordinates[0]][a_coordinates[1]]=blank

def play_continuous():
	playing = True
	coordinates = [0,0]
	board = [[blank]*size for i in range(size)]
	board[random.randint(1,size-1)][random.randint(1,size-1)]=treasure_symbol
	print("Find the treasure! It is marked {}".format(treasure_symbol))


	def on_press(key):
		try:
			k = key.char
		except:
			return False
		if k not in ['a','s','d','w',""]:
			print("KEY NOT IN SET")
			return False
		direction = k
		move(coordinates,direction,size)
		if board[coordinates[0]][coordinates[1]] == treasure_symbol:
			print_board(board)
			print("You win!\n")
			return False
		show(board,coordinates)

	show(board,coordinates)
	with keyboard.Listener(on_press=on_press) as lis:
		lis.join() # no this if main thread is polling self.keys
	print("YOU WIN!")


while True:
	play_continuous()
