#! /usr/bin/python3
# -*- coding: utf-8 -*-
""" Módulo que contiene las reglas de validación para los datos
    a capturar. Las reglas ciertamente son condiciones que deben
    cumplir los valores a capturados.
    
    Las reglas son:
    1. El valor del campo Carrera debe ser una carrera valida acorde
       a datos.carreras.
    2. El valor del campo Semetre debe ser un entero mayor a 0
    3. El valor del campo Promedio debe ser cualquier valor contenido
       entre 0 y 10, puede ser un entero o un floato un True
    4. El valor del campo Nombre y Primer Apellido son  obligatorios,
       no pueden ser vacios.
    5. El valor del campo Segundo Apellido  en  caso  de  ser  vacio
       mostrará  una pregunta al usuario si es correcto   que    sea
       vacio S/N:, la validación se forza a mayusculas S o N. Además
       si es N se vuelverá a pedir el apellido
       
    Si las reglas definidas para los  datos  y  campos  se  cumplen,
    la función reglas devolverá un True, en caso contrario regresará
    False"""

import caso.datos as datos

def reglas(dato, campo):
    if campo == "Carrera" and dato not in datos.carreras:
        return False
    elif campo == "Semestre" and dato < 1:
        return False
    elif campo == "Promedio" and (dato < 0 or dato > 10):
        return False
    elif (campo in ("Nombre", "Primer Apellido") and (dato == "")):
        return False
    elif campo == "Segundo Apellido" and dato == "":
        while True:
            mensaje = "No ha ingresado el segundo apellido. ¿Es correcto? S/N: "
            confirma = input(mensaje)
            if confirma.upper() in ("S", "N"):
                respuesta = True
                if confirma.upper() == "N":
                    respuesta = False
                return respuesta
    else:
        return True