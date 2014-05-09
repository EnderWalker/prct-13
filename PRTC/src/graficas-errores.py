#!encoding: UTF-8
#Se importan las siguientes librerias
import time
import timeit
import modulo
import matplotlib.pyplot as pl
#Ejemplo modificado de gráfica
start=time.time()
l=[]
e=[]
def error(nro_intervalos,nro_test,umbral):
  er=0
  for i in range (nro_test): #usamos el archivo creado como libreria, modluo.py
    s=modulo.aproxpi(nro_intervalos)
    error=abs(s-modulo.pi)
    if error>=umbral:
      er=er+1
  return ((er/nro_test)*100)
#t_upla=(100,1000,10000,100000)
t_upla=(10,50,100,150, 500, 550, 1000)
for i in range(len(t_upla)):#Funcion referida a los tiempos de carga, que se consigue al ejecutar el programa.
  s=error(t_upla[i],1,0.01)
  e=e+[s]
  print "El porcentaje de error es de: %11.10f" %s
  finish=time.time()-start
  l=l+[finish]
print ('Los tiempos son:')
print l
y=[]
for i in range(len(t_upla)):#Funciones para hacer e imprimir el grafico.
  y=y+[t_upla[i]]
grafica1=pl.subplot(211)
pl.plot(l,y,'m',marker='h')
pl.xlabel('Tiempo empleado')
pl.ylabel('Intervalos')
pl.title('Tiempo frente a cantidad de intervalos')
pl.xlim(0.0, 0.003)
pl.ylim(0.0, 1000.0)
pl.legend(['Tiempos'], loc=4, numpoints=2)
grafica2=pl.subplot(212)
pl.plot(e,y,'c',marker='h')
pl.xlabel('Porcentaje de error')
pl.ylabel('Intervalos')
pl.title('Error~Nº Intervalo')
pl.xlim(0,0,1.0)
pl.ylim(-0.5,1000.0)
pl.legend(['Porcentajes'], loc=4, numpoints=2)
pl.savefig('figura.png',dpi=100)
pl.show()