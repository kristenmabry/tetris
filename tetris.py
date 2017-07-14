# name: Kristen Mabry
# collaborators:Joy
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
		self.window = GraphWin("Tetris", col*30+200, row*30+100)
		self.current_shape = ""
		self.tops = [self.row]*self.column
		self.key = None
		self.window.bind_all('<Key>', self.key_pressed)
		self.all_blocks = []
		self.score = 0
		self.score_display = Text(Point(self.column*30 + 100, 110), str(self.score))
		self.score_display.setSize(16)
		self.score_display.draw(self.window)
		

	def add_floor(self):
		for x in range(self.column):
			self.all_blocks.append(Block([x, self.row],"blue"))

# creates a new shape and drops it until it can't move
	def add_drop_shape(self):
		self.shape_letter = self.next_shape
		if self.shape_letter == 0:
			self.current_shape = I_shape([int(self.column/2),-1])
			self.current_shape.draw(self.window)
		elif self.shape_letter == 1:
			self.current_shape = J_shape([int(self.column/2),-1])
			self.current_shape.draw(self.window)
		elif self.shape_letter == 2:
			self.current_shape = L_shape([int(self.column/2),-1])
			self.current_shape.draw(self.window)
		elif self.shape_letter == 3:
			self.current_shape = O_shape([int(self.column/2),-1])
			self.current_shape.draw(self.window)
		elif self.shape_letter == 4:
			self.current_shape = S_shape([int(self.column/2),-1])
			self.current_shape.draw(self.window)
		elif self.shape_letter == 5:
			self.current_shape = T_shape([int(self.column/2),-1])
			self.current_shape.draw(self.window)
		elif self.shape_letter == 6:
			self.current_shape = Z_shape([int(self.column/2),-1])
			self.current_shape.draw(self.window)
		while self.current_shape.can_move(0,1) == True:
			self.handle_keypress()
			self.current_shape.move(0,1)
			self.handle_keypress()
			time.sleep(.25)
		self.score += 5

#replaces the block list with the location of each of the top blocks
		for block in self.current_shape.list_of_blocks:
			point = block.getP1()
			y = point.getY()
			x = point.getX()
			self.all_blocks.append(block)
			if y/30 < self.tops[int(x/30)]:
				self.tops[int(x/30)] = int(y/30)
			
	
# creates a random shape and saves it as an instance variable
	def random_shape(self):
		self.next_shape = random.randint(0,6)

	def key_pressed(self, event):
		self.key = event.keysym
	
	def handle_keypress(self):
		if self.key == "Right":
			if self.current_shape.can_move(1,0):
				self.current_shape.move(1,0)
		elif self.key == "Left":
			if self.current_shape.can_move(-1,0):
				self.current_shape.move(-1,0)
		elif self.key == "Down":
			if self.current_shape.can_move(0,1):
				self.current_shape.move(0,1)
		elif self.key == "Up":
			if self.current_shape.can_rotate():
				self.current_shape.rotate()
		elif self.key == "p":
			pause_window = Rectangle(Point(self.column*6, self.row*6), Point(self.column*24, self.row*12))
			pause_window.setFill("white")
			pause_window.draw(self.window)

			pause_text2 = Text(Point(self.column*15, self.row*9-20), "Game Paused")
			pause_text2.setSize(18)
			pause_text2.draw(self.window)

			pause_text = Text(Point(self.column*15, self.row*9+20), "Click to continue")
			pause_text.setSize(14)
			pause_text.draw(self.window)

			self.window.getMouse()
			
			pause_window.undraw()
			pause_text.undraw()
			pause_text2.undraw()


		self.key = None


	def delete_row(self):
		for row in range(self.row):
			blocks_in_row = []
#adds all the blocks in the current row to the list
			for block in self.all_blocks:
				if block.coordinates[1] == row:
					blocks_in_row.append(block)
#checks if there are as many blocks in that row as there are columns and deletes those blocks
			if len(blocks_in_row) == self.column:
				for block in blocks_in_row:
					block.undraw()
					self.all_blocks.remove(block)
