from graphics import *
import tetris_day1

win = GraphWin("WTP Tetris", 300, 300)

block = tetris_day1.Block([5,6],"blue")
block2 = tetris_day1.Block([1,2],"green")
block3 = tetris_day1.Block([7,4],"orange")
block.draw(win)
block2.draw(win)
block3.draw(win)


win.getMouse()