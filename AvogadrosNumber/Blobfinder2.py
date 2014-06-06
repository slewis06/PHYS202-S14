
class Blob():
    def __init__(self):
        # construct an empty blob
        self.pixels = []
    #def __str__(self):
        #return "blob mass = %d" % (self.mass())
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
            if r+g+b <= threshold: 
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
                
          
def BlobFinder(picture, tau): #Tau of 180 works for milk, 600 works for run4.
    """
    picture = picture from file.
    tau = brightness threshold used in monochrome.
    
    Uses the monochrome function to invert the picture color so that the count function
    can then be called which runs through each pixel, finding a blob, filling it, then 
    appending it to a list.
    """
    float(tau)
    monochrome(picture, tau)
    #create list of blobs from picture.
    LstOfBlobs = count(picture)
    #return list
    return LstOfBlobs

def countbeads(P,lst):
    """
    P = minimum mass of a blob for it to be considered a 'bead'.
    lst = List of Blobs gained from BlobFinder function.
    
    countbeads takes the list of blobs of all sizes from the BlobFinder function and itterates
    through each blob and appends them to a new list if the blob has a mass (number of pixels)
    greater than P. This eliminates any one pixel 'noise' particles in the picture. The resulting
    list of 'Big Blobs' can also be reffered to as a list of 'beads'. The function then returns 
    the length of the list to see how many beads are present in the picture.
    """
    #initialize list
    LstOfBigBlobs = []
    #itterate through list.
    for b in lst:
        #find mass of each blob.
        x = b.mass()
        if x >= P:
            #append blob to new list if mass is greater than the value P given by the user.
            LstOfBigBlobs.append(b)
    return len(LstOfBigBlobs)

def getbeads(P,lst):
    """
    P = minimum mass of a blob for it to be considered a 'bead'.
    lst = List of Blobs gained from BlobFinder function.
    
    get takes the list of blobs of all sizes from the BlobFinder function and itterates
    through each blob and appends them to a new list if the blob has a mass (number of pixels)
    greater than P. This eliminates any one pixel 'noise' particles in the picture. The resulting
    list of 'Big Blobs' can also be reffered to as a list of 'beads'. The function then returns 
    the list of beads (LstOfBigBlobs).
    """
    #initialize list
    LstOfBigBlobs = []
    #itterate through list.
    for b in lst:
        #find mass of each blob.
        x = b.mass()
        if x >= P:
            #append blob to new list if mass is greater than the value P given by the user.
            LstOfBigBlobs.append(b)
    return LstOfBigBlobs