#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""Ejemplo de modulos en el curso de Python"""
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