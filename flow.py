# Abstract ALL the things
from flowimage import FlowImage
from flowmatrix import FlowMatrix
from cell import Cell

class Flow:

    def __init__(self, img):
        self.flow = FlowImage(img)
        self.matrix = FlowMatrix(self.flow.gridsize, self.flow.colours)

        print self.flow.gridsize
        print self.flow.cell_spacing
        print self.flow.colours

        self.matrix.printMatrix()


    def toggleMaze(self):
        123
    def solve(self):
        123
    def printPaths(self):
        123





a = Flow('flow5x5.jpg')
a.solve()
a.printPaths()