#moves all the blocks above it down one row

				for block in self.all_blocks:
					if block.coordinates[1] < row:
						block.move(0,1)
				self.score += 100
				
				
	def create_window(self):				
		tetris_window = Rectangle(Point(0,0), Point(self.column*30,self.row*30))
		tetris_window.draw(self.window)
		tetris_name = Text(Point(self.column*30/2, self.row*30+50), "Tetris")
		tetris_name.setSize(36)
		tetris_name.draw(self.window)
		level_display = Text(Point(self.column*30 + 100, 20), "Level:")
		level_display.setSize(18)
		level_display.draw(self.window)
		score_display = Text(Point(self.column*30 + 100, 80), "Score:")
		score_display.setSize(18)
		score_display.draw(self.window)
		preview_window_text = Text(Point(self.column*30 + 100, 140), "Preview Window")
		preview_window_text.setSize(18)
		preview_window_text.draw(self.window)
		preview_window = Rectangle(Point(self.column*30 + 20, 160), Point(self.column*30 + 180, 320))
		preview_window.draw(self.window)
	
	def keep_score(self):
		self.score_display.undraw()
		self.score_display = Text(Point(self.column*30 + 100, 110), str(self.score))
		self.score_display.setSize(16)
		self.score_display.draw(self.window)

	"""def preview(self):
		if self.next_shape == 0:
			preview_shape = I_shape([int(self.column+3),8])
			preview_shape.draw(self.window)
		elif self.next_shape == 1:
			preview_shape = J_shape([int(self.column+3),8])
			preview_shape.draw(self.window)
		elif self.next_shape == 2:
			preview_shape = L_shape([int(self.column+3),8])
			preview_shape.draw(self.window)
		elif self.next_shape == 3:
			preview_shape = O_shape([int(self.column+3),8])
			preview_shape.draw(self.window)
		elif self.next_shape == 4:
			preview_shape = S_shape([int(self.column+3),8])
			preview_shape.draw(self.window)
		elif self.next_shape == 5:
			preview_shape = T_shape([int(self.column+3),8])
			preview_shape.draw(self.window)
		elif self.next_shape == 6:
			preview_shape = Z_shape([int(self.column+3),8])
			preview_shape.draw(self.window)"""
	

		
# creates a single block using the rectangle class in graphics
class Block(Rectangle):
	def __init__(self, coords, color):
		self.coordinates = coords
		self.point1 = Point(coords[0]*30, coords[1]*30)
		self.point2 = Point((coords[0]*30)+30, (coords[1]*30)+30)
		Rectangle.__init__(self, self.point1, self.point2)
		Rectangle.setFill(self, color)
		Rectangle.setWidth(self, 3)
		
