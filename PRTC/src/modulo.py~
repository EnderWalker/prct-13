#! /usr/bin/python
#!encoding: UTF-8

import sys

pi=3.1415926535897931159979634685441852
#Código para aproximar el valor de pi, creado en las anteriores prácticas
def aproxpi(fin):
  if fin>0:
    suma=0
    for i in range(1,fin+1):
      a=(i-1.0)/fin
      b=(i+0.0)/fin
      xi=(i-0.5)/fin
      fxi=4.0/(1.0+xi*xi)
      suma+=fxi
    aprox=suma/fin
  return aprox
#Comprovaciones de la función
if __name__=="__main__":
   if (len(sys.argv)==3):
    p1=int(sys.argv[1])
    p2=int(sys.argv[2])
   else:
    print "En esta función se usaran los valores 10 y 10. Dentro de la función usted deverá introducir los números"
    p1=10
    p2=10
   l=[]
   for i in range(1,p2+1):
     p1=p1*i
     s=aproxpi(p1)
     print "El valor aproximado de PI es: %11.10f" % s
     l=l+[s]
   print l
   

