import datetime

# VARIABLES GLOBALES 
matriz_notas = []
datos_cargados = False
carga_manual = False

def leer_csv():
    global matriz_notas, datos_cargados
    with open("notas.csv", "r") as archivo:
        next(archivo)  # Salta cabecera
        matriz_notas = []
        for linea in archivo:
            fila = [int(n) for n in linea.strip().split(',')]
            matriz_notas.append(fila)
    datos_cargados = True
    print("Datos cargados correctamente.")

def guardar_csv():
    fecha = datetime.date.today().strftime("%d-%m-%Y")
    with open(f"{fecha}.csv", "w") as archivo:
        archivo.write("trimestre1,trimestre2,trimestre3\n")
        for fila in matriz_notas:
            archivo.write(f"{fila[0]},{fila[1]},{fila[2]}\n")
    print(f"Archivo guardado: {fecha}.csv")

def cargar_manualmente():
    global matriz_notas, datos_cargados, carga_manual
    matriz_notas = []
    print("Ingrese notas (1-10) para 7 alumnos:")
    for i in range(7):
        fila = []
        for j in range(3):
            while True:
                try:
                    n = int(input(f"Alumno {i+1} Trimestre {j+1}: "))
                    if 1 <= n <= 10:
                        fila.append(n)
                        break
                    print("La nota debe ser 1-10.")
                except ValueError: print("Ingrese un número válido.")
        matriz_notas.append(fila)
    datos_cargados = True
    carga_manual = True

def mostrar_desaprobados():
    encontrado = False
    for i, fila in enumerate(matriz_notas):
        if any(n < 7 for n in fila):
            print(f"Alumno {i+1} está desaprobado.")
            encontrado = True
    if not encontrado: print("No hay desaprobados.")

def mostrar_aplazos():
    encontrado = False
    for i, fila in enumerate(matriz_notas):
        if any(n < 4 for n in fila):
            print(f"Alumno {i+1} tiene aplazos.")
            encontrado = True
    if not encontrado: print("No hay aplazos.")

def calcular_porcentajes():
    total = len(matriz_notas)
    desaprobados = sum(1 for fila in matriz_notas if any(n < 7 for n in fila))
    print(f"Aprobados: {((total-desaprobados)/total)*100:.1f}%")
    print(f"Desaprobados: {(desaprobados/total)*100:.1f}%")

def mejor_trimestre():
    sumas = [sum(fila[i] for fila in matriz_notas) for i in range(3)]
    mejor = max(sumas)
    for i, s in enumerate(sumas):
        if s == mejor: print(f"Trimestre {i+1} es el mejor con promedio {s/len(matriz_notas):.2f}")

def mostrar_menu():
    global datos_cargados
    while True:
        print("\n--- MENÚ ---")
        print("1. Cargar notas\n2. Mostrar desaprobados\n3. Mostrar aplazos\n4. % Aprobados/Desaprobados\n5. Mejor trimestre\n6. Salir")
        opcion = input("Seleccione: ")
        if opcion == "1":
            tipo = input("m - Manual, a - Archivo: ").lower()
            if tipo == "m": cargar_manualmente()
            elif tipo == "a": leer_csv()
        elif not datos_cargados: print("Error: Cargue datos primero.")
        elif opcion == "2": mostrar_desaprobados()
        elif opcion == "3": mostrar_aplazos()
        elif opcion == "4": calcular_porcentajes()
        elif opcion == "5": mejor_trimestre()
        elif opcion == "6":
            if carga_manual: guardar_csv()
            break
        else: print("Opción no válida.")

if __name__ == "__main__":
    mostrar_menu()