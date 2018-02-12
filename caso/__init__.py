#! /usr/bin/python3
# -*- coding: utf-8 -*-
""" Ejemplo de modulos en el curso de Python.

    Módulo que inicia el flujo de Sistema, el cual, importa al
    presente ámbito, la funcionalidad de altas, listado, además
    establece la  referencia  a los  datos  para  su  consulta,
    validación y almacenamiento posterior.
    
    El  metodo principal controla el flujo principal de nuestro
    Sistema. Mediante  un ciclo infinito, se solicita el número 
    de alumnos a procesar, el cual debe  ser un entero e indica
    el número de veces a ser invocado el modulo altas. En caso,
    de no ser un entero válido atrapamos el error y el  sistema
    seguira solicitando dicho número de alumnos a procesar.
    
    Los alumnos capturados con exito seran agregados a la lista
    en memoria y ubicada  en  "caso.datos.alumnos", lista  que,
    será desplegada al final de la captura."""

import caso.altas as altas
import caso.listado as listado
import caso.datos as datos

def principal():
    while True:
        try:
            alumnos = input("Número de alumnos:")
            alumnos = int(alumnos)
            print()
        except (ValueError) as error:
            print(error)
            continue
        else:
            break
    for contador in range(alumnos):
        print("\nAlumno nuevo", contador + 1)
        datos.alumnos.append(altas.alta())
    listado.despliega_todos()