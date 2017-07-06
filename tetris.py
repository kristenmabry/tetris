# name: Kristen Mabry
# collaborators:
# tetris.py
# plays a game of tetris

from graphics import *

win = GraphWin("WTP Tetris", 300, 300)

class Block(Rectangle):
	def __init__(self, coords, color):
		self.point1 = Point(coords[0]*30, coords[1]*30)
		self.point2 = Point((coords[0]*30)+30, (coords[1]*30)+30)
		Rectangle.__init__(self, self.point1, self.point2)
		Rectangle.setFill(self, color)
		Rectangle.setWidth(self, 3)
def i_block(coords):
	center_block = Block(coords,"blue")
	block_1_coords = [coords[0]-1, coords[1]]
	block_1 = Block(block_1_coords, "blue")
	block_2_coords = [coords[0]+1, coords[1]]
	block_2 = Block(block_2_coords, "blue")
	block_3_coords = [coords[0]+2, coords[1]]
	block_3 = Block(block_3_coords, "blue")
	return [block_1, center_block, block_2, block_3]

def j_block(coords):
	center_block = Block(coords,"orange")
	block_1_coords = [coords[0]-1, coords[1]]
	block_1 = Block(block_1_coords, "orange")
	block_2_coords = [coords[0]+1, coords[1]]
	block_2 = Block(block_2_coords, "orange")
	block_3_coords = [coords[0]+1, coords[1]+1]
	block_3 = Block(block_3_coords, "orange")
	return [block_1, center_block, block_2, block_3]

def l_block(coords):
	center_block = Block(coords,"cyan")
	block_1_coords = [coords[0]-1, coords[1]]
	block_1 = Block(block_1_coords, "cyan")
	block_2_coords = [coords[0]+1, coords[1]]
	block_2 = Block(block_2_coords, "cyan")
	block_3_coords = [coords[0]-1, coords[1]+1]
	block_3 = Block(block_3_coords, "cyan")
	return [block_1, center_block, block_2, block_3]

def o_block(coords):
	center_block = Block(coords,"red")
	block_1_coords = [coords[0]-1, coords[1]]
	block_1 = Block(block_1_coords, "red")
	block_2_coords = [coords[0], coords[1]+1]
	block_2 = Block(block_2_coords, "red")
	block_3_coords = [coords[0]-1, coords[1]+1]
	block_3 = Block(block_3_coords, "red")
	return [block_1, center_block, block_2, block_3]

def s_block(coords):
	center_block = Block(coords,"green2")
	block_1_coords = [coords[0]+1, coords[1]]
	block_1 = Block(block_1_coords, "green2")
	block_2_coords = [coords[0], coords[1]+1]
	block_2 = Block(block_2_coords, "green2")
	block_3_coords = [coords[0]-1, coords[1]+1]
	block_3 = Block(block_3_coords, "green2")
	return [block_1, center_block, block_2, block_3]

def t_block(coords):
	center_block = Block(coords,"yellow")
	block_1_coords = [coords[0]+1, coords[1]]
	block_1 = Block(block_1_coords, "yellow")
	block_2_coords = [coords[0], coords[1]+1]
	block_2 = Block(block_2_coords, "yellow")
	block_3_coords = [coords[0]-1, coords[1]]
	block_3 = Block(block_3_coords, "yellow")
	return [block_1, center_block, block_2, block_3]

def z_block(coords):
	center_block = Block(coords,"magenta")
	block_1_coords = [coords[0]+1, coords[1]+1]
	block_1 = Block(block_1_coords, "magenta")
	block_2_coords = [coords[0], coords[1]+1]
	block_2 = Block(block_2_coords, "magenta")
	block_3_coords = [coords[0]-1, coords[1]]
	block_3 = Block(block_3_coords, "magenta")
	return [block_1, center_block, block_2, block_3]
	

block = z_block([2,3])
for x in block:
	x.draw(win)

win.getMouse()


