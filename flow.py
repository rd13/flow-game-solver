# Abstract ALL the things
from flowmatrix import FlowMatrix
from cell import Cell
import copy

class Flow:

    def __init__(self, img):
        self.matrix = FlowMatrix(img)

        print self.matrix.gridsize
        print self.matrix.colours

        self.matrix.printMatrix()

        self.solve()

    def solve(self):

        def search(maze, x, y):

            if (x,y) == self.end:
                # Found a solution
                return True
            elif maze[x][y] == True:
                # Hit a wall
                return False
            elif maze[x][y] == 3:
                return False

            # mark as visited
            maze[x][y] = 3

            # explore neighbors clockwise starting by the one on the right
            if ((x < len(maze)-1 and search(maze, x+1, y))
                or (y > 0 and search(maze, x, y-1))
                or (x > 0 and search(maze, x-1, y))
                or (y < len(maze)-1 and search(maze, x, y+1))):
                return True

            return False

        def checkIfPathConflicts(paths):

            colours = copy.deepcopy(self.matrix.colours)
            colours.pop(colour_index)

            for c in colours:

                dupe = copy.deepcopy(self.matrix.matrix)

                for path in paths:
                    self.matrix.toggleCell(dupe, path)

                self.matrix.toggleCell(dupe, c[0])
                self.matrix.toggleCell(dupe, c[1])
                
                self.end = c[1]

                if search(dupe, c[0][0], c[0][1]) == False:
                    return True
                    

            return False

        def findPaths(maze, start, end):


            result = []
            if start.row < 0 or start.col < 0:
                return False
            if start.row == self.matrix.gridsize or start.col == self.matrix.gridsize:
                return False
            if maze[start.row][start.col] is 1:
                return False

            if start.isequals(end):
                # Start a new path
                result.append([start.tuple()])
                return result

            maze[start.row][start.col] = 1

            nextCells = [x[:] for x in ['']*4]
            nextCells[0] = Cell((start.row + 1, start.col))
            nextCells[2] = Cell((start.row, start.col + 1))
            nextCells[1] = Cell((start.row - 1, start.col))
            nextCells[3] = Cell((start.row, start.col - 1))

            for nextCell in nextCells:
                paths = findPaths(maze, nextCell, end)
                if paths is not False:
                    for i, (path) in enumerate(paths):
                        path.append(start.tuple())

                        if start.tuple() == start_colour:
                            if checkIfPathConflicts(paths[i]):
                                paths[i] = []
                    
                    result.extend(paths)

            maze[start.row][start.col] = 0

            if len(result) == 0:
                return False
            
            return result

        for i, (co) in enumerate(self.matrix.colours):
            
            for cell in co:
                self.matrix.toggleCell(self.matrix.matrix, cell)

            start_colour = co[0]
            colour_index = i

            paths = findPaths(self.matrix.matrix, Cell(co[0]), Cell(co[1]))

            if paths:
                print paths
            
            for cell in co:
                self.matrix.toggleCell(self.matrix.matrix, cell)


    class Thread:
        def add(self):
            pass
        def start(self):
            pass
        def join(self):
            pass


a = Flow('flow6x6.png')
