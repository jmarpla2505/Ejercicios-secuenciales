#Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde. Por ejemplo: 1000 minutos son 16 horas y 40 minutos.

Minutos = 0
Minutos = (int)(input("Dime una cantidad de minutos:\n "))
print(Minutos, "minutos son", int(Minutos/60), "horas y", Minutos%60, "minutos")
