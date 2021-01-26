import random 
import curses 
import os
import subprocess
from dependencies import start_game
# to be sure that path is actually a home dir for max collection

start_game()
# Start playinh the game
s = curses.initscr() #initializing the screen
curses.curs_set(0)
sh, sw = s.getmaxyx()
w = curses.newwin(sh, sw, 0, 0) #creating a new window with the strarting at (0,0)
w.keypad(1)
w.timeout(100)

#making the snake starting point
snk_x = sw/4
snk_y = sh/2
#making the snake parts
snake = [
	[snk_y,snk_x],
	[snk_y,snk_x-1],
	[snk_y,snk_x-2]
]

#food 
food = [sh/2,sw/2] # initililizing the food at the middle
w.addch( int(food[0]), int(food[1]), curses.ACS_PI) # adding to the screen/window with the character PI

key = curses.KEY_RIGHT # DEFAULT STATRING OF THE SNAKE

while True:
	next_key = w.getch()
	key = key if next_key == -1 else next_key
	#continue in same direction if no key else use the next key	
	#conditon of loosing the game
	if snake[0][0] in [0,sh] or snake[0][1] in [0,sw] or snake[0] in snake[1:]:
		curses.endwin()
		# quit()
		# os.remove("filename")

	
	new_head = [snake[0][0], snake[0][1]]	
	
	if key == curses.KEY_DOWN:
		new_head[0] +=1
	if key == curses.KEY_UP:
		new_head[0] -=1
	if key == curses.KEY_LEFT:
		new_head[1] -=1	
	if key == curses.KEY_RIGHT:
		new_head[1] +=1
		
	snake.insert(0,new_head)
	
	if snake[0] ==food:
		
		food = None
		while food is None:
			nf = [
				random.randint(1,sh-1),
				random.randint(1,sw-1)
				]
				
			food = nf if nf not in snake else None
		
		w.addch(food[0], food[1], curses.ACS_PI)
		
	else:
		tail = snake.pop()
		w.addch(int(tail[0]), int(tail[1]), ' ')
	
	w.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)
	