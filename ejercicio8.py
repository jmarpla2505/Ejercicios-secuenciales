#Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus
#ventas, el vendedor desea saber cuanto dinero obtendrá por concepto de
#comisiones por las tres ventas que realiza en el mes y el total que recibirá en el
#mes tomando en cuenta su sueldo base y comisiones.

venta1 = 0
venta2 = 0
venta3 = 0
comisiones = 0
sueldobase = 0
sueldototal = 0

venta1 = int(input("Dinero generado con la primera venta:\n "))
venta2 = int(input("Dinero generado con la segunda venta:\n "))
venta3 = int(input("Dinero generado con la tercera venta:\n "))
sueldobase= venta1+venta2+venta3
print("El sueldo base es ", sueldobase)
comisiones = sueldobase*0.1
print("La comisión es de", comisiones)
sueldototal= sueldobase+comisiones
print("El sueldo total es", sueldototal )
