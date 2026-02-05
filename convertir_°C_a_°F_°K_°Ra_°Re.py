# Programa para convertir grados °C a °F,°K,°Ra y °Re

#Librerias
import math

#-----
#input
#-----

print("                                         ")
print("     Convertir °C a °F,°K,°Ra y °Re      ")
print("                                         ")


C=int(input("Digite el valor de grados centigrados: "))

#----------
#Processing
#----------

F=C*1.8+32
K=C+273.15
Ra=C*1.8+491.67
Re=C*0.8

#-------
#output
#------

print("                      ")
print("      Resultados      ")
print("                      ")
print("Grados Fahrenheit: " +str(F))
print("                           ")
print("Grados Kelvin: " +str(K))
print("                           ")
print("Grados Rankine: " +str(Ra))
print("                           ")
print("Grados Réaumur: " +str(Re))
print("                           ")
