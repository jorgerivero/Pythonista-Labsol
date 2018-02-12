#! /usr/bin/python3
# -*- coding: utf-8 -*-
""" Módulo que contiene la funcionalidad para despeglar a
    un alumno o todos los alumnos contenidos.
    
    Se importa el modulo caso.datos
    
    Contiene dos funciones: """
import caso.datos as datos

""" Despliega un alumno de acuerdo al datos.orden

    Ejemplo:
    
    Ingrese nombre: Jorge
    Ingrese primer apellido: Rivero
    Ingrese segundo apellido: R
    Ingrese carrera: Sistemas
    Ingrese semestre: 1
    Ingrese promedio: 1
    Ingrese al corriente: 1
    {'Al Corriente': True,
     'Carrera': 'Sistemas',
     'Nombre': 'Jorge',
     'Primer Apellido': 'Rivero',
     'Promedio': 1.0,
     'Segundo Apellido': 'Ronquillo',
     'Semestre': 1}"""
def despliega_uno(elemento):
    for campo in datos.orden:
        print(campo + ": " + str(elemento[campo]))

"""Despliega todos los alumnos contenidos en la lista
   datos.alumnos
   
   Ejemplo:
   
    Alumno:  1
    Nombre: Eduardo
    Primer Apellido: Sánchez
    Segundo Apellido: Ramos
    Carrera: Sistemas
    Semestre: 6
    Promedio: 7.5
    Al Corriente: True
   ..."""
def despliega_todos():
    contador = 0
    for alumno in datos.alumnos:
        contador += 1
        print("\nAlumno: ", contador)
        despliega_uno(alumno)