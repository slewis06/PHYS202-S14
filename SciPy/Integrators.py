
import numpy as np
import matplotlib.pyplot as plt

import scipy.integrate as integrate
from scipy.integrate import dblquad
from scipy.integrate import tplquad

def trapz(func,start,end,Num_steps):
    """
    Trapz takes an equation (func), start and end points, and the number of trapezoids you want to use.
    Trapz then uses this to calculate the integral (I) from start to end using trapezoids.
    """
    h = (end-start)/Num_steps
    k = np.arange(1,Num_steps)
    I = h*(0.5*func(start) + 0.5*func(end) + func(start+k*h).sum())
    
    return I

def simps(func,start,end,Num_steps):
    """
    Simps takes an equation (func), start and end points, and the number of quadratic curves
    you want to use. Simps then uses this to calculate the integral (I) from start to end
    using quadratic curves as opposed to straight lines.
    """
    h = (end-start)/Num_steps
    k1 = np.arange(1,Num_steps/2+1)
    k2 = np.arange(1,Num_steps/2)
    I = (1./3.)*h*(func(start) + func(end) + 4.*func(start+(2*k1-1)*h).sum() + 2.*func(start+2*k2*h).sum())
    
    return I