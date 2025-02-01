import numpy as np
import pylab as pl


def fourie_quadra(t, N, omega):
    y=0
    for k in range(1, N, 2):
        b_k=0
        c_k=2/(k*np.pi)
        omega_k=omega*k
        y += (b_k*np.cos(omega_k*t))+(c_k*np.sin(omega_k*t))
    return y

def quadra(t, T):
    f= (t/T)%1<0.5
    y=np.zeros_like(t)
    for i in range(len(t)):
        if f[i]:
            y[i]=0.5
        else:
            y[i]=-0.5
    return y

#inserimento dati
N=1000
npunti = 1000
omega=1
T=2*(np.pi/omega)
t=np.linspace(0,4*T,npunti)

#plot
pl.plot(t/T, fourie_quadra(t, N, 1), color='blue', label=f"N= {N}")
#,marker='.',linestyle=''
pl.plot(t/T, quadra(t, T), linestyle="--", color='red')

#bellurie
pl.ylabel('Ricostruzione onda quadra [arb.un.]',fontsize=14)
pl.xlabel('Periodi',fontsize=14)
pl.legend(loc="upper right",fontsize=14)



pl.show()