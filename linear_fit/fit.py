import pylab
import numpy
from scipy.optimize import curve_fit
x,Dx,y,Dy=pylab.loadtxt("data.txt",unpack=True)

# Si usa il modulo subplot per mettere due grafici in una singola figura
#
pylab.suptitle("La mia prima retta di regressione lineare", size=18)
pylab.subplot(2,1,2)
pylab.errorbar(x,y,Dy,Dx,linestyle = "", color = "black", marker = "o")
pylab.rc("font",size=18)
pylab.xlabel("$\Delta A$  [A]",size=18)
pylab.ylabel("$B$  [B]", size=18)
pylab.minorticks_on()


# Approccio analitico alla minimizzazione => moltiplicatori di Lagrange (alla fine del file: ci sono le formule da utilizzare già scritte).
# Approccio analitico: più affidabile, meno affetta da problemi di accuratezza matematica, non richiede conoscenze
# preliminari sui parametri della funzione da minimizzare. Può essere matematicamente complessa da fare, specie per funzioni complicate.
# Approccio numerico (pacchetto scipy.optimize). Algoritmo tipicamente usato: Levenberg-Marquardt (LMA).
# Si cercano minimini locali del Chi^2
# Attenzione: è richiesto fornire dei valori iniziali dei parametri, da cui possa partire per cercare il minimo.
# Come si trovano questi valori? Guardando i dati / studiando "teoricamente" il modello!

#Valori iniziali parametri

init=(0,2)
#
#

sigma=Dy
w=1/sigma**2

#Definizione funzione di fit 

def ff(x, aa, bb):
    return aa+bb*x
# Routine di fit numerico
pars,covm=curve_fit(ff,x,y,init,sigma)

chi2 = ((w*(y-ff(x,pars[0],pars[1]))**2)).sum()
ndof=len(x)-len(init)
# Print dei parametri del best fit
print ("Parametri del best fit:")
print(pars)

# Print della matrice di covarianza
print ("Matrice di covarianza:")
print(covm)
print ("I valori fuori diagonale indicano quanto la variazione di un parametro debba essere compensata dall'altro a parità di fit")
print ("")
print ("Chi quadro e numero di gradi di libertà:")
print (chi2, ndof)
print ("Parametri del fit con loro incertezza, radice quadrata degli elementi diagonali della matrice di covarianza")
print("a (intercetta) = ", pars[0], "+/-", numpy.sqrt(covm[0,0]))
print("b (coeff. angolare) = ", pars[1], "+/-", numpy.sqrt(covm[1,1]))
print ("Coeff. di correlazione (o covarianza normalizzata):")
print ("Se |norm cov| > 0.8 si dice che i dati sono fortemente correlati (o anticorrelati)")
print("norm cov = ", covm[0,1]/(numpy.sqrt(covm[0,0]*covm[1,1])))
xx=numpy.linspace(min(x),max(x),100)
pylab.plot(xx,ff(xx,pars[0],pars[1]), color="red")

# 
print ("Definizione di residuali normalizzati: r_i = (y_i - f(x_i))/sigma_i")

# In teoria, r_i dovrebbe essere descritto da una gaussiana a media nulla e varianza unitaria
#

# 
#
#

pylab.subplot(2,1,1)
# Costruzione dell'array dei residuali normalizzati
r = (y-ff(x,pars[0],pars[1]))/sigma
# Accorgimenti estetici
pylab.rc("font",size=16)
pylab.ylabel("Norm. res.",size=18)
pylab.minorticks_on()
# Set del range y del plot dei residuali
pylab.ylim((-40,25))
# Plot dei residuali
pylab.plot(x,r,linestyle="--",color="blue",marker="o")
pylab.savefig("Bestfit.pdf")
pylab.show()
