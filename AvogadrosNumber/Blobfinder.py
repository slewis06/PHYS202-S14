
class Blob():
    def __init__(self):
        # construct an empty blob
        self.pixels = []
    def __str__(self):
        return "blob mass = %d" % (self.mass())
    def add(self, i, j):
        #add a pixel (i, j) to the blob
        self.pixels.append((i,j))
    def mass(self):
        # return number of pixels added = its mass
        self.mass = len(self.pixels)
        return self.mass
    def distanceTo(self, b):
        # return distance between centers of masses of this blob and b
        x1 = self.centerOfMass()[0]
        x2 = b.centerOfMass()[0]
        y1 = self.centerOfMass()[1]
        y2 = b.centerOfMass()[1]
        
        dist = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
        return dist
    def centerOfMass(self):
        # return tuple of (x,y) values for this blob's center of mass
        # format center-of-mass coordinates with 4 digits to right
        # of decimal point
        x = 0
        y = 0
        for coord in self.pixels:
            x += coord[0]
            y += coord[1]
        x_avg = x/(len(self.pixels))
        y_avg = y/(len(self.pixels))
        return [x_avg, y_avg]
    #def __repr__(self):
        #return "<Blob mass:%s center of mass:%s>" % (self.mass, self.centerOfMass)
    
def monochrome(picture, threshold):
    """loops over the pixels in the loaded image, 
    replacing the RGB values of each with either 
    black or white depending on whether its total 
    luminance is above or below some threshold 
    passed in by the user"""
    black = (0, 0, 0)
    white = (255, 255, 255)
    
    xsize, ysize = picture.size
    temp = picture.load()
    for x in range(xsize):
        for y in range(ysize):
            r,g,b = temp[x,y]
            if r+g+b >= threshold: 
                temp[x,y] = black
            else:
                temp[x,y] = white
    #return picture
                
def fill(picture, xsize, ysize, xstart, ystart):
    """keep a list of pixels that need to be looked at, 
    but haven't yet been filled in - a list of the (x,y) 
    coordinates of pixels that are neighbors of ones we have 
    already examined.  Keep looping until there's nothing 
    left in this list"""
    queue = [(xstart,ystart)]
    blobby = Blob()
    while queue:
        BLACK = (0,0,0)
        RED = (255,0,0)
        x,y,queue = queue[0][0], queue[0][1], queue[1:]
        if picture[x,y] == BLACK:
            picture[x,y] = RED
            blobby.add(x,y)
            if x > 0:
                queue.append((x-1,y))
            if x < (xsize-1):
                queue.append((x+1,y))
            if y > 0:
                queue.append((x, y-1))
            if y < (ysize-1):
                queue.append((x, y+1))
    return blobby

#Modified to accept which fillfunction to use
def count(picture):
    """scan the image top to bottom and left to right using a nested loop.
    when black pixel is found, increment the count, then call the fill
    function to fill in all the pixels connected to that one."""
    xsize, ysize = picture.size
    temp = picture.load()
    LstOfBlobs = []
    
    result = 0
    BLACK = (0,0,0)
    RED = (255,0,0)
    for x in range(xsize):
        for y in range(ysize):
            if temp[x,y] == BLACK:
                LstOfBlobs.append(fill(temp,xsize,ysize,x,y))
    return LstOfBlobs
                
          
def BlobFinder(picture, tau):
    float(tau)
    monochrome(picture, tau)
    LstOfBlobs = count(picture)
    return LstOfBlobs

def countbeads(P,lst):
    LstOfBigBlobs = []
    for b in lst:
        x = b.mass()
        print x
        if x >= P:
            LstOfBigBlobs.append(x)
    return len(LstOfBigBlobs)

def getbeads(P,lst):
    LstOfBigBlobs = []
    for b in LstOfBlobs:
        x = b.mass()
        if x >= P:
            LstOfBigBlobs.append(x)
    return LstOfBigBlobs