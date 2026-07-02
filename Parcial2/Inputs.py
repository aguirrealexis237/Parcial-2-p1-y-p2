import random

def es_letra_o_espacio(caracter):
    cod = ord(caracter)
    return (65 <= cod <= 90) or (97 <= cod <= 122) or cod == 32

def es_numero(texto):
    for car in texto:
        cod = ord(car)
        if not (cod >= 48 and cod <= 57):
            return False
    return len(texto) > 0

def validar_nombre_apellido(texto):
    if len(texto) < 3:
        return False
    for letra in texto:
        if not es_letra_o_espacio(letra):
            return False
    return True

def generar_legajo_unico(lista):
    while True:
        nuevo_legajo = random.randint(100000, 999999)
        repetido = False
        for alu in lista:
            if alu['legajo'] == nuevo_legajo:
                repetido = True
                break
        if not repetido:
            return nuevo_legajo