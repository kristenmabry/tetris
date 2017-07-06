# name: Kristen Mabry
# collaborators:
# tetris.py
# plays a game of tetris

from graphics import *

# creates a single block using the rectangle class in graphics
class Block(Rectangle):
	def __init__(self, coords, color):
		self.point1 = Point(coords[0]*30, coords[1]*30)
		self.point2 = Point((coords[0]*30)+30, (coords[1]*30)+30)
		Rectangle.__init__(self, self.point1, self.point2)
		Rectangle.setFill(self, color)
		Rectangle.setWidth(self, 3)

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
	




