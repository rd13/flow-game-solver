from flowimage import FlowImage

class FlowMatrix:

    def __init__(self, img):

        self.flow = FlowImage(img)

        self.gridsize = self.flow.gridsize
        self.colours = self.flow.colours

        self.constructMatrix(self.gridsize, self.colours)

    def constructMatrix(self, gridsize, colours):

        matrix = [x[:] for x in [[0]*gridsize]*gridsize]

        for c1,c2 in colours:
            matrix[c1[0]][c1[1]] = 1
            matrix[c2[0]][c2[1]] = 1
            
        self.matrix = matrix

    def toggleCell(self, matrix, cell):
        matrix[cell[0]][cell[1]] = 1 if matrix[cell[0]][cell[1]] == False else 0

    def printMatrix(self):
        for i1, row in enumerate(self.matrix):
            for i2, col in enumerate(row):
                print "#|" if col else "_|",
            print '\n',