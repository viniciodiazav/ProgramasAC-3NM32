# Califiaciones Ordenadas

import os
from QuickSort import quickSort

def getGrades():
    grades = []
    grade = -1
    i = 1
  #  os.system("clear")
    print("====== Captura de calificaciones ======\nINGRESE \"q\" PARA SALIR\n")
    while (grade != 'q' or (grade < 0 and grade > 10)):
        grade = input(f"calificacion [{i}]: ")
        if (grade.lower() == 'q'):
            print(f"\nCapturando {i} calificaciones...\n") 
            return grades
        else:
            try:
                grade = int(grade)
                if (grade < 0):
                    print("\n*** Ingrese una calificacion mayor o igual a 0 ***\n")
                elif (grade > 10):
                    print("\n*** Ingrese una calificacion mayor o igual a 10 ***\n")
                else:
                    grades.append(grade)
                    i += 1
            except:
                print("\n*** Ingrese una calificacion valida ***\n")


def printSortGrades(grades):
    print("Calificaiones ordenadas:")
    quickSort(grades, 0, len(grades) - 1)
    print(grades)
    print(f"Promedio: {(sum(grades) / len(grades)):.2f}")

grades = getGrades()
printSortGrades(grades)