# for y, checks if the space below it is unoccupied based on the list of current top block locations
# need to fix x
	def can_move(self, dx, dy):
		can_move = True

	#makes sure there are no blocks beneath it for moving down
		if dy > 0:
			for blocks in game.all_blocks:
				if [self.coordinates[0], self.coordinates[1]+dy] == blocks.coordinates:
					can_move = False

	#makes sure the block doesn't move too far to the right
		elif dx > 0 and self.coordinates[0] + dx >= game.column:
			can_move = False
	#makes sure the block doesn't move too far to the left
		elif dx < 0 and self.coordinates[0] + dx < 0:
			can_move = False

	#makes sure the block doesn't hit blocks to the side of it
		else:
			for blocks in game.all_blocks:
				if [self.coordinates[0]+dx, self.coordinates[1]] == blocks.coordinates:
					can_move = False
		return can_move


	def move(self, dx, dy):
		Rectangle.move(self, dx*30, dy*30)
		self.coordinates[0] += dx
		self.coordinates[1] += dy


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
			block.move(dx, dy)

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
		self.rotate_options = [0,1]
		self.rotate_position = 0

		block_1_coords = [center_coords[0]-1, center_coords[1]]
		block_2_coords = [center_coords[0]+1, center_coords[1]]
		block_3_coords = [center_coords[0]+2, center_coords[1]]
		list_of_coords = [block_1_coords, center_coords, block_2_coords, block_3_coords]
		Shape.__init__(self, list_of_coords, "blue")
		

	def can_rotate(self):
		can_rotate = []
		if self.rotate_position == 0:
			#left block
			if self.list_of_blocks[0].can_move(1,1) == False:
				can_rotate.append(False)
			#center block doesn't move. right block
			elif self.list_of_blocks[2].can_move(-1,-1) == False:
				can_rotate.append(False)
			elif self.list_of_blocks[3].can_move(-2,-2) == False:
				can_rotate.append(False)
		elif self.rotate_position == 1:
			#bottom block doesn't move or else the shape moves up one
			if self.list_of_blocks[1].can_move(1,1) == False:
				can_rotate.append(False)
			elif self.list_of_blocks[2].can_move(2,2) == False:
				can_rotate.append(False)
			elif self.list_of_blocks[3].can_move(3,3) == False:
				can_rotate.append(False)

		if False in can_rotate:
			return False
		else:
			return True
	
	def rotate(self):
		if self.rotate_position == 0:
			self.list_of_blocks[0].move(1,1)
			self.list_of_blocks[2].move(-1,-1)
			self.list_of_blocks[3].move(-2,-2)
			self.rotate_position = 1
		elif self.rotate_position == 1:
			self.list_of_blocks[1].move(1,1)
			self.list_of_blocks[2].move(2,2)
			self.list_of_blocks[3].move(3,3)
			self.rotate_position = 0
				
class J_shape(Shape):
	def __init__(self, center_coords):
		self.rotate_options = [0,1,2,3]
		self.rotate_position = 0
		block_1_coords = [center_coords[0]-1, center_coords[1]]
		block_2_coords = [center_coords[0]+1, center_coords[1]]
		block_3_coords = [center_coords[0]+1, center_coords[1]+1]
		list_of_coords = [block_1_coords, center_coords, block_2_coords, block_3_coords]
		Shape.__init__(self, list_of_coords, "orange")

	def can_rotate(self):
		can_rotate = []
		if self.rotate_position == 0:
			#left block
			if self.list_of_blocks[0].can_move(1,-1) == False:
				can_rotate.append(False)
			#center block doesn't move. right block
			elif self.list_of_blocks[2].can_move(-1,1) == False:
				can_rotate.append(False)
			#bottom block
			elif self.list_of_blocks[3].can_move(-2,0) == False:
				can_rotate.append(False)
		elif self.rotate_position == 1:
			if self.list_of_blocks[0].can_move(1,2) == False:
				can_rotate.append(False)
			elif self.list_of_blocks[1].can_move(0,1) == False:
				can_rotate.append(False)
			elif self.list_of_blocks[2].can_move(-1,0) == False:
				can_rotate.append(False)
			elif self.list_of_blocks[3].can_move(0,-1) == False:
				can_rotate.append(False)
		elif self.rotate_position == 2:
			if self.list_of_blocks[0].can_move(-1,1) == False:
				can_rotate.append(False)
			# center block doesn't move again
			elif self.list_of_blocks[2].can_move(1,-1) == False:
				can_rotate.append(False)
			elif self.list_of_blocks[3].can_move(2,0) == False:
				can_rotate.append(False)
		elif self.rotate_position == 3:
			if self.list_of_blocks[0].can_move(-1,-1) == False:
				can_rotate.append(False)
			elif self.list_of_blocks[2].can_move(1,1) == False:
				can_rotate.append(False)
			elif self.list_of_blocks[3].can_move(0,2) == False:
				can_rotate.append(False)


		if False in can_rotate:
			return False
		else:
			return True
	
	def rotate(self):
		if self.rotate_position == 0:
			self.list_of_blocks[0].move(1,-1)
			self.list_of_blocks[2].move(-1,1)
			self.list_of_blocks[3].move(-2,0)
			self.rotate_position = 1
		elif self.rotate_position == 1:
			self.list_of_blocks[0].move(1,2)
			self.list_of_blocks[1].move(0,1)
			self.list_of_blocks[2].move(-1,0)
			self.list_of_blocks[3].move(0,-1)
			self.rotate_position = 2
		elif self.rotate_position == 2:
			self.list_of_blocks[0].move(-1,1)
			self.list_of_blocks[2].move(1,-1)
			self.list_of_blocks[3].move(2,0)
			self.rotate_position = 3
		elif self.rotate_position == 3:
			self.list_of_blocks[0].move(-1,-1)
			self.list_of_blocks[2].move(1,1)
			self.list_of_blocks[3].move(0,2)
			self.rotate_position = 0


