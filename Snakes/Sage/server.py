# database-ic vercnum e tvialnery ev list-i mej e dnum amen toghy mek index-e
with open('data.txt', "r") as f:
	lines = [line.rstrip() for line in f]


import random
# vercnum e patahakan item list-ic
def Random(l):
	return l[random.randint(0,len(l)-1)]




# odzi tesadashty tvery vercnum e arandzin index-i mej
# ev sa klini mek toghani matrix 1D
# width = 11 height = 11


# LineMatrix = [int(i) for i in str(lines[0])]

# sa hetagaeum aveli krchat kdardznem
LineMatrix = []

for i in range(len(lines[0])):
	LineMatrix.append(int(lines[0][i]))


matrix = []
for x in range(1,12):
	matrix.append(LineMatrix[(x-1)*11:x*11])

pos = [int(i) for i in lines[1].split()]

# for i in range(len(matrix)):
	# print(matrix[i])
# print(LineMatrix)




# class

class Snake:
	"""docstring for Snake"""
	def __init__(self, pos):
		self.pos = pos # sa hstak posn e
		self.x = 5
		self.y = 5
	def __call__(self):
		self.move()
	def FieldOfViewPositions(self):
		x = self.x
		y = self.y
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
	def FrontBoxes(self):
		x = self.x
		y = self.y
		self.FrontDirections = [
			[x, y - 1,8], # 0 Up
			[x, y + 1,2], # 1 Down
			[x - 1, y,4], # 2 Left
			[x + 1, y,6]  # 3 Right
		]
	def chooseCell(self,character):
		self.FieldOfViewPositions()
		found = []
		for i in range(len(self.directions)):
			x = self.directions[i][0]
			y = self.directions[i][1]
			# for z in range(len(character)):
			if matrix[y][x] == character:
				found.append([x,y])

		return found
	def FrontChooseCell(self,*character):
		self.FrontBoxes()
		found = []
		for i in range(len(self.FrontDirections)):
			x = self.FrontDirections[i][0]
			y = self.FrontDirections[i][1]
			side_move = self.FrontDirections[i][2]
			for z in range(len(character)):
				if matrix[y][x] == character[z]:
					found.append([x,y,side_move])

		return found
	def PushInData(self,push=True,move=8):
		if push == True:
			with open('MyData.txt', "w") as f:
				f.write('{move}{br}'.format(move= move,br='\n'))
		elif push == False:
			with open('MyData.txt', "r") as f:
				lines = [line.rstrip() for line in f]
			return lines
	def move(self):
		try:

			find_coming_list = [] 
			SelectedCellApple = self.chooseCell(2)
			# find coming apple
			if SelectedCellApple:
				for i in range(len(SelectedCellApple)):
					# apple-i pos-y
					x = SelectedCellApple[i][0]
					y = SelectedCellApple[i][1]
					# estegh this odzic hanum enq this apple-i posery
					# ev da mulov enq hanum verjum kuneneq drakan tiv
					find_coming_list.append(abs(self.x - x)+abs(self.y - y))
				# estegh man e galis amenamot xndzory ev veradardznum e index-y apple-i
				index_apple = find_coming_list.index(min(find_coming_list))
				newCell = SelectedCellApple[index_apple]
			
		except Exception:
			newCell = False

		if newCell:
			if self.x < newCell[0]: # right
				side_move_snake = 6
			elif self.x > newCell[0]: # left
				side_move_snake = 4
			elif self.y < newCell[1]: # down
				side_move_snake = 2
			elif self.y > newCell[1]: # up
				side_move_snake = 8
			print('move',side_move_snake)
		# else:
		# 	try:
		# 		emptyCells = self.FrontChooseCell(0)
		# 		newCell = Random(emptyCells)
		# 	except ValueError:
		# 		newCell = False
		# 	if newCell:
		# 		print('move',newCell[2])


Snake = Snake([pos[0],pos[1]])()











# def move(self):




# 		self.FrontBoxes()
# 		list_have_item = []
# 		for i in range(len(self.FrontDirections)):
# 			x = self.FrontDirections[i][0]
# 			y = self.FrontDirections[i][1]
# 			if matrix[y][x] == 0:
# 				list_have_item.append(0)
# 			else:
# 				list_have_item.append(1)
# 		move_bool = Tr
# 		if self.x < pos_apple[0] and list_have_item[3] == 0: # right
# 			side_move_snake = 6
# 		elif self.x > pos_apple[0] and list_have_item[2] == 0: # left
# 			side_move_snake = 4
# 		elif self.y < pos_apple[1] and list_have_item[0] == 0: # down
# 			side_move_snake = 2
# 		elif self.y > pos_apple[1] and list_have_item[1] == 0: # up
# 			side_move_snake = 8
# 		else:

# 			emptyCells = self.FrontChooseCell(0)
# 			side_move_snake = Random(emptyCells)

# 	else:
# 		# vercnum e data-ic tvialnery
# 		side_move = self.PushInData(False)
# 		# vercnum e arajin toghi datan 
# 		# vory verjin qayln er
# 		side_move_snake = int(side_move[0])
# 		self.FrontBoxes()
# 		for i in range(len(self.FrontDirections)):
# 			item = self.FrontDirections[i][2]
# 			if item == side_move_snake:
# 				x = self.FrontDirections[i][0]
# 				y = self.FrontDirections[i][1]

# 				if matrix[y][x] == 1:
# 					print('mtav')
# 					emptyCells = self.FrontChooseCell(0)
# 					side_move_snake = Random(emptyCells)
# 				break
# 	# print('move',side_move_snake)
# 	# print(SelectedCellApple)


# 	print('move',side_move_snake)

# 	self.PushInData(True,side_move_snake)

