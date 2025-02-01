import numpy as np
import pylab as pl


def fourie_triangolare(t, N, omega):
    y=0
    for k in range(1, N, 2):
        b_k=(2/(k*np.pi))**2
        c_k=0
        omega_k=omega*k
        y += (b_k*np.cos(omega_k*t))+(c_k*np.sin(omega_k*t))
    return y

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

# #inserimento dati
# omega=1
# T=2*(np.pi/omega)
# t=np.linspace(0,4*T,300)
#
# pl.plot(t/T, fourie_triangolare(t, 200, 1))

#inserimento dati
N=1000
npunti = 10000
f=1
T=1/f
f_t=100
fase=0

t=np.linspace(0,4*T,npunti)

pl.plot(t/T, triangolare_RC(t, f, f_t, fase))

pl.show()