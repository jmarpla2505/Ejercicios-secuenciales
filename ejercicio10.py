#Un alumno desea saber cual será su calificación final en la materia de
#Algoritmos. Dicha calificación se compone de los siguientes porcentajes:
# 55% del promedio de sus tres calificaciones parciales.
# 30% de la calificación del examen final.
# 15% de la calificación de un trabajo final.

parcial1 = 0
parcial2 = 0
parcial3 = 0 
examenfinal = 0
trabajofinal = 0

parcial1 = int(input("Nota del primer parcial:\n "))
parcial2 = int(input("Nota del segundo parcial:\n "))
parcial3 = int(input("Nota del tercer parcial:\n "))
examenfinal = int(input("Nota del examen final:\n "))
trabajofinal = int(input("Nota del trabajo final:\n "))
print("La calificación en la materia de algoritmos es", ((parcial1+parcial2+parcial3)/3)*0.55+examenfinal*0.3+trabajofinal*0.15)