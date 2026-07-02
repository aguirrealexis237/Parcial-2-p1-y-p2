import Inputs
import Funciones
import Archivos

def ejecutar():
    lista_alumnos = []
    datos_cargados = False
    
    while True:
        print("\n--- MENÚ UTN FRA ---")
        print("1. Cargar alumnos (Archivo/Manual)")
        print("2. Mostrar egresados por plan")
        print("3. Mostrar egresados anteriores al 2000")
        print("4. Buscar alumno")
        print("5. Salón de la fama")
        print("6. Salir"

       )

        opcion = input("Seleccione: ")
        
        # Validar acceso previo a cargar datos
        if not datos_cargados and opcion in ["2", "3", "4", "5"]:
            print("Error: Debe cargar los alumnos (Opción 1) primero.")
            input("Presione Enter...")
            continue

        elif opcion == "1":
            print("\nTipo de carga:")
            print("a. Archivo (alumnos.json)")
            print("b. Manual")
            tipo = input("Seleccione (a/b): ")
            
            if tipo == "a":
                lista_alumnos = Archivos.cargar_archivo("alumnos.json")
                datos_cargados = True
                print("Datos cargados correctamente.")
                
            elif tipo == "b":
                # Pedimos datos con validaciones simples
                nombre = input("Nombre: ")
                apellido = input("Apellido: ")
                egreso = int(input("Año egreso (1991-2026): "))
                plan = int(input("Plan (1991, 2003, 2024): "))
                promedio = float(input("Nota promedio (6-10): "))
                
                # Generamos el legajo único (función que ya tienes en Inputs)
                legajo = Inputs.generar_legajo_unico(lista_alumnos)
                
                nuevo_alumno = {
                    "legajo": legajo,
                    "nombre": nombre,
                    "apellido": apellido,
                    "egreso": egreso,
                    "plan": plan,
                    "nota_promedio": promedio
                }
                
                confirmar = input(f"¿Desea agregar a {nombre} {apellido} con legajo {legajo}? (s/n): ")
                if confirmar.lower() == 's':
                    lista_alumnos.append(nuevo_alumno)
                    datos_cargados = True
                    print("Alumno agregado con éxito.")
            else:
                print("Opción no válida.")

        elif opcion == "2":
            plan_b = input("Ingrese plan (1991, 2003, 2024): ")
            encontro = False
            for alu in lista_alumnos:
                # Comparamos como string para evitar errores si el JSON tiene números
                if str(alu['plan']) == plan_b:
                    print(f"{alu['nombre']} {alu['apellido']} - Promedio: {alu['nota_promedio']}")
                    encontro = True
            if not encontro:
                print("No hay alumnos de ese plan.")
            input("Presione Enter...")

        elif opcion == "3":
            encontro = False
            acumulador = 0
            contador = 0
            for alu in lista_alumnos:
                if alu['egreso'] < 2000:
                    print(f"{alu['nombre']} {alu['apellido']} ({alu['egreso']})")
                    acumulador += alu['nota_promedio']
                    contador += 1
                    encontro = True
            if encontro:
                print(f"Promedio general: {acumulador / contador:.2f}")
            else:
                print("No hay egresados anteriores al 2000.")
            input("Presione Enter...")

        elif opcion == "4":
            texto = input("Ingrese nombre o apellido (mínimo 3 letras): ")
            if Inputs.validar_nombre_apellido(texto):
                resultados = Funciones.filtrar_por_busqueda(lista_alumnos, texto)
                print(f"Se encontraron {len(resultados)} alumnos.")
                for r in resultados:
                    print(f"- {r['nombre']} {r['apellido']}")
            else:
                print("Error: Ingrese solo letras (mínimo 3).")
            input("Presione Enter...")

        elif opcion == "5":
            ordenados = Funciones.burbujeo_ordenar(lista_alumnos.copy())
            encontro = False
            for alu in ordenados:
                if alu['nota_promedio'] >= 9:
                    print(f"{alu['nombre']} {alu['apellido']} - Nota: {alu['nota_promedio']}")
                    encontro = True
            if not encontro:
                print("No hay alumnos con promedio >= 9.")
            input("Presione Enter...")

        elif opcion == "6":
            Archivos.guardar_archivo("alumnos.json", lista_alumnos)
            break

    