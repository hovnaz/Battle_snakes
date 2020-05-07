# # database-ic vercnum e tvialnery ev list-i mej e dnum amen toghy mek index-e
# with open('data.txt', "r") as f:
# 	lines = [line.rstrip() for line in f]


# import random
# # vercnum e patahakan item list-ic
# def Random(l):
# 	return l[random.randint(0,len(l)-1)]


# # odzi tesadashty tvery vercnum e arandzin index-i mej
# # ev sa klini mek toghani matrix 1D
# # width = 11 height = 11


# # LineMatrix = [int(i) for i in str(lines[0])]

# # sa hetagaeum aveli krchat kdardznem
# LineMatrix = []

# for i in range(len(lines[0])):
# 	LineMatrix.append(int(lines[0][i]))


# matrix = []
# for x in range(1,12):
# 	matrix.append(LineMatrix[(x-1)*11:x*11])

# pos = [int(i) for i in lines[1].split()]

# # for i in range(len(matrix)):
# 	# print(matrix[i])
# # print(LineMatrix)




# # class
# class Snake:
# 	"""docstring for Snake"""
# 	def __init__(self, pos):
# 		self.pos = pos # sa hstak posn e
# 		self.x = 5
# 		self.y = 5
# 		self.side_move_snake = 8
# 	def __call__(self):
# 		self.move()
# 	def FieldOfViewPositions(self):
# 		x = self.x
# 		y = self.y
# 		self.directions = [
			# [x - 5, y - 5],
			# [x - 4, y - 5],
			# [x - 3, y - 5],
			# [x - 2, y - 5],
			# [x - 1, y - 5],
			# [x, y - 5],
			# [x + 1, y - 5],
			# [x + 2, y - 5],
			# [x + 3, y - 5],
			# [x + 4, y - 5],
			# [x + 5, y - 5],

# 			[x - 5, y - 4],
# 			[x - 4, y - 4],
# 			[x - 3, y - 4],
# 			[x - 2, y - 4],
# 			[x - 1, y - 4],
# 			[x, y - 4],
# 			[x + 1, y - 4],
# 			[x + 2, y - 4],
# 			[x + 3, y - 4],
# 			[x + 4, y - 4],
# 			[x + 5, y - 4],

# 			[x - 5, y - 3],
# 			[x - 4, y - 3],
# 			[x - 3, y - 3],
# 			[x - 2, y - 3],
# 			[x - 1, y - 3],
# 			[x, y - 3],
# 			[x + 1, y - 3],
# 			[x + 2, y - 3],
# 			[x + 3, y - 3],
# 			[x + 4, y - 3],
# 			[x + 5, y - 3],

# 			[x - 5, y - 2],
# 			[x - 4, y - 2],
# 			[x - 3, y - 2],
# 			[x - 2, y - 2],
# 			[x - 1, y - 2],
# 			[x, y - 2],
# 			[x + 1, y - 2],
# 			[x + 2, y - 2],
# 			[x + 3, y - 2],
# 			[x + 4, y - 2],
# 			[x + 5, y - 2],

# 			[x - 5, y - 1],
# 			[x - 4, y - 1],
# 			[x - 3, y - 1],
# 			[x - 2, y - 1],
# 			[x - 1, y - 1],
# 			[x, y - 1],
# 			[x + 1, y - 1],
# 			[x + 2, y - 1],
# 			[x + 3, y - 1],
# 			[x + 4, y - 1],
# 			[x + 5, y - 1],

# 			[x - 5, y],
# 			[x - 4, y],
# 			[x - 3, y],
# 			[x - 2, y],
# 			[x - 1, y],
# 			[x + 1, y],
# 			[x + 2, y],
# 			[x + 3, y],
# 			[x + 4, y],
# 			[x + 5, y],

# 			[x - 5, y + 1],
# 			[x - 4, y +1],
# 			[x - 3, y + 1],
# 			[x - 2, y + 1],
# 			[x - 1, y + 1],
# 			[x, y + 1],
# 			[x + 1, y + 1],
# 			[x + 2, y + 1],
# 			[x + 3, y + 1],
# 			[x + 4, y + 1],
# 			[x + 5, y + 1],

# 			[x - 5, y + 2],
# 			[x - 4, y +2],
# 			[x - 3, y + 2],
# 			[x - 2, y + 2],
# 			[x - 1, y + 2],
# 			[x, y + 2],
# 			[x + 1, y + 2],
# 			[x + 2, y + 2],
# 			[x + 3, y + 2],
# 			[x + 4, y + 2],
# 			[x + 5, y + 2],

# 			[x - 5, y + 3],
# 			[x - 4, y +3],
# 			[x - 3, y + 3],
# 			[x - 2, y + 3],
# 			[x - 1, y + 3],
# 			[x, y + 3],
# 			[x + 1, y + 3],
# 			[x + 2, y + 3],
# 			[x + 3, y + 3],
# 			[x + 4, y + 3],
# 			[x + 5, y + 3],

