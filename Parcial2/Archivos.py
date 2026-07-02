
import json

def cargar_archivo(nombre_archivo):
    # Uso de json permitido por ser estándar de Python
    with open(nombre_archivo, 'r') as f:
        return json.load(f)

def guardar_archivo(nombre_archivo, lista):
    with open(nombre_archivo, 'w') as f:
        json.dump(lista, f, indent=4)