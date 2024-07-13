import random
import csv
import math
from tabulate import tabulate

trabajadores = ["Juan Perez", "Maria Garcia", "Carlos Lopez", "Ana Martinez", "Pedro Rodriguez", 
                "Laura Hernandez", "Miguel Sanchez", "Isabel Gomez", "Francisco Diaz", "Elena Fernandez"]

sueldos = []

def asignar_sueldos():
    global sueldos
    sueldos = [random.randint(300000, 2500000) for _ in range(10)]
    print("Sueldos asignados aleatoriamente.")

def clasificar_sueldos():
    menores = [(trabajadores[i], sueldos[i]) for i in range(10) if sueldos[i] < 800000]
    mayores = [(trabajadores[i], sueldos[i]) for i in range(10) if sueldos[i] > 2000000]
    
    print("\nSueldos menores a $800.000")
    print("TOTAL:", len(menores))
    print(tabulate(menores, headers=["Nombre Empleado", "Sueldo"], tablefmt="pretty"))
    
    print("\nSueldos superiores a $2.000.000")
    print("TOTAL:", len(mayores))
    print(tabulate(mayores, headers=["Nombre Empleado", "Sueldo"], tablefmt="pretty"))
    
    print("\nTOTAL SUELDOS:", sum(sueldos))

def ver_estadisticas():
    max_sueldo = max(sueldos)
    min_sueldo = min(sueldos)
    promedio_sueldo = sum(sueldos) / len(sueldos)
    media_geometrica = math.exp(sum(math.log(s) for s in sueldos) / len(sueldos))
    
    print("\nEstadisticas:")
    print(f"Sueldo mas alto: ${max_sueldo}")
    print(f"Sueldo mas bajo: ${min_sueldo}")
    print(f"Promedio de sueldos: ${promedio_sueldo:.2f}")
    print(f"Media geometrica: ${media_geometrica:.2f}")

def reporte_sueldos():
    reporte = []
    for i in range(10):
        sueldo_base = sueldos[i]
        descuento_salud = sueldo_base * 0.07
        descuento_afp = sueldo_base * 0.12
        sueldo_liquido = sueldo_base - descuento_salud - descuento_afp
        
        reporte.append([
            trabajadores[i], 
            sueldo_base, 
            f"{descuento_salud:.1f}", 
            f"{descuento_afp:.1f}", 
            f"{sueldo_liquido:.1f}"
        ])

    print("\nReporte de sueldos:")
    print(tabulate(reporte, headers=["Nombre Empleado", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Liquido"], tablefmt="pretty"))

    with open('reporte_sueldos.csv', 'w', newline='') as csvfile:
        fieldnames = ["Nombre empleado", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Liquido"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for emp in reporte:
            writer.writerow({
                'Nombre empleado': emp[0], 
                'Sueldo Base': emp[1], 
                'Descuento Salud': emp[2], 
                'Descuento AFP': emp[3], 
                'Sueldo Liquido': emp[4]
            })
    
    print("Reporte de sueldos generado en 'reporte_sueldos.csv'.")

def salir_programa():
    print("\nFinalizando programa...")
    print("Este programa fue Desarrollado por: Antonella Cuvertino")
    print("contacto: An.cuvertino@duocuc.cl")
    print("RUT 21.988.926-7")

def menu():
    while True:
        print("\nMenu:")
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadisticas")
        print("4. Reporte de sueldos")
        print("5. Salir del programa")
        
        opcion = input("Seleccione una opcion: ")
        
        if opcion == '1':
            asignar_sueldos()
        elif opcion == '2':
            clasificar_sueldos()
        elif opcion == '3':
            ver_estadisticas()
        elif opcion == '4':
            reporte_sueldos()
        elif opcion == '5':
            salir_programa()
            break
        else:
            print("Opcion no valida. Intente nuevamente.")

menu()
