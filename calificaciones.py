# Calificaciones

import math as m

def getGrades():
    print("====== Captura de calificaciones ======\n*** Ingrese 'q' para salir ***\n")
    grade = -1
    grades = []
    while (grade != 'q'):
        grade = input(f"Ingrese la calificacion {len(grades) + 1}: ")
        if (grade == 'q'):
            print(f"\nCapturando {len(grades)} calificaciones...\n")
            return grades
        else:
            try:
                grade = int(grade)
                if (grade < 0 or grade > 10):
                    print("\nIngrese una calificacion dentro del rango de 0 a 10...\n")
                else:
                    grades.append(grade)
            except:
                print("\nIngrese una calificacion valida...\n")

def getAverage(grades):
    return round(sum(grades) / len(grades), 1)

def gradesGtAvergae(grades, av):
    gradesGt = []
    for grade in grades:
        if (grade > av):
            gradesGt.append(grade)
    return gradesGt

def printResults(grades, av):
    gradesGtAv = gradesGtAvergae(grades, av)
    print(f"Tu promedio es de: {av:.1f}")
    print(f"Existen {len(gradesGtAv)} calificaciones mas altas que el promedio: {gradesGtAv}")


grades = getGrades()
av = getAverage(grades)

printResults(grades, av)

