import numpy as np
import pylab as pl

def quadra_RC(t, f, f_t, fase):
    N=1000
    omega_t = f_t*(2*np.pi)
    omega = f*(2*np.pi)
    y=0
    for k in range(1, N, 2):
        b_k=0
        c_k=2/(k*np.pi)
        omega_k=omega*k
        g_k=1/np.sqrt(1+(omega_k/omega_t)**2)
        fi_k=-np.arctan(omega_k/omega_t)
        y += (g_k*b_k*np.cos(omega_k*t+fi_k+ fase))+(g_k*c_k*np.sin(omega_k*t+fi_k+ fase))
    return y

def quadra_CR(t, N, f, f_t):
    omega_t = f_t*(2*np.pi)
    omega = f*(2*np.pi)
    y=0
    for k in range(1, N, 2):
        b_k=0
        c_k=2/(k*np.pi)
        omega_k=omega*k
        g_k=1/np.sqrt(1+(omega_t/omega_k)**2)
        fi_k=np.arctan(omega_t/omega_k)
        y += (g_k*b_k*np.cos(omega_k*t+fi_k))+(g_k*c_k*np.sin(omega_k*t+fi_k))
    return y

#inserimento dati
N=1000
npunti = 10000
f=500
T=1/f
f_t=100
fase=np.pi

t=np.linspace(0,4*T,npunti)

#plot
pl.plot(t/T, quadra_RC(t, f, f_t, fase))
pl.plot([], [], ' ', label=f"f= {f}")#linea invisibile 1

#bellurie
pl.ylabel('V_out [arb.un.]',fontsize=14)
pl.xlabel('tempo [t/T]',fontsize=14)
pl.legend(loc="upper right",fontsize=14)

pl.show()