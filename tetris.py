# name: Kristen Mabry
# collaborators:
# tetris.py
# plays a game of tetris

from graphics import *
import time
import random

#keeps track of variables for the game
class Game():
	def __init__(self, col, row):
		self.column = col
		self.row = row
		self.window = GraphWin("Tetris", col*30, row*30)
		self.current_shape = ""
		self.block_locations = [self.row]*self.column

# creates a new shape and drops it until it can't move
	def add_drop_shape(self,shape_letter):
		if shape_letter == 0:
			self.current_shape = I_shape([int(self.column/2),-1])
			self.current_shape.draw(self.window)
		elif shape_letter == 1:
			self.current_shape = J_shape([int(self.column/2),-1])
			self.current_shape.draw(self.window)
		elif shape_letter == 2:
			self.current_shape = L_shape([int(self.column/2),-1])
			self.current_shape.draw(self.window)
		elif shape_letter == 3:
			self.current_shape = O_shape([int(self.column/2),-1])
			self.current_shape.draw(self.window)
		elif shape_letter == 4:
			self.current_shape = S_shape([int(self.column/2),-1])
			self.current_shape.draw(self.window)
		elif shape_letter == 5:
			self.current_shape = T_shape([int(self.column/2),-1])
			self.current_shape.draw(self.window)
		elif shape_letter == 6:
			self.current_shape = Z_shape([int(self.column/2),-1])
			self.current_shape.draw(self.window)
		while self.current_shape.can_move(0,1) == True:
			self.current_shape.move(0,1)
			time.sleep(.25)

#replaces the block list with the location of each of the top blocks
		for block in self.current_shape.list_of_blocks:
			point = block.getP1()
			y = point.getY()
			x = point.getX()
			if y/30 < self.block_locations[int(x/30)]:
				self.block_locations[int(x/30)] = int(y/30)
			
	
# creates a random shape and saves it as an instance variable
	def random_shape(self):
		self.current_shape = random.randint(0, 6)
		return self.current_shape
				
game = Game(10,20)
		
# creates a single block using the rectangle class in graphics
class Block(Rectangle):
	def __init__(self, coords, color):
		self.point1 = Point(coords[0]*30, coords[1]*30)
		self.point2 = Point((coords[0]*30)+30, (coords[1]*30)+30)
		Rectangle.__init__(self, self.point1, self.point2)
		Rectangle.setFill(self, color)
		Rectangle.setWidth(self, 3)
		
# for y, checks if the space below it is unoccupied based on the list of current top block locations
# need to fix x
	def can_move(self,dx, dy):
		bottom_right = Rectangle.getP2(self)
		right_x = bottom_right.getX()
		lowest_y = bottom_right.getY()
		if (lowest_y/30)-1 + dy >= game.block_locations[int((right_x/30)-1)]:
			can_move = False
		elif dx != 0:
			if dx > 0 and right_x/30 + dx > win_x:
				can_move = False
			if dx < 0 and (right_x-30)/30 - dx < 0:
				can_move = False
		else:
			can_move = True
		return can_move


# creates multiple blocks depending on the list of coordinates
# method draws each block to form the final shape
class Shape():
	def __init__(self, coords, color):
		self.list_of_blocks = []
		for x in coords:
			block = Block(x, color)
			self.list_of_blocks.append(block)

	def draw(self, win):
		for x in self.list_of_blocks:
			x.draw(win)

#moves the shape by dx and dy which are coordinates
	def move(self,dx,dy):
		for block in self.list_of_blocks:
			block.move(dx*30, dy*30)

#uses the move method in block to see if the shape can move
	def can_move(self,dx,dy):
		can_move = True
		for block in self.list_of_blocks:
			if block.can_move(dx,dy) == False:
				can_move = False
		return can_move


# defines the list of coordinates and the color for each shape

class I_shape(Shape):
	def __init__(self, center_coords):
		
		block_1_coords = [center_coords[0]-1, center_coords[1]]
		block_2_coords = [center_coords[0]+1, center_coords[1]]
		block_3_coords = [center_coords[0]+2, center_coords[1]]
		list_of_coords = [block_1_coords, center_coords, block_2_coords, block_3_coords]
		Shape.__init__(self, list_of_coords, "blue")

class J_shape(Shape):
	def __init__(self, center_coords):
		block_1_coords = [center_coords[0]-1, center_coords[1]]
		block_2_coords = [center_coords[0]+1, center_coords[1]]
		block_3_coords = [center_coords[0]+1, center_coords[1]+1]
		list_of_coords = [block_1_coords, center_coords, block_2_coords, block_3_coords]
		Shape.__init__(self, list_of_coords, "orange")

class L_shape(Shape):
	def __init__(self, center_coords):
		block_1_coords = [center_coords[0]-1, center_coords[1]]
		block_2_coords = [center_coords[0]+1, center_coords[1]]
		block_3_coords = [center_coords[0]-1, center_coords[1]+1]
		list_of_coords = [block_1_coords, center_coords, block_2_coords, block_3_coords]
		Shape.__init__(self, list_of_coords, "cyan")


class O_shape(Shape):
	def __init__(self, center_coords):
		block_1_coords = [center_coords[0]-1, center_coords[1]]
		block_2_coords = [center_coords[0], center_coords[1]+1]
		block_3_coords = [center_coords[0]-1, center_coords[1]+1]
		list_of_coords = [block_1_coords, center_coords, block_2_coords, block_3_coords]
		Shape.__init__(self, list_of_coords, "red")

class S_shape(Shape):
	def __init__(self, center_coords):
		block_1_coords = [center_coords[0]+1, center_coords[1]]
		block_2_coords = [center_coords[0], center_coords[1]+1]
		block_3_coords = [center_coords[0]-1, center_coords[1]+1]
		list_of_coords = [block_1_coords, center_coords, block_2_coords, block_3_coords]
		Shape.__init__(self, list_of_coords, "green2")

class T_shape(Shape):
	def __init__(self, center_coords):
		block_1_coords = [center_coords[0]+1, center_coords[1]]
		block_2_coords = [center_coords[0], center_coords[1]+1]
		block_3_coords = [center_coords[0]-1, center_coords[1]]
		list_of_coords = [block_1_coords, center_coords, block_2_coords, block_3_coords]
		Shape.__init__(self, list_of_coords, "yellow")

class Z_shape(Shape):
	def __init__(self, center_coords):
		block_1_coords = [center_coords[0]+1, center_coords[1]+1]
		block_2_coords = [center_coords[0], center_coords[1]+1]
		block_3_coords = [center_coords[0]-1, center_coords[1]]
		list_of_coords = [block_1_coords, center_coords, block_2_coords, block_3_coords]
		Shape.__init__(self, list_of_coords, "magenta")

def drop_shapes() :
	while 0 not in game.block_locations:
		new_shape = game.random_shape()
		game.add_drop_shape(new_shape)
		time.sleep(1)
drop_shapes()
