class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
    def isequals(self, obj):
        if self == obj:
            return True
        elif (obj == None) or (type(obj) != type(self)):
            return False
        elif self.row == obj.row and self.col == obj.col:
            return True
        else: 
            return False
    def tuple(self):
        return (self.row,self.col)