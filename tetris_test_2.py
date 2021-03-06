from graphics import *
from tetris import *
 
win = GraphWin("WTP Tetris", 600, 600)
 
wonky = Shape([[10,4],[12,4],[13,4],[15,4],[11,3],[14,3],[10,5],[11,6],[12,7],[13,7],[14,6],[15,5]],"pink")
i = I_shape([1,9])
j = J_shape([7,9])
l = L_shape([9,1])
o = O_shape([1,1])
s = S_shape([5,1])
t = T_shape([1,5])
z = Z_shape([5,5])
 
shapes_list = [wonky, i, j, l, o, s, t, z]
 
for shape in shapes_list:
    shape.draw(win)

win.getMouse()

