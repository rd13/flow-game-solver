class Cell:
    def __init__(self, ref):
        self.row = ref[0]
        self.col = ref[1]
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