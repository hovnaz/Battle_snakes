# settings



# hatuk modulner


import os,sys
import pygame
from pygame.locals import *
import random

from subprocess import PIPE, Popen

	




StartBoolean = True
snake_color = [((155,62,92),(185,102,129)), ((121,185,177),(147,225,216)), ((96,98,80),(117,119,97))]
snake_pos = [[10,40],[15,14],[20,24]]

Data = {
	'snake': {},
	'apple': []
}



# kubiki chapy
size_box = 15

# ashxarhi erkaruteuny u bardzruteuny
heightWindowX = 50 * size_box
heightWindowY = 50 * size_box


# hatuk guener
DIE_COLOR = (16, 20, 26)
Wall_COLOR = (27, 27, 22)


# xndzori qanaky

Apple_count = 200


# ashxarhi gdzagiry
matrix = []


# vercnum e skzbnakan dir-y
DefaultCwd = os.getcwd()







# vercnum e Snakes-i meji bolor folder-nery
# ev kcum e FNamesSnakesF sra mej
FNamesMain = next(os.walk('.'))[1]
if 'Snakes' in FNamesMain:
	FNamesSnakesF = next(os.walk('Snakes/.'))[1]
	if len(FNamesSnakesF) <= 0:
		StartBoolean = False
else:
	StartBoolean = False

del FNamesMain


import math


# clent@n e voroshum ashxari araguteuny
try:
	delay_snake = int(input('Enter the speed of snakes in a millisecond '))
except ValueError:
	delay_snake = 0


# class Snake

