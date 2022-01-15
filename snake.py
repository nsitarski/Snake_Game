#Import Required Libraries
import pygame
import random
import numpy as np

#draw new food location and increase teail length
def food():
	global foodx
	global foody
	global taillength
	foodx = random.randint(0,((displayWidth -xsize) / xsize)) * xsize
	foody = random.randint(0,((displayHeight - ysize) / ysize)) * ysize
	taillength = taillength + 1
	pygame.draw.rect(gameDisplay, red, [foodx, foody, xsize, ysize],0)
	
#draw new head, if head == any tail value return True for quit game
def head(x,y):
	global x_tail
	global y_tail
	global quitGame
	global taillength
	pygame.draw.rect( gameDisplay, white, [x, y, xsize, ysize],0)
	for index in np.arange(taillength):
		if x_tail[index] == x and y_tail[index] == y:
			return True
			
#Draws Tail		
def tail(x,y,color):
	pygame.draw.rect( gameDisplay, color, [x, y, xsize, ysize],0)
		
def gameLoop():	
	hitSelf = False
	quitGame = False
	global x_head 
	global y_head
	global x_tail
	global y_tail
	global taillength
	global foodx
	global foody
	
	change = 10 
	direction = "right"
	speed = 12
	while not quitGame:	
		
		#checks for button press	
		for event in pygame.event.get():			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					if direction != "down":
						direction = "up"				
				elif event.key == pygame.K_DOWN:
					if direction != "up":
						direction = "down"				
				elif event.key == pygame.K_LEFT:
					if direction != "right":
						direction = "left"				
				elif event.key == pygame.K_RIGHT:
					if direction != "left":
						direction = "right"
				elif event.key == pygame.K_q:
					return(len(x_tail))
					
		#Adds head value to tail array		
		if taillength >= 1:
			x_tail.append(x_head)
			y_tail.append(y_head)
			
		#removes first value from tail array	
		if len(x_tail) > taillength:
			x_tail.pop(0)
			y_tail.pop(0)
		
		#sets movement direction				
		if direction == "up":
			y_head = y_head - change
		elif direction == "down":
			y_head = y_head + change	
		elif direction == "left":
			x_head = x_head - change
		elif direction == "right":
			x_head = x_head + change
		
		#move to other side of screen if hitting edge	
		if y_head < 0 :
			y_head = displayHeight	
		elif y_head >= displayHeight:
			y_head = 0
		elif x_head < 0:
			x_head = displayWidth	
		elif x_head >= displayWidth:
			x_head = 0	
					
		gameDisplay.fill(black)	
		
		#check to see if head == body
		quitGame = head(x_head, y_head)
		if quitGame == True:
			return(len(x_tail))
		
		#prints the values of the tail.	
		if taillength >= 1:
			for index in np.arange(taillength):
				rand_color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
				tail(x_tail[index], y_tail[index],rand_color)
				
		#check to see if head == food
		if foodx == x_head and foody == y_head:
			food()
			
		else:
			pygame.draw.rect(gameDisplay, red, [foodx, foody, xsize, ysize],0)
			
		pygame.display.update()
		clock.tick(speed)
		
#Required Initialization for pygame
pygame.init()

#Set game window size
displayWidth = 800
displayHeight = 600

#Set RBG for food, snake, and background
red = (255,0,0)
white = (255,255,255)
black = (0,0,0)

#set size of pixel
xsize = 10
ysize = 10

#set initial food x,y coordinates. 
#Use this math to ensure 100% overlap with snake. 
foodx = random.randint(0,(displayWidth / xsize))  *xsize
foody = random.randint(0,(displayHeight  / ysize))  *ysize

#set initial head location
x_head = 200
y_head = 200

#set initial tail length and set up empty tail array
taillength = 0
x_tail = []
y_tail = []

#show game window
gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))

#add title to window
pygame.display.set_caption('My First Snake game')

#set up clock object used later for tracking time
clock = pygame.time.Clock()

#start main game loop						
score = gameLoop()
pygame.quit()
print("\nGreat Job. Your Score Was {:,}!!!".format(score*100))
input()
quit()

