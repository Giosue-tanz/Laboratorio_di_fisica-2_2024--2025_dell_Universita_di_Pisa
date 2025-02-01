from scipy.optimize import curve_fit
import pylab
import numpy as np
from G import guadagno_quadra

# data load
Directory="/Users/jakit/Desktop/Laboratorio2/Relazione natale obbligatorio/"

NomeFile = 'f_guadagno.txt'
Filename=(Directory+NomeFile)
x=pylab.loadtxt(Filename,unpack=True)

NomeFile = 'Vout_quadra.txt'
Filename=(Directory+NomeFile)
vout,Dvout=pylab.loadtxt(Filename,unpack=True)

vin = np.full_like(vout, 15.76)
Dvin = np.full_like(Dvout, Dvout[0])

y= vout/vin
Dy= y*(np.sqrt((Dvout/vout)**2+(Dvin/vin)**2))

# scatter plot with error bars
pylab.errorbar(x,y,Dy,linestyle = '', color = 'black', marker = '.')

# make the array with initial values (to be carefully adjusted!)
init=400

# set the error (to be modified if effective errors have to be accounted for)
# sigma=Dy/np.sqrt(3)
# w=1/sigma**2

def ff_quadra(f, f_t):
    return guadagno_quadra(f, f_t)

pars_quadra,covm_quadra=curve_fit(ff_quadra,x,y,init,Dy,absolute_sigma=False) # <<<< NOTE THE absolute_sigma option

# calculate the kappasquare for the best-fit funtion
w=1/Dy**2
kappa2_quadra = ((w*(y-ff_quadra(x,*pars_quadra))**2)).sum()

# determine the ndof
ndof_quadra=len(x)-1 # len(init)

# print results on the console
print('f_t quadra', pars_quadra)
# print(covm)
# print (kappa2/ndof, ndof)



NomeFile = 'Vout_seno.txt'
Filename=(Directory+NomeFile)
vout,Dvout=pylab.loadtxt(Filename,unpack=True)

vin = np.full_like(vout, 14.08)
Dvin = np.full_like(Dvout, 0.50)

y= vout/vin
Dy= y*(np.sqrt((Dvout/vout)**2+(Dvin/vin)**2))

# scatter plot with error bars
pylab.errorbar(x,y,Dy,linestyle = '', color = 'purple', marker = '.')

# make the array with initial values (to be carefully adjusted!)
init=400

# set the error (to be modified if effective errors have to be accounted for)
# sigma=Dy/np.sqrt(3)
# w=1/sigma**2

def ff_seno(f, f_t):
    return 1/(np.sqrt(1+(f/f_t)**2))

pars_seno,covm_seno=curve_fit(ff_seno,x,y,init,Dy,absolute_sigma=False) # <<<< NOTE THE absolute_sigma option

# calculate the kappasquare for the best-fit funtion
w=1/Dy**2
kappa2_seno = ((w*(y-ff_seno(x,*pars_seno))**2)).sum()

# determine the ndof
ndof_seno=len(x)-1 # len(init)

# print results on the console
print('f_t seno', pars_seno)
# print(covm)
# print (kappa2/ndof, ndof)



# NomeFile = 'Vout_quadra.txt'
# Filename=(Directory+NomeFile)
# vout,Dvout=pylab.loadtxt(Filename,unpack=True)
#
# vin = np.full_like(vout, 15.76)
# Dvin = np.full_like(Dvout, Dvout[0])
#
# y= vout/vin
# Dy= y*(np.sqrt((Dvout/vout)**2+(Dvin/vin)**2))
#
# # scatter plot with error bars
# pylab.errorbar(x,y,Dy,linestyle = '', color = 'black', marker = '.')
#
# # make the array with initial values (to be carefully adjusted!)
# init=400
#
# # set the error (to be modified if effective errors have to be accounted for)
# # sigma=Dy/np.sqrt(3)
# # w=1/sigma**2
#
# def ff_quadra(f, f_t):
#     return guadagno_quadra(f, f_t)
#
# pars_quadra,covm=curve_fit(ff_quadra,x,y,init,Dy,absolute_sigma=False) # <<<< NOTE THE absolute_sigma option
#
# # calculate the kappasquare for the best-fit funtion
# w=1/Dy**2
# kappa2 = ((w*(y-ff_quadra(x,*pars_quadra))**2)).sum()
#
# # determine the ndof
# ndof=len(x)-1 # len(init)
#
# # print results on the console
# # print('1', pars)
# # print(covm)
# # print (kappa2/ndof, ndof)

#PLOT
xx=np.logspace(2, 4.3, 300)

# bellurie
pylab.rc('font',size=20)
pylab.xlabel('Frequenza [Hz]',fontsize=20)
pylab.ylabel('Guadagno',fontsize=20)
pylab.minorticks_on()
pylab.yscale("log")
pylab.xscale("log")

# AT THE SECOND STEP, YOU MUST REPLACE *pars WITH *init
pylab.plot(xx,ff_quadra(xx,*pars_quadra), color='red', label='fit onda quadra')
pylab.plot(xx,ff_seno(xx,*pars_seno), color='cyan', label='fit onda sinusoidale')

pylab.legend(loc="lower left",fontsize=18)

pylab.show()