class Snake:
	def __init__(self,name,pos):
		self.name = name
		self.pos = pos

		self.previous_step = [] # prev step
		self.tail_list = [] # pochy

		# listi mej mtcnum e pochi postionnery 3 hat
		for x in range(1,4):
			self.tail_list.append([self.pos[0],self.pos[1]+x])
		Data['snake'][self.name]['tail_pos'] = self.tail_list
	# sran kancum enq loop-um 
	def __call__(self,event):
		# kanchum e tvial odzi glxavor kodin da karogh e linel cankacac lezu


		# skzbic gnum e skzbnakan dir
		os.chdir(DefaultCwd)
		# isk heto teghapoxvum e tvial dir
		os.chdir('{}/{}'.format('Snakes',self.name))

		try:
			process = Popen(Data['snake'][self.name]['cmd'], stdin=PIPE, stdout=PIPE)
			stdin,stdout = process.communicate()
		except KeyboardInterrupt:
			sys.exit()
		except EOFError:
			sys.exit()
		except OSError:
			sys.exit()


		strLine = stdin.decode('utf-8')
		print(strLine)
		ArrLine = strLine.split()

		for x in range(len(ArrLine)):
			if ArrLine[x] == 'move':
				ArrLine = ArrLine[x+1]
				break


		# isk aestegh kanchum e mnacac functioner-y 
		if not event == '_':
			self.move(event)
		else:
			self.move(ArrLine)
		self.PushInData()
	def tail(self,push=' '):
		if push == '_': # die
			return
		# previous step 
		x = self.previous_step[0]
		y = self.previous_step[1]

		# avelacnum e poch verjum

		if push == True: # push
			self.tail_list.append([x,y])
		elif not push: # pop
			prev_tail = self.tail_list.pop()
			matrix[prev_tail[1]][prev_tail[0]] = 0


		# move

		prev_tail = self.tail_list.pop() # jnjum e verjiny
		self.tail_list.insert(0,[x,y]) # avelacnum e odzi naxord qaelum evs mek pochi ktor :D

		matrix[prev_tail[1]][prev_tail[0]] = 0 # jnjvac teghu matrixum el e jnjum
		matrix[y][x] = 3 # naev nor ktorn el e matrix mtcnum





		Data['snake'][self.name]['tail_pos'] = self.tail_list



	def eat(self,pos):
		newX = pos[0]
		newY = pos[1]

		matrix[self.pos[1]][self.pos[0]] = 0
		matrix[newY][newX] = 8 # index
		self.pos[0] = newX 
		self.pos[1] = newY


		apple = Data['apple']

		apple.remove([self.pos[0],self.pos[1]])

	def die(self):
		matrix[self.pos[1]][self.pos[0]] = 1


		for i in range(len(self.tail_list)): #die in tail
			x = self.tail_list[i][0]
			y = self.tail_list[i][1]
			matrix[y][x] = 1

		Data['snake'][self.name]['tail_pos'] = self.tail_list
		Data['snake'][self.name]['die'] = True

	def move(self,side):
		settings_tail = ' '
		x = self.pos[0]
		y = self.pos[1]
		newX = x
		newY = y
		if side == 'left' or side == 4 or side == '4': 
			newX = x-1
		elif side == 'right' or side == 6 or side == '6':
			newX = x+1
		elif side == 'up' or side == 8 or side == '8':
			newY = y-1
		elif side == 'down' or side == 2 or side == '2':
			newY = y+1
		else:
			newY = y-1

		if matrix[newY][newX] == 0: # move
			# print('move')
			matrix[y][x] = 0;
			matrix[newY][newX] = 8 # index
			self.pos[0] = newX 
			self.pos[1] = newY

		elif matrix[newY][newX] == 2: # eat
			self.eat([newX,newY])
			settings_tail = True
		else: # die
			self.die()
			settings_tail = '_'


		Data['snake'][self.name]['pos'] = self.pos
		self.previous_step = [x,y]

		# pochi kargavorumnery
		self.tail(settings_tail)

	def FieldOfViewPositions(self):
		x = self.pos[0]
		y = self.pos[1]
		self.directions = [
			[x - 5, y - 5],
			[x - 4, y - 5],
			[x - 3, y - 5],
			[x - 2, y - 5],
			[x - 1, y - 5],
			[x, y - 5],
			[x + 1, y - 5],
			[x + 2, y - 5],
			[x + 3, y - 5],
			[x + 4, y - 5],
			[x + 5, y - 5],

			[x - 5, y - 4],
			[x - 4, y - 4],
			[x - 3, y - 4],
			[x - 2, y - 4],
			[x - 1, y - 4],
			[x, y - 4],
			[x + 1, y - 4],
			[x + 2, y - 4],
			[x + 3, y - 4],
			[x + 4, y - 4],
			[x + 5, y - 4],

			[x - 5, y - 3],
			[x - 4, y - 3],
			[x - 3, y - 3],
			[x - 2, y - 3],
			[x - 1, y - 3],
			[x, y - 3],
			[x + 1, y - 3],
			[x + 2, y - 3],
			[x + 3, y - 3],
			[x + 4, y - 3],
			[x + 5, y - 3],

			[x - 5, y - 2],
			[x - 4, y - 2],
			[x - 3, y - 2],
			[x - 2, y - 2],
			[x - 1, y - 2],
			[x, y - 2],
			[x + 1, y - 2],
			[x + 2, y - 2],
			[x + 3, y - 2],
			[x + 4, y - 2],
			[x + 5, y - 2],

			[x - 5, y - 1],
			[x - 4, y - 1],
			[x - 3, y - 1],
			[x - 2, y - 1],
			[x - 1, y - 1],
			[x, y - 1],
			[x + 1, y - 1],
			[x + 2, y - 1],
			[x + 3, y - 1],
			[x + 4, y - 1],
			[x + 5, y - 1],

			[x - 5, y],
			[x - 4, y],
			[x - 3, y],
			[x - 2, y],
			[x - 1, y],
			[x, y],
			[x + 1, y],
			[x + 2, y],
			[x + 3, y],
			[x + 4, y],
			[x + 5, y],

			[x - 5, y + 1],
			[x - 4, y +1],
			[x - 3, y + 1],
			[x - 2, y + 1],
			[x - 1, y + 1],
			[x, y + 1],
			[x + 1, y + 1],
			[x + 2, y + 1],
			[x + 3, y + 1],
			[x + 4, y + 1],
			[x + 5, y + 1],

			[x - 5, y + 2],
			[x - 4, y +2],
			[x - 3, y + 2],
			[x - 2, y + 2],
			[x - 1, y + 2],
			[x, y + 2],
			[x + 1, y + 2],
			[x + 2, y + 2],
			[x + 3, y + 2],
			[x + 4, y + 2],
			[x + 5, y + 2],

			[x - 5, y + 3],
			[x - 4, y +3],
			[x - 3, y + 3],
			[x - 2, y + 3],
			[x - 1, y + 3],
			[x, y + 3],
			[x + 1, y + 3],
			[x + 2, y + 3],
			[x + 3, y + 3],
			[x + 4, y + 3],
			[x + 5, y + 3],

			[x - 5, y + 4],
			[x - 4, y +4],
			[x - 3, y + 4],
			[x - 2, y + 4],
			[x - 1, y + 4],
			[x, y + 4],
			[x + 1, y + 4],
			[x + 2, y + 4],
			[x + 3, y + 4],
			[x + 4, y + 4],
			[x + 5, y + 4],

			[x - 5, y + 5],
			[x - 4, y +5],
			[x - 3, y + 5],
			[x - 2, y + 5],
			[x - 1, y + 5],
			[x, y + 5],
			[x + 1, y + 5],
			[x + 2, y + 5],
			[x + 3, y + 5],
			[x + 4, y + 5],
			[x + 5, y + 5]
		]

	def PushInData(self):
		self.FieldOfViewPositions()
		found = ''
		for i in range(len(self.directions)):
			x = self.directions[i][0]
			y = self.directions[i][1]
			if x <= 0 or x >= heightWindowX//size_box-1 or y <= 0 or y >= heightWindowY//size_box-1:
				found+= '1'
			else:
				found+= str(matrix[y][x])

			with open('data.txt', "w") as f:

				f.write('{matrix}{br}{posX} {posY}{br}{tail_Len}'.format(matrix=found,br='\n',tail_Len=len(self.tail_list),posX = self.pos[0],posY = self.pos[1]))
				# matrix
				# snake head pos
				# tail_Len

