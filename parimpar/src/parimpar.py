# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "rodma"
__date__ = "$17-oct-2015 12:57:28$"
num=1
while num!=0:
    num=input("Ingrese un numero(presione cero para salir):")
    if num==0:
        print "Hasta pronto!"
    else:
        if (num%2)==0:
         print "El numero es par"
        else:
            print "El numero es impar"
    
    