class L_shape(Shape):
	def __init__(self, center_coords):
		self.rotate_options = [0,1,2,3]
		self.rotate_position = 0
		block_1_coords = [center_coords[0]-1, center_coords[1]]
		block_2_coords = [center_coords[0]+1, center_coords[1]]
		block_3_coords = [center_coords[0]-1, center_coords[1]+1]
		list_of_coords = [block_1_coords, center_coords, block_2_coords, block_3_coords]
		Shape.__init__(self, list_of_coords, "cyan")

	def can_rotate(self):
		can_rotate = []
		if self.rotate_position == 0:
			#left block
			if self.list_of_blocks[0].can_move(1,-1) == False:
				can_rotate.append(False)
			#center block doesn't move. right block
			elif self.list_of_blocks[2].can_move(-1,1) == False:
				can_rotate.append(False)
			#bottom block
			elif self.list_of_blocks[3].can_move(0,-2) == False:
				can_rotate.append(False)
		elif self.rotate_position == 1:
			if self.list_of_blocks[0].can_move(1,2) == False:
				can_rotate.append(False)
			elif self.list_of_blocks[1].can_move(0,1) == False:
				can_rotate.append(False)
			elif self.list_of_blocks[2].can_move(-1,0) == False:
				can_rotate.append(False)
			elif self.list_of_blocks[3].can_move(2,1) == False:
				can_rotate.append(False)
		elif self.rotate_position == 2:
			if self.list_of_blocks[0].can_move(-1,1) == False:
				can_rotate.append(False)
			# center block doesn't move again
			elif self.list_of_blocks[2].can_move(1,-1) == False:
				can_rotate.append(False)
			elif self.list_of_blocks[3].can_move(0,2) == False:
				can_rotate.append(False)
		elif self.rotate_position == 3:
			if self.list_of_blocks[0].can_move(-1,-1) == False:
				can_rotate.append(False)
			elif self.list_of_blocks[2].can_move(1,1) == False:
				can_rotate.append(False)
			elif self.list_of_blocks[3].can_move(-2,0) == False:
				can_rotate.append(False)


		if False in can_rotate:
			return False
		else:
			return True
	
	def rotate(self):
		if self.rotate_position == 0:
			self.list_of_blocks[0].move(1,-1)
			self.list_of_blocks[2].move(-1,1)
			self.list_of_blocks[3].move(0,-2)
			self.rotate_position = 1
		elif self.rotate_position == 1:
			self.list_of_blocks[0].move(1,2)
			self.list_of_blocks[1].move(0,1)
			self.list_of_blocks[2].move(-1,0)
			self.list_of_blocks[3].move(2,1)
			self.rotate_position = 2
		elif self.rotate_position == 2:
			self.list_of_blocks[0].move(-1,1)
			self.list_of_blocks[2].move(1,-1)
			self.list_of_blocks[3].move(0,2)
			self.rotate_position = 3
		elif self.rotate_position == 3:
			self.list_of_blocks[0].move(-1,-1)
			self.list_of_blocks[2].move(1,1)
			self.list_of_blocks[3].move(-2,0)
			self.rotate_position = 0


class O_shape(Shape):
	def __init__(self, center_coords):
		self.rotate_options = [0]
		self.rotate_position = 0
		block_1_coords = [center_coords[0]-1, center_coords[1]]
		block_2_coords = [center_coords[0], center_coords[1]+1]
		block_3_coords = [center_coords[0]-1, center_coords[1]+1]
		list_of_coords = [block_1_coords, center_coords, block_2_coords, block_3_coords]
		Shape.__init__(self, list_of_coords, "red")
	
	def can_rotate(self):
		pass
	def rotate(self):
		pass

