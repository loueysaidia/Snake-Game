#import the important modules
import random
import curses
#////////////////////////////////////////////////////
# initilaze the screen

screen = curses.initscr()

#////////////////////////////////////////////////////
#set the visibility of the cursor false\

curses.curs_set(0)

#////////////////////////////////////////////////////
#take the max hieght and width of the screen

screen_hieght,screen_width = screen.getmaxyx()

#/////////////////////////////////////////////////////
#initilaze the window with the screen height and width

window = curses.newwin(screen_hieght,screen_width,0,0)

#////////////////////////////////////////////////////
#allow window to receive from the keyboard

window.keypad(True)

#////////////////////////////////////////////////////
#set the delay for updating the screen

window.timeout(100)

#set the coordinates of the initial position of the snake head

snk_x= screen_width//4
snk_y = screen_hieght//2

#////////////////////////////////////////////////////
#difine the initial position of the snake body

snake = [
    [snk_y,snk_x],
    [snk_y,snk_x-1],
    [snk_y,snk_x-2]
]

#////////////////////////////////////////////////////
#creat the position of the food in the middle of the screen

food = [screen_hieght//2,screen_width//2]
#////////////////////////////////////////////////////
#add the food in the screen by the PI character

window.addch(food[0],food[1],curses.ACS_PI)
#////////////////////////////////////////////////////
#set the initial movement to right

key = curses.KEY_RIGHT

#////////////////////////////////////////////////////
#creat the game loops that loops forever until the player loses or quits

while True:

#take the next key from the keyboard
    next_key = window.getch()
#test if the next key is the reverse of the initial key put the next_key = -1
    if key == curses.KEY_DOWN and next_key == curses.KEY_UP:
        next_key=-1
    elif key == curses.KEY_UP and next_key == curses.KEY_DOWN:
        next_key=-1
    elif key == curses.KEY_LEFT and next_key == curses.KEY_RIGHT:
        next_key=-1
    elif key == curses.KEY_RIGHT and next_key == curses.KEY_LEFT:
        next_key=-1
#test if the next_key == -1 put key = key else key =next_key
    key = key if next_key == -1 else next_key
#if the head of snake collided in the edges of the screen or in the body of the snake the game is over and the player is losing the game
    if snake[0][0] in [0,screen_hieght] or snake[0][1] in [0,screen_width] or snake[0] in snake[1:]:
        curses.endwin()
        quit()
#creat new head and initialize it by the coordinates of the first head
    new_head = [snake[0][0],snake[0][1]]
#test the key for update the position
    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1
#insert the new head in the first position in the snake
    snake.insert(0, new_head)
#test if the snake it the food
    if snake[0] == food:
        food = None
#generat new position of the food in the screen by the modules random until the snake was eating the food
        while food is None:
            new_food = [random.randint(1, screen_hieght - 1), random.randint(1, screen_width - 1)]
            food = new_food if new_food not in snake else None
#add the new position of food
        window.addch(food[0], food[1], curses.ACS_PI)
#take the tail of the snake and replace it by space
    else:
        tail = snake.pop()
        window.addch(tail[0], tail[1], ' ')
    window.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)