#Pide al usuario dos pares de números x1,y2 y x2,y2, que representen dos puntos
#en el plano. Calcula y muestra la distancia entre ellos.
import math
x1 = 0
y1 = 0
y2 = 0
x2 = 0
x1 = int(input("Dime x1:\n"))
x2 = int(input("Dime x2:\n"))
y1 = int(input("Dime y1:\n"))
y2 = int(input("Dime y2:\n"))
print("La distancia entre los puntos es", math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1)))