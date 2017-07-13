from tetris import *


blocks = [I_shape([1,0]),I_shape([5,0]),I_shape([9,0]),I_shape([6,0])]

for block in blocks:
	block.draw(game.window)
	game.current_shape = block
	game.add_drop_shape("I")
game.window.getMouse()
game.delete_row()
game.window.getMouse()
game.window.close
