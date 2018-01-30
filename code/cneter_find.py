import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy import stats
data=np.loadtxt('../data.txt')
xdata=np.arange(8192)
def gaus(x,A,B,C):
    return A*np.exp(-(x-B)**2/(2*C**2))
our_guess=(40000, 207.5,3)
Am,res=curve_fit(gaus,xdata[202:214],data[202:214,0],p0=our_guess)
print(Am[1])
our_guess=(50000, 2353,3)
Cs,res=curve_fit(gaus,xdata[2340:2370],data[2340:2370,2],p0=our_guess)
print(Cs[1])
our_guess=(10000, 4745,4)
Co1,res=curve_fit(gaus,xdata[4725:4765],data[4725:4765,3],p0=our_guess)
print(Co1[1])
our_guess=(14000, 4177,5)
Co2,res=curve_fit(gaus,xdata[4160:4200],data[4160:4200,3],p0=our_guess)
print(Co2[1])
chn=(Am[1],Cs[1],Co1[1],Co2[1])
pE=(59.5409,661.657,1332.492,1173.228)
slope, intercept, r_value, p_value, td_err = stats.linregress(chn,pE)
xi=np.arange(200,5050)
yi=slope*xi+intercept
print(slope)
print(intercept)
print(r_value)
plt.figure()
plt.plot(xi,yi,'r-',chn,pE,'o')
plt.title("Energy Calibration")
plt.xlabel('Chanel Number')
plt.ylabel('Energy,keV')
plt.savefig('../images/Calibration.png')
plt.show()

