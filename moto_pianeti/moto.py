#
# L'esercizio consiste, sostanzialmente, nell'utilizzare l'algoritmo Velocity-Verlet per risolvere equazioni differenziali ordinarie
# L'esercizio parte dal problema fisico del moto di un pianeta all'interno del campo gravitazionale solare (senza correzione relativistica) e l'idea è:
# A) Disegnare diversi tipi di orbite, di diversa eccentricità;
# B) Verificare la seconda legge di Keplero dA/dt = 0 per un'orbita ellittica.
# La teoria verrà accennata via via che servirà.
#
#

#%matplotlib inline
import matplotlib
from numpy import *
from matplotlib.pyplot import *
#from pylab import *
#pi=3.14
N=1000       #numero di passi
tau=0.001    #yr  => è il time-step, in anni.
GM=4*pi**2   #(AU^3)/(yr^2)
time=linspace(0,N*tau,N)

def orbit(x0,y0,vx0,vy0):
    x=zeros(N)
    y=zeros(N)
    vx=zeros(N)
    vy=zeros(N)
    r=zeros(N)
    
    x[0]=x0
    y[0]=y0
    vx[0]=vx0
    vy[0]=vy0
    
    r[0]=sqrt(x[0]**2+y[0]**2)  #raggio
    
    for i in range(N-1):      #il ciclo deve andare fino a N-1 perchè altrimenti x, y, vx e vy non
                              #avrebbero più posti disponibili per salvare i valori
        
        # Implementazione dell'algoritmo velocity verlet

        ax_i1=-GM*x[i]/r[i]**3 #componente x dell'accelerazione all'istante i-esimo
        ay_i1=-GM*y[i]/r[i]**3 #componente y dell'accelerazione all'istante i-esimo
        
        x[i+1]=x[i]+vx[i]*tau+tau*tau*ax_i1/2
        y[i+1]=y[i]+vy[i]*tau+tau*tau*ay_i1/2
        
        r[i+1]=sqrt(x[i+1]**2+y[i+1]**2) #aggiorno il raggio per calcolare la nuova accelerazione
        
        ax_i2=-GM*x[i+1]/r[i+1]**3 #componente x dell'accelerazione all'istante (i+1)-esimo
        ay_i2=-GM*y[i+1]/r[i+1]**3 #componente y dell'accelerazione all'istante (i+1)-esimo
        
        vx[i+1]=vx[i]+(ax_i1+ax_i2)*tau/2
        vy[i+1]=vy[i]+(ay_i1+ay_i2)*tau/2
        
    return x,y,vx,vy,r

#  Esempio di utilizzo della funzione 
#  "Orbita rettilinea"
#

x0=.5
y0=0.
vx0=12
vfuga=sqrt(2*GM/x0)  # attenzione, questo è il valore massimo affinché il pianeta non sfugga dall'attrazione solare
vy0=0.
x,y,vx,vy,r=orbit(x0,y0,vx0,vy0)
# si può sostituire vx0 > vfuga nella funzione sopra, se si vuole studiare il caso in cui il pianeta sfugge

figure(1)
plot(x,y,label='Orbita rettilinea')
plot(0,0,'x')
xlim([-1,1])
xlabel('x ($AU$)')
ylabel('y ($AU$)')
grid()
legend()

#figure(2)
#plot(time,r,label='Distanza in funzione del tempo')
#xlabel('Time (yr)')
#ylabel('r(t) ($AU$)')
#grid()
#legend(loc=2)

#show()

#  Esempio di utilizzo della funzione 
#  "Orbita circolare"
# Eccentricità pari a 0
# Disegno due orbite con raggio diverso

x0=2.
y0=0.
vx0=0.
vy0=2*pi/sqrt(x0)   # Si ricava dalla teoria:  v0= 2*pi*r/T, con T periodo dell'orbita. Ma T si esplicita attraverso la terza legge di Keplero
# e si sostituisce dentro quell'espressione.
# T^2 = 4*pi^2 * r^3 / GM. Togliendo le unità => T= sqrt(r^3).

x1=1.
y1=0.
vx1=0.
vy1=2*pi/sqrt(x1)
x,y,vx,vy,r=orbit(x0,y0,vx0,vy0)
x1,y1,vx1,vx1,r1=orbit(x1,y1,vx1,vy1)

e=1-min(r)/2
e1=1-min(r1)
print ("Orbita circolare")
print ('eccentricità per r=x0: ',e)
print ('eccentricità per r=x1: ',e1)
print ("")


figure(1)
plot(x,y,label='Orbita circolare. r=$x_0$')
plot(x1,y1,label='Orbita circolare. r=$x_1$')
plot(0,0,'x')
axis('equal')
xlabel('x ($AU$)')
ylabel('y ($AU$)')
title('Grafico dell\'orbita')
legend(loc=4,fontsize=9)
grid()

#figure(2)
#plot(time,r,label='Distanza in funzione del tempo')
#title('Distanza in un\'orbita circolare')
#ylim([1,3])
#xlabel('Time (yr)')
#ylabel('r(t) ($AU$)')
#grid()
#legend()

#draw() #attenzione, questo, rispetto a show() fa andare avanti il programma



#  Esempio di utilizzo della funzione                                                                                                                     
#  "Orbita ellittica"                                                                                                                                   
# Eccentricità pari tra 0 ed 1                                                                                                                               
# Disegno due orbite con raggio diverso                                                                                                                   


x0=1
y0=0.
vx0=0.
vy0=2*pi/sqrt(x0)-1
N=1000

x,y,vx,vy,r=orbit(x0,y0,vx0,vy0)

plot(x,y,label='Orbita ellittica')
plot(0,0,'x')
axis('equal')
xlabel('x ($AU$)')
ylabel('y ($AU$)')
legend()
grid()

a=(min(r)+max(r))/2
e=1-min(r)/a     # Nota che per l'orbita ellittica l'eccentricità si può calcolare così:
# e = 1 - r_min/r0, dove r_min = distanza minima del pianeta dal sole
# r0 = raggio dell'orbita nel caso fosse circolare

print ('Orbita ellittica')
print ('L\'eccentricità è: ',e)

draw()

# Verifica della seconda legge di Keplero:
# Il raggio vettore che parte dal fuoco dell'orbita e giunge fino al pianeta che sta eseguendo il suo moto spazza aree uguali in intervalli di tempo uguali.
# Questa legge, detta "Legge delle aree", è dimostrabile attraverso la conservazione del momento angolare in quanto, se questo è conservato (come nel caso delle orbite dei pianeti), la velcità angolare e quella aerolare sono costanti. Questa legge può essere verificata computazionalmente come segue.


A=zeros(N)

for i in range(len(x)):
    if i!=N-1:
        A[i]=x[i]*y[i+1]-x[i+1]*y[i]
    else:
        A[i]=A[i-1]
figure(2)   # questo permette di creare finestre diverse
plot(time,A)
title('Area in funzione del tempo')
ylim([0,0.01])
ylabel('dA/dt ($AU^2\cdot yr^{-1}$)')
xlabel('Time (yr)')
grid()

print ("Dalla figura 2 si vede che dA/dt = 0, verificando la seconda legge di Keplero")
show()  # ferma il programma
