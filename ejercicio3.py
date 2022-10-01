#Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
import math
cateto1 = 0
cateto2 = 0
cateto1 = (int)(input("Dime un cateto del triángulo:\n "))
cateto2 = (int)(input("Dime otro cateto del triángulo:\n  "))
hipotenusa = math.sqrt(cateto1*cateto1+cateto2*cateto2)
print("La hipotenusa es:", hipotenusa)
