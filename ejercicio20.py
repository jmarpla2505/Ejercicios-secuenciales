#Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos)
#después de pedirnos cuantas monedas tenemos (de 2€, 1€, 50 céntimos, 20
#céntimos o 10 céntimos).



monedas2 = 0
monedas1 = 0
monedas50 = 0
monedas20 = 0
monedas10 = 0
centimos = 0
euros = 0

monedas2 = int(input("Dime cúantas monedas tienes de 2 euros:\n"))
monedas1 = int(input("Dime cúantas monedas tienes de 1 euro:\n"))
monedas50 = int(input("Dime cúantas monedas tienes de 50 céntimos:\n"))
monedas20 = int(input("Dime cúantas monedas tienes de 20 céntimos:\n"))
monedas10 = int(input("Dime cúantas monedas tienes de 10 céntimos:\n"))
euros = monedas2+monedas1
centimos = monedas50*0.5+monedas20*0.2+monedas10*0.10
dinerototal = euros+centimos
print("En total, tienes:", dinerototal, "euros")