import numpy as np
import pylab as pl

def triangolare_RC(t, f, f_t, fase):
    N=1000
    omega_t = f_t*(2*np.pi)
    omega = f*(2*np.pi)
    y=0
    for k in range(1, N, 2):
        b_k=(2/(k*np.pi))**2
        c_k=0
        omega_k=omega*k
        g_k=1/np.sqrt(1+(omega_k/omega_t)**2)
        fi_k=-np.arctan(omega_k/omega_t)
        y += (g_k*b_k*np.cos(omega_k*t+fi_k+ fase))+(g_k*c_k*np.sin(omega_k*t+fi_k+ fase))
    return y

def quadra_RC(t, N, f, f_t):
    omega_t = f_t*(2*np.pi)
    omega = f*(2*np.pi)
    y=0
    for k in range(1, N, 2):
        b_k=0
        c_k=2/(k*np.pi)
        omega_k=omega*k
        g_k=1/np.sqrt(1+(omega_k/omega_t)**2)
        fi_k=-np.arctan(omega_k/omega_t)
        y += (g_k*b_k*np.cos(omega_k*t+fi_k))+(g_k*c_k*np.sin(omega_k*t+fi_k))
    return y

def guadagno_quadra(f, f_t):
    N=1000
    npunti = 1000
    y=[]

    for i in f:
        T=1/i
        t=np.linspace(0,4*T,npunti)
        max=np.max(quadra_RC(t,N,i,f_t))
        min=np.min(quadra_RC(t,N,i,f_t))
        y.append(max-min)

    return y

def guadagno_seno(f, f_t):
    y=1/np.sqrt(1+(f/f_t)**2)
    return y

def guadagno_triangolare(f, f_t):
    N=1000
    npunti = 1000
    y=[]

    for i in f:
        T=1/i
        t=np.linspace(0,4*T,npunti)
        max=np.max(triangolare_RC(t,i,f_t,0))
        min=np.min(triangolare_RC(t,i,f_t,0))
        y.append(max-min)

    return y

N=1000
npunti = 1000
f=np.arange(1,500,3)
#f=np.array([3.5, 10.4, 15.2, 16.8, 20.3, 25.5, 32.5, 44.34, 53.2, 58.8])
f_t=100

# y=[]
#
# for i in f:
#     T=1/i
#     t=np.logspace(0,4*T,npunti)
#     max=np.max(quadra_RC(t,N,i,f_t))
#     min=np.min(quadra_RC(t,N,i,f_t))
#     y.append(max-min)
#     print(i)

y_quadra=guadagno_quadra(f, f_t)
y_triangolare=guadagno_triangolare(f, f_t)

pl.plot(f,y_quadra, label="quadra")
pl.plot(f, 1/np.sqrt(1+(f/f_t)**2), label="sinusoidale")
pl.plot(f,y_triangolare, label="triangolare")
pl.xscale("log")
pl.yscale("log")
pl.ylabel('Guadagno',fontsize=20)
pl.xlabel('Frequenza [Hz]',fontsize=20)

pl.legend(loc="lower left",fontsize=18)

pl.show()