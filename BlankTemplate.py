"""
this is how to draw circles and lines - see below

pygame.draw.circle(screen,(r,g,b),(x,y),(10),(0))
pygame.draw.line(screen,(r,g,b),(startx,starty),(endx,endy),width)

"""

#first things first
import pygame, sys, math, random


#init values here
width=700
height=700
glock=20
MX=MY=0

Step1 = "0"
Step2 = "0"
Step3 = "0"
Step4 = "0"
Draw = "0"

#init functions


#init stuff
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()



#looping code goes here
running = 1

while running:
	#erases screen, fills it with black per loop
	screen.fill((0, 0, 0))

	#keyboard inputs, press q to quit
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = 0
			pygame.quit()
		elif event.type == pygame.MOUSEMOTION:
			MX,MY = event.pos
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_p:
				glock = glock + 1
				print(glock)
			elif event.key == pygame.K_o:
				glock = glock - 1
				print(glock)
			##elif event.key == pygame.K_q:
			##	if Step1 == "0":
			##		Step1 = "1"
			##		print("Step1 ON")
			##		running = 0
			##	elif Step1 == "1":
			##		Step1 = "0"
			##		print("Step1 OFF")
			elif event.key == pygame.K_w:
				if Step2 == "0":
					Step2 = "1"
					print("Step2 ON")
				elif Step2 == "1":
					Step2 = "0"
					print("Step2 Off")
			elif event.key == pygame.K_e:
				if Step3 == "0":
					Step3 = "1"
					print("Step3 ON")
				elif Step3 == "1":
					Step3 = "0"
					print("Step3 Off")
			elif event.key == pygame.K_r:
				if Step4 == "0":
					Step4 = "1"
					print("Step4 ON")
				elif Step4 == "1":
					Step4 = "0"
					print("Step4 OFF")
			elif event.key == pygame.K_a:
				if Draw == "0":
					Draw = "1"
					print("Draw ON")
				elif Draw == "1":
					Draw = "0"
					print("Draw Off")
					

	if Step1 == "1":
		Step1 = "0"


	if Step2 == "1":
		Step2 = "0"
		

	if Step3 == "1":
		Step3 = "0"

	if Step4 == "1":
		Step4 = "0"


	if Draw == "1":
		Draw = "0"


	#drawing stuff goes here
	pygame.draw.circle(screen,(255,2,66),(MX,MY),(5),(0))
	pygame.draw.aaline(screen,(0,255,0),(0,0),(MY,MX),2)
	
	
	#draws the circle and line to screen
	pygame.display.flip()
	
	#waits for a bit before starting the loop again 
	clock.tick(glock)







