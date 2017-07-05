from graphics import *
import tetris

win = GraphWin("WTP Tetris", 300, 300)

block = tetris.Block([5,6],"blue")
block2 = tetris.Block([1,2],"green")
block3 = tetris.Block([7,4],"orange")
block.draw(win)
block2.draw(win)
block3.draw(win)


win.getMouse()
