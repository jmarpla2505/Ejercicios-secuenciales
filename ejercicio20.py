#Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos)
#después de pedirnos cuantas monedas tenemos (de 2€, 1€, 50 céntimos, 20
#céntimos o 10 céntimos).



monedas2 = 0
monedas1 = 0
monedas50 = 0
monedas20 = 0
monedas10 = 0
cents = 0
centimoseuros = 0

monedas2 = int(input("Dime cúantas monedas tienes de 2 euros:\n"))
monedas1 = int(input("Dime cúantas monedas tienes de 1 euro:\n"))
monedas50 = int(input("Dime cúantas monedas tienes de 50 céntimos:\n"))
monedas20 = int(input("Dime cúantas monedas tienes de 20 céntimos:\n"))
monedas10 = int(input("Dime cúantas monedas tienes de 10 céntimos:\n"))
cents = monedas50*50+monedas20*20+monedas10*10
if cents>=100:
    centimoseuros=abs(100-cents)
    print("Tienes", int(monedas2*2+monedas1+centimoseuros/100), "euros y", monedas50*50+monedas20*20+monedas10*10-centimoseuros, "céntimos")
