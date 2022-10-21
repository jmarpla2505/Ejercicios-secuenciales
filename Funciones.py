"""""
#Ejercicio 1


def saludarusuario(nombre:str):
    print("Hola", nombre)

saludarusuario(nombre = input("Dime el nombre del usuario:\n"))

#Ejercicio 2

def calcularrectp (base:int, altura:int):
    perimetro = base*2+altura*2
    return perimetro

perimetro= calcularrectp (1,2)
print ("El perímetro es", perimetro)

def calcularrecta (base:int, altura:int):
    area= base*altura
    return area

area = calcularrecta (1,2)
print ("El área es", area )

def calcularareayper(base:int, altura:int):
     vDatos=[]
     area = calcularrecta(base,altura)
     perimetro=calcularrectp(base,altura)
     vDatos.append(area)
     vDatos.append(perimetro)
     return vDatos

base= int(input("Dime el valor de la base:"))
altura= int(input("Dime el valor de la altura:"))

vNum = calcularareayper(base,altura)
print("El área es", vNum[0])
print("El perímetro es", vNum[1])


#Ejercicio 3

import math
def calculartri (cateto1=int, cateto2=int):
    return math.sqrt(cateto1**2+cateto2**2)

hipotenusa = calculartri (1,2)
print("La hipotenusa es", hipotenusa)

#Ejercicio 4

def sumanums(num1=int, num2=int):
    return num1+num2
def restanums(num1=int, num2= int):
    return num1-num2
def multnums(num1=int, num2=int):
    return num1*num2
def divnums(num1= int, num2= int):
    return num1/num2

suma = sumanums (1,2)
print("La suma es", suma)
resta= restanums (1,2)
print("La resta es", resta)
multiplicacion = multnums (1,2)
print("La multiplicación es", multiplicacion)
division= divnums (1,2)
print("La división es", division)



#Ejercicio 5

def calculargrados(grados=int):
      return (grados-32)*(5/9)

grados= calculargrados (60)
print("Los grados son", grados)
"""""
#Ejercicio 6
def medianumerica(num1=int, num2=int, num3=int):
    media=(num1+num2+num3)/3
    return media

num1= int(input("Dime el valor del número 1:"))
num2= int(input("Dime el valor del número 2:"))
num3= int(input("Dime el valor del número 3:"))

media = medianumerica(num1,num2,num3)
print("La media es", media)




