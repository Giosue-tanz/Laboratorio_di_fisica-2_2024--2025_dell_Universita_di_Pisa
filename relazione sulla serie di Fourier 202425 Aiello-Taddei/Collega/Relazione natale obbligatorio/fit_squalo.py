from scipy.optimize import curve_fit
import pylab
import numpy as np
from RC import quadra_RC

# data load
Filename = 'data c.txt'

x, y=pylab.loadtxt(Filename,unpack=True)

#Temporary
Dy=np.full_like(y, 1)

# scatter plot with error bars
pylab.errorbar(x,y,Dy,linestyle = '', color = 'black', marker = '.')

# make the array with initial values (to be carefully adjusted!)
f=1/(np.max(x)/4)
init=(500e-6, 500e-6, 3000, 1600, np.pi-np.pi)

# set the error (to be modified if effective errors have to be accounted for)
# sigma=Dy/np.sqrt(3)
# w=1/sigma**2

def ff(x, f, f_t, a, off, fase):
    return (a*quadra_RC(x, f, f_t, fase))+off

pars,covm=curve_fit(ff,x,y,init,Dy,absolute_sigma=False) # <<<< NOTE THE absolute_sigma option

# calculate the kappasquare for the best-fit funtion
w=1/Dy**2
kappa2 = ((w*(y-ff(x,*pars))**2)).sum()

# determine the ndof
ndof=len(x)-len(init)

# print results on the console
print('f:', "%.2f" % (pars[0]*(10**6)))
print('f_t:', "%.2f" % (pars[1]*(10**6)))
print('A:', "%.2f" % pars[2])
print('offset:', "%.2f" % pars[3])
print('fase:', "%.2f" % pars[4])
print(covm)
print (kappa2/ndof, ndof)

xx=np.linspace(np.min(x), np.max(x), 800)

pylab.plot(xx,ff(xx,*pars), color='red')

# bellurie
pylab.rc('font',size=16)
pylab.ylabel('V_out [digit]',fontsize=18)
pylab.xlabel('tempo [$\mu$s]',fontsize=18)
pylab.minorticks_on()

# f=1000
# T=1/f
# f_t=400
#
# t=np.linspace(0,4*T,npunti)
#
# #plot
# pl.plot(t/T, ff(t, f, f_t), color='red')

pylab.show()