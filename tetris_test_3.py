from graphics import *
from tetris import *
 
#game = Game(12,20)
shape_letter_list = ["I","J","L","O","S","T","Z"]
 
for shape in shape_letter_list:
    game.add_drop_shape(shape)

