
import numpy as np
import matplotlib.pyplot as plt

def twoforward(x,y):
    """
    Finds the slope of an array of values from the first to the
    second to last entry. The slope of the second
    to last entry is then calculated using backwards diff.
    """
    dydx = np.zeros(y.shape,float)
    dydx[0:-1] = np.diff(y)/np.diff(x)
    dydx[-1] = (y[-1] - y[-2])/(x[-1] - x[-2])
    return dydx

def twocentered(x,y):
    """
    The slope of an array of values is calculated by taking the difference
    of two points adjacent to the point in question.
    The slope of the two endpoint are then calulated using forwards
    and backwards difference.
    """
    dydx = np.zeros(y.shape,float)
    dydx[1:-1] = (y[2:] - y[:-2])/(x[2:] - x[:-2])
    dydx[0] = (y[1] - y[0])/(x[1] - x[0])
    dydx[-1] = (y[-1] - y[-2])/(x[-1] - x[-2])
    return dydx

def fourcentered(x,y):
    """
    Takes a point in an array (that isnt the first, second, second-to-last, or last) 
    and computes the slope of the function at that point by subtracting values from the 
    four values on either side. The first and second array values have their derivative 
    calculated using the forward difference. The last two array values have their
    derivative calculated with the backwards difference method.
    """
    dydx2 = np.zeros(y.shape,float)
    h = x[1] - x[0]
    dydx2[2:-2] = (y[0:-4] - 8*y[1:-3] + 8*y[3:-1] - y[4:])/(12*h)
    
    dydx2[0:2] = np.diff(y[0:2])/np.diff(x[0:2])
    dydx2[-2:-1] = (y[-2:-1] - y[-1:])/(x[-2:-1] - x[-1:])
    return dydx2