class S_shape(Shape):
	def __init__(self, center_coords):
		self.rotate_options = [0,1]
		self.rotate_position = 0
		block_1_coords = [center_coords[0]+1, center_coords[1]]
		block_2_coords = [center_coords[0], center_coords[1]+1]
		block_3_coords = [center_coords[0]-1, center_coords[1]+1]
		list_of_coords = [block_1_coords, center_coords, block_2_coords, block_3_coords]
		Shape.__init__(self, list_of_coords, "green2")

	def can_rotate(self):
		can_rotate = []
		if self.rotate_position == 0:
			#left block
			if self.list_of_blocks[0].can_move(-1,1) == False:
				can_rotate.append(False)
			#center block doesn't move. right block
			elif self.list_of_blocks[2].can_move(-1,-1) == False:
				can_rotate.append(False)
			elif self.list_of_blocks[3].can_move(0,-2) == False:
				can_rotate.append(False)
		elif self.rotate_position == 1:
			#bottom block doesn't move or else the shape moves up one
			if self.list_of_blocks[0].can_move(-1,0) == False:
				can_rotate.append(False)
			elif self.list_of_blocks[1].can_move(0,1) == False:
				can_rotate.append(False)
			elif self.list_of_blocks[2].can_move(1,0) == False:
				can_rotate.append(False)
			elif self.list_of_blocks[3].can_move(2,1) == False:
				can_rotate.append(False)

		if False in can_rotate:
			return False
		else:
			return True
	
	def rotate(self):
		if self.rotate_position == 0:
			self.list_of_blocks[0].move(-1,1)
			self.list_of_blocks[2].move(-1,-1)
			self.list_of_blocks[3].move(0,-2)
			self.rotate_position = 1
		elif self.rotate_position == 1:
			self.list_of_blocks[0].move(-1,0)
			self.list_of_blocks[1].move(0,1)
			self.list_of_blocks[2].move(1,0)
			self.list_of_blocks[3].move(2,1)
			self.list_of_blocks = [self.list_of_blocks[3],self.list_of_blocks[2],self.list_of_blocks[1],self.list_of_blocks[0]]
			self.rotate_position = 0

class T_shape(Shape):
	def __init__(self, center_coords):
		self.rotate_options = [0,1,2,3]
		self.rotate_position = 0
		block_1_coords = [center_coords[0]+1, center_coords[1]]
		block_2_coords = [center_coords[0], center_coords[1]+1]
		block_3_coords = [center_coords[0]-1, center_coords[1]]
		list_of_coords = [block_1_coords, center_coords, block_2_coords, block_3_coords]
		Shape.__init__(self, list_of_coords, "yellow")

	def can_rotate(self):
		can_rotate = []
		if self.rotate_position == 0:
			#left block
			if self.list_of_blocks[0].can_move(-1,1) == False:
				can_rotate.append(False)
			#center block doesn't move. right block
			elif self.list_of_blocks[2].can_move(-1,-1) == False:
				can_rotate.append(False)
			elif self.list_of_blocks[3].can_move(1,-1) == False:
				can_rotate.append(False)
		elif self.rotate_position == 1:
			if self.list_of_blocks[0].can_move(-1,0) == False:
				can_rotate.append(False)
			elif self.list_of_blocks[1].can_move(0,1) == False:
				can_rotate.append(False)
			elif self.list_of_blocks[2].can_move(1,0) == False:
				can_rotate.append(False)
			elif self.list_of_blocks[3].can_move(1,2) == False:
				can_rotate.append(False)
		elif self.rotate_position == 2:
			if self.list_of_blocks[0].can_move(1,-2) == False:
				can_rotate.append(False)
			elif self.list_of_blocks[1].can_move(0,-1) == False:
				can_rotate.append(False)
			elif self.list_of_blocks[2].can_move(1,0) == False:
				can_rotate.append(False)
			elif self.list_of_blocks[3].can_move(-1,0) == False:
				can_rotate.append(False)
		elif self.rotate_position == 3:
			if self.list_of_blocks[0].can_move(1,1) == False:
				can_rotate.append(False)
			elif self.list_of_blocks[2].can_move(-1,1) == False:
				can_rotate.append(False)
			elif self.list_of_blocks[3].can_move(-1,-1) == False:
				can_rotate.append(False)

		if False in can_rotate:
			return False
		else:
			return True
	
	def rotate(self):
		if self.rotate_position == 0:
			self.list_of_blocks[0].move(-1,1)
			self.list_of_blocks[2].move(-1,-1)
			self.list_of_blocks[3].move(1,-1)
			self.rotate_position = 1
		elif self.rotate_position == 1:
			self.list_of_blocks[0].move(-1,0)
			self.list_of_blocks[1].move(0,1)
			self.list_of_blocks[2].move(1,0)
			self.list_of_blocks[3].move(1,2)
			self.rotate_position = 2
		elif self.rotate_position == 2:
			self.list_of_blocks[0].move(1,-2)
			self.list_of_blocks[1].move(0,-1)
			self.list_of_blocks[2].move(1,0)
			self.list_of_blocks[3].move(-1,0)
			self.rotate_position = 3
		elif self.rotate_position == 3:
			self.list_of_blocks[0].move(1,1)
			self.list_of_blocks[2].move(-1,1)
			self.list_of_blocks[3].move(-1,-1)
			self.rotate_position = 0

