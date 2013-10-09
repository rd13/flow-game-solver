import cv2
import numpy as np

class FlowImage:
    def __init__(self, img):
        self.img = cv2.imread(img)
        self.img_gray = cv2.cvtColor(self.img,cv2.COLOR_BGR2GRAY)
        self.getGrid()
        self.getColours()

    def getGrid(self):
        edges = cv2.Canny(self.img_gray,150,200,apertureSize = 3)
        lines = cv2.HoughLinesP(edges,1,np.pi/180,275, minLineLength = 600, maxLineGap = 100)[0].tolist()

        for x1,y1,x2,y2 in lines:
            for index, (x3,y3,x4,y4) in enumerate(lines):
                if y1==y2 and y3==y4: # Horizontal Lines
                    diff = abs(y1-y3)
                elif x1==x2 and x3==x4: # Vertical Lines
                    diff = abs(x1-x3)
                else:
                    diff = 0

                if diff < 10 and diff is not 0:
                    del lines[index]

        self.gridsize = (len(lines) - 2) / 2

        # The space between two lines
        cell_spacing = [(L[0]) for L in lines if L[0] == L[2]]
        cell_spacing = sorted(cell_spacing)
        cell_spacing = cell_spacing[0:2]
        self.cell_spacing = reduce(lambda a,b: b-a, cell_spacing)

    def getColours(self):
        # Returns a list of colours, and their positions within the flow grid
        circles = cv2.HoughCircles(self.img_gray,cv2.cv.CV_HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=10,maxRadius=50)
        circles = np.uint16(np.around(circles))

        colours = []
        centre_points = []
        grouped = []

        for i in circles[0,:]:
            # RGB Values
            colours.append(self.img[i[1], i[0]])
            # X/Y Coordinates of the center point of each circle
            centre_points.append((i[1],i[0]))

        # Count the number of unique coloured circles
        for i1, (b1,g1,r1) in enumerate(colours):
            for i2, (b2,g2,r2) in enumerate(colours):

                # Match colours that are similar i.e. RGB triplet is within an acceptable similarity threshold
                diff = abs(abs(int(r1) - int(r2)) + abs(int(g1) - int(g2)) + abs(int(b1) - int(b2)))
                if diff < 20 and diff is not 0:
                    colours[i1] = colours[i2]

        # Calculate cell locations e.g. Green (Start/End) = [(X,Y),(X,Y)]
        for i1, (b1,g1,r1) in enumerate(colours):
            for i2, (b2,g2,r2) in enumerate(colours):
                if b1 == b2 and g1 == g2 and r1 == r2 and i2 > i1:
                    colour1 = (centre_points[i1][0]/self.cell_spacing,centre_points[i1][1]/self.cell_spacing)
                    colour2 = (centre_points[i2][0]/self.cell_spacing,centre_points[i2][1]/self.cell_spacing)
                    grouped.append([colour1,colour2])

        self.colours = grouped