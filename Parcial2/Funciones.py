
def a_minuscula(caracter):
    cod = ord(caracter)
    if 65 <= cod <= 90:
        return chr(cod + 32)
    return caracter

def filtrar_por_busqueda(lista, texto):
    encontrados = []
    # Convertimos la búsqueda a minúscula una vez
    busqueda_lower = ""
    for c in texto:
        busqueda_lower += a_minuscula(c)
    
    for alumno in lista:
        # Procesamos nombre y apellido del alumno manualmente
        nombre_lower = ""
        for c in alumno['nombre']:
            nombre_lower += a_minuscula(c)
            
        # Lógica de búsqueda parcial (revisar si busqueda_lower esta dentro de nombre_lower)
        # Puedes usar el operador 'in' de Python que es básico
        if busqueda_lower in nombre_lower:
            encontrados.append(alumno)
    return encontrados

def burbujeo_ordenar(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if lista[j]['nota_promedio'] < lista[j + 1]['nota_promedio']:
                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = aux
    return lista


def borrar_alumno_por_legajo(lista, legajo_a_borrar):
    for i in range(len(lista)):
        if lista[i]['legajo'] == legajo_a_borrar:
            lista.pop(i)
            return True 
    return False