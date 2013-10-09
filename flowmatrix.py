class FlowMatrix:

    def __init__(self, gridsize, colours):
        self.constructMatrix(gridsize, colours)

    def constructMatrix(self, gridsize, colours):

        matrix = [x[:] for x in [[0]*gridsize]*gridsize]

        for c1,c2 in colours:
            matrix[c1[0]][c1[1]] = 1
            matrix[c2[0]][c2[1]] = 1
            
        self.matrix = matrix

    def printMatrix(self):
        for i1, row in enumerate(self.matrix):
            for i2, col in enumerate(row):
                print "#|" if col else "_|",
            print '\n',