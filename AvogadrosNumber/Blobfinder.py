
class Blob():
    def __init__(self):
        self.pixels = []
    def add(self, i, j):
        pass
        
    
    def BlobFinder(picture, threshold):
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