# 			[x - 5, y + 4],
# 			[x - 4, y +4],
# 			[x - 3, y + 4],
# 			[x - 2, y + 4],
# 			[x - 1, y + 4],
# 			[x, y + 4],
# 			[x + 1, y + 4],
# 			[x + 2, y + 4],
# 			[x + 3, y + 4],
# 			[x + 4, y + 4],
# 			[x + 5, y + 4],

# 			[x - 5, y + 5],
# 			[x - 4, y +5],
# 			[x - 3, y + 5],
# 			[x - 2, y + 5],
# 			[x - 1, y + 5],
# 			[x, y + 5],
# 			[x + 1, y + 5],
# 			[x + 2, y + 5],
# 			[x + 3, y + 5],
# 			[x + 4, y + 5],
# 			[x + 5, y + 5]
# 		]
# 	def FrontBoxes(self):
# 		x = self.x
# 		y = self.y
# 		self.FrontDirections = [
# 			[x, y - 1,8], # 0 Up
# 			[x, y + 1,2], # 1 Down
# 			[x - 1, y,4], # 2 Left
# 			[x + 1, y,6]  # 3 Right
# 		]
# 	def chooseCell(self,character):
# 		self.FieldOfViewPositions()
# 		found = []
# 		for i in range(len(self.directions)):
# 			x = self.directions[i][0]
# 			y = self.directions[i][1]
# 			# for z in range(len(character)):
# 			if matrix[y][x] == character:
# 				found.append([x,y])

# 		return found
# 	def FrontChooseCell(self,*character):
# 		self.FrontBoxes()
# 		found = []
# 		for i in range(len(self.FrontDirections)):
# 			x = self.FrontDirections[i][0]
# 			y = self.FrontDirections[i][1]
# 			side_move = self.FrontDirections[i][2]
# 			for z in range(len(character)):
# 				if matrix[y][x] == character[z]:
# 					found.append([x,y,side_move])

# 		return found
# 	def PushInData(self,push=True,move=8):
# 		if push == True:
# 			with open('MyData.txt', "w") as f:
# 				f.write('{move}{br}'.format(move= move,br='\n'))
# 		elif push == False:
# 			with open('MyData.txt', "r") as f:
# 				lines = [line.rstrip() for line in f]
# 			return lines
# 	def ShowTheBoxInFront(self,side=8):
# 		self.FrontBoxes()
# 		this_box = self.FrontDirections
# 		if side == 8:
# 			x = this_box[0][0]
# 			y = this_box[0][1]
# 		elif side == 4:
# 			x = this_box[2][0]
# 			y = this_box[2][1]
# 		elif side == 6:
# 			x = this_box[3][0]
# 			y = this_box[3][1]
# 		elif side == 2:
# 			x = this_box[1][0]
# 			y = this_box[1][1]
# 		else:
# 			x = this_box[0][0]
# 			y = this_box[0][1]

# 		return matrix[y][x]
# 		print(self.FrontDirections[0][0])
# 	def move(self):
# 		try:

# 			find_coming_list = [] 
# 			SelectedCellApple = self.chooseCell(2)
# 			# find coming apple
# 			if SelectedCellApple:
# 				for i in range(len(SelectedCellApple)):
# 					# apple-i pos-y
# 					x = SelectedCellApple[i][0]
# 					y = SelectedCellApple[i][1]
# 					# estegh this odzic hanum enq this apple-i posery
# 					# ev da mulov enq hanum verjum kuneneq drakan tiv
# 					find_coming_list.append(abs(self.x - x)+abs(self.y - y))
# 				# estegh man e galis amenamot xndzory ev veradardznum e index-y apple-i
# 				index_apple = find_coming_list.index(min(find_coming_list))
# 				newCell = SelectedCellApple[index_apple]
			
# 		except Exception:
# 			newCell = False
# 		try:
# 			if newCell:
# 				if self.x < newCell[0]: # right
# 					self.side_move_snake = 6
# 				elif self.x > newCell[0]: # left
# 					self.side_move_snake = 4
# 				elif self.y < newCell[1]: # down
# 					self.side_move_snake = 2
# 				elif self.y > newCell[1]: # up
# 					self.side_move_snake = 8

# 			FrontBox = self.ShowTheBoxInFront(self.side_move_snake)
# 			if FrontBox != 0 and FrontBox != 2:
# 				newCell_if = self.FrontChooseCell(0,2)
# 				if len(newCell_if) >= 1:
# 					newCell_if_random = Random(newCell_if)

# 					self.side_move_snake = newCell_if_random[2]

# 		except UnboundLocalError:
# 			newCell_if = self.FrontChooseCell(0,2)

# 			if len(newCell_if) >= 1:
# 				newCell_if_random = Random(newCell_if)
# 				self.side_move_snake = newCell_if_random[2]


# 		print('move',self.side_move_snake)

# Snake = Snake([pos[0],pos[1]])()



















































# w_graph = Graph.create_from_nodes([a,b,c,d,e,f])

# w_graph.connect(a, b, 5)
# w_graph.connect(a, c, 10)
# w_graph.connect(a, e, 2)
# w_graph.connect(b, c, 2)
# w_graph.connect(b, d, 4)
# w_graph.connect(c, d, 7)
# w_graph.connect(c, f, 10)
# w_graph.connect(d, e, 3)

# w_graph.print_adj_mat()
