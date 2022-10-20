"""""
#Ejercicio 1
def saludarusuario(nombre:str):
    print("Hola", nombre)

saludarusuario(nombre = input("Dime el nombre del usuario:\n"))

#Ejercicio 2

def calcularrect (base:int, altura:int):
    print("El perímetro es", base*2+altura*2)
    print("El área es", base*altura)

calcularrect (2,4)

#Ejercicio 3
import math
def calculartri (cateto1=int, cateto2=int):
    print ("La hipotenusa es", math.sqrt(cateto1**2+cateto2**2))

calculartri (2,2)

#Ejercicio 4

def sumanums(num1=int, num2=int):
    print("La suma es", num1+num2)
    print("La resta es", num1-num2)
    print("La multiplicación es", num1*num2)
    print("La división es", num1/num2)

sumanums(2,2)

#Ejercicio 5

def calculargrados(grados=int):
    print("Son:", (grados-32)*(5/9), "grados Celsius")

calculargrados (60)
"""""
#Ejercicio 6
def medianumerica(num1=int, num2=int, num3=int):
    print("La media es", (num1+num2+num3/3))

medianumerica(num1 = int(input("Dime el número 1:\n")))
medianumerica(num2 = int(input("Dime el número 2:\n")))
medianumerica(num3 = int(input("Dime el número 3:\n")))