# generate tmatrix


for y in range(heightWindowY//size_box):
	matrix.append([])
	for x in range(heightWindowX//size_box):
		matrix[y].append(0)

# patern e sarqum 
for side in range(heightWindowY//size_box):
	matrix[side][0] = 1 # left

	matrix[side][len(matrix[0])-1] = 1 # right

for side in range(heightWindowX//size_box):
	matrix[0][side] = 1 # up
	matrix[len(matrix)-1][side] = 1 # down







# generate snake

for i in range(len(FNamesSnakesF)):

	Data['snake'][FNamesSnakesF[i]] = {
	'name': FNamesSnakesF[i],
	'color': snake_color[i],
	'pos': snake_pos[i],
	'tail_pos': [],
	'die': False,
	'cmd': [],
	'class': ''
	}
# create snakes classes
for i in range(len(FNamesSnakesF)):
	# odzeri classnery mtcnum e baza

	snake = Data['snake'][FNamesSnakesF[i]]
	snake['class'] = Snake(snake['name'],snake['pos'])

# generate matrix
for i in range(len(FNamesSnakesF)): # aestegh pochi poziciannern e mtcnum matrix vor ereva	

	snake = Data['snake'][FNamesSnakesF[i]]
	# print(snake['tail_pos'])
	for z in range(len(snake['tail_pos'])):
		x = snake['tail_pos'][z][0]
		y = snake['tail_pos'][z][1]
		matrix[y][x] = 3



# generate appales

while Apple_count > 0:
	x = random.randint(1,heightWindowX//size_box-1)
	y = random.randint(1,heightWindowY//size_box-1)
	if matrix[y][x] == 0:
		matrix[y][x] = 2
		Apple_count-=1
		Data['apple'].append([x,y])

# aestegh mtcnum e data command.txt-i gracy vor kareli lini kanchel nran
for i in range(len(FNamesSnakesF)):
	fName = '{}/{}/{}'.format('Snakes',FNamesSnakesF[i],'command.txt')
	with open(fName, 'r') as f:
		cmd = f.read()
		cmd = cmd.split()

		Data['snake'][FNamesSnakesF[i]]['cmd'] = cmd




del side


# create window and map
pygame.init()
screen = pygame.display.set_mode((heightWindowX, heightWindowY), 0, 32)
# ashxatum e anverj



move = '_'
while StartBoolean:
	# sa patuihany pakelu hamar e
	for event in pygame.event.get():
		if event.type == QUIT:
			sys.exit()


	keys=pygame.key.get_pressed()
	if keys[K_LEFT]:
		move = 4
	elif keys[K_RIGHT]:
		move = 6
	elif keys[K_DOWN]:
		move = 2
	elif keys[K_UP]:
		move = 8
	else:
		move='_'	
	try:
		pygame.time.delay(delay_snake)


		screen.fill((255,255,255))

		# sa patern e nerkum baec mez petq che sa aestegh toghnel petq e inchqan hnaravor e shut aesteghic durs hanel ev ashxatacnel miaen 1 ankam voch te cikli mej anhntat

		pygame.draw.rect(screen, Wall_COLOR, (0,0,heightWindowX,size_box))
		pygame.draw.rect(screen, Wall_COLOR, (0,size_box*(heightWindowY // size_box-1),heightWindowX,size_box))
		pygame.draw.rect(screen, Wall_COLOR, (0,size_box*1,size_box,heightWindowY-(size_box*2)))
		pygame.draw.rect(screen, Wall_COLOR, (size_box*(heightWindowX // size_box-1),size_box*1,size_box,heightWindowY-(size_box*2)))




		for i in range(len(FNamesSnakesF)):
			color = [snake['color'][0],snake['color'][1]]
			snake = Data['snake'][FNamesSnakesF[i]]
			if snake['die']:
				color = [DIE_COLOR,DIE_COLOR]
			if not snake['die']: # ete merel e apa el class-y chi ashxati
				snake['class'](move)
			# head
			x = snake['pos'][0]
			y = snake['pos'][1]
			pygame.draw.rect(screen, color[0], (size_box * x, size_box * y,size_box,size_box))
			# tail
			for d in range(len(snake['tail_pos'])):
				x = snake['tail_pos'][d][0]
				y = snake['tail_pos'][d][1]
				pygame.draw.rect(screen, color[1], (size_box * x,size_box * y,size_box,size_box))

			



		apple = Data['apple']
		# apples
		for i in range(len(apple)):
			x = apple[i][0]
			y = apple[i][1]
			pygame.draw.rect(screen, (255,0,0), (size_box * x, size_box * y,size_box,size_box))



		screen.unlock()
		# amen angam update anum
		# popoxuterunry tesnelu hamer
		pygame.display.update()

	except KeyboardInterrupt:
		sys.exit()
		break
	except EOFError:
		sys.exit()
		break
	except OSError:
		sys.exit()
		break
	except Exception:
		sys.exit()
		break