#needs rotations

class Z_shape(Shape):
	def __init__(self, center_coords):
		self.rotate_options = [0,1]
		self.rotate_position = 0
		block_1_coords = [center_coords[0]+1, center_coords[1]+1]
		block_2_coords = [center_coords[0], center_coords[1]+1]
		block_3_coords = [center_coords[0]-1, center_coords[1]]
		list_of_coords = [block_1_coords, block_2_coords, center_coords, block_3_coords]
		Shape.__init__(self, list_of_coords, "magenta")

	def can_rotate(self):
		can_rotate = []
		if self.rotate_position == 0:
			#left block
			if self.list_of_blocks[0].can_move(-2,0) == False:
				can_rotate.append(False)
			#center block doesn't move. right block
			elif self.list_of_blocks[1].can_move(-1,-1) == False:
				can_rotate.append(False)
			elif self.list_of_blocks[3].can_move(1,-1) == False:
				can_rotate.append(False)
		elif self.rotate_position == 1:
			#bottom block doesn't move or else the shape moves up one
			if self.list_of_blocks[0].can_move(0,-1) == False:
				can_rotate.append(False)
			elif self.list_of_blocks[1].can_move(1,0) == False:
				can_rotate.append(False)
			elif self.list_of_blocks[2].can_move(0,1) == False:
				can_rotate.append(False)
			elif self.list_of_blocks[3].can_move(1,2) == False:
				can_rotate.append(False)

		if False in can_rotate:
			return False
		else:
			return True
	
	def rotate(self):
		if self.rotate_position == 0:
			self.list_of_blocks[0].move(-2,0)
			self.list_of_blocks[1].move(-1,-1)
			self.list_of_blocks[3].move(1,-1)
			self.rotate_position = 1
		elif self.rotate_position == 1:
			self.list_of_blocks[0].move(0,-1)
			self.list_of_blocks[1].move(1,0)
			self.list_of_blocks[2].move(0,1)
			self.list_of_blocks[3].move(1,2)
			self.list_of_blocks = [self.list_of_blocks[3],self.list_of_blocks[2],self.list_of_blocks[1],self.list_of_blocks[0]]
			self.rotate_position = 0

def drop_shapes() :
	while 0 not in game.tops and -1 not in game.tops:
		game.random_shape()
		#game.preview()
		game.add_drop_shape()
		game.delete_row()
		game.keep_score()
		time.sleep(1)

game = Game(12,30)
game.create_window()
game.add_floor()
I = I_shape([4,4])
print(I.list_of_blocks)
drop_shapes()


