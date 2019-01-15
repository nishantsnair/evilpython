from random import randint

def print_board(board,frame):
	print()
	print(frame*(len(board[0])+2))
	for row in board:
		print(frame + "".join(row) + frame)
	print(frame*(len(board[0])+2))

def mark(board,coordinates,symbol):
	board[coordinates[0]][coordinates[1]]=symbol

def place_treasure(board,body,treasure_symbol):
	treasure = body[0]
	size = len(board)
	if len(body) >= size*size:
		return
	while treasure in body:
		treasure = [randint(0,size-1),randint(0,size-1)]
	mark(board,treasure,treasure_symbol)
	return treasure

def valid_move(coordinates, direction, size):
	if direction == "a" and coordinates[1] > 0:
		coordinates[1]-=1
	elif direction == "d" and coordinates[1] < size-1:
		coordinates[1]+=1
	elif direction == "s" and coordinates[0] < size - 1:
		coordinates[0]+=1
	elif direction == "w" and coordinates[0] > 0:
		coordinates[0]-=1
	else:
		return False
	return True


def play(size=6,player="0",blank=" ",treasure_symbol="X",frame="#"):
	playing = True
	board = [[blank]*size for i in range(size)]
	body = [[randint(0,size-1),randint(0,size-1)]]
	treasure = place_treasure(board,body,treasure_symbol)

	print("Find the treasure! It is marked {}".format(treasure_symbol))

	while playing:
		head = body[0][:]
		tail = body.pop()
		mark(board,head,player)
		print_board(board,frame=frame)


		print("Enter a direction (asdw) then ENTER")
		direction = input()

		if not valid_move(head,direction,size) or (head in body):
			playing = False
		body = [head] + body

		if head == treasure:
			body = body + [tail]
			treasure = place_treasure(board,body,treasure_symbol)
		else:
			mark(board,tail,blank)

	if len(body) == size*size:
		print("YOU WIN!")
	else:
		print("YOU LOSE!")


play()
