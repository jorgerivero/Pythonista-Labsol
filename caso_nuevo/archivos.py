#! /usr/bin/python3
# -*- coding: utf-8 -*-
""" Módulo que contiene la funcionalidad para despeglar a
    un alumno o todos los alumnos contenidos en el archivo
    {datos.ruta}/alumnos.txt
    
    Se importa el modulo caso_nuevo.datos
    
    Contiene tres funciones: """
import caso_nuevo.datos as datos

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

""" Abre el archivo de modo seguro para lectura, modo 'r'.
    Despliega uno a uno todos los alumnos contenidos
    en el archivo:  {datos.ruta}/alumnos.txt
   
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
def despliega_todos(ruta=datos.ruta):
    with open(ruta, 'r') as archivo:
        contador = 0
        for alumno in archivo:
            # evalua que sea un objeto valido
            alumno = eval(alumno)
            contador += 1
            print("\nAlumno: ", contador)
            despliega_uno(alumno)
        
""" Abre el archivo en modo seguro (with open) para escritura, modo 'a'.
    En caso de existir un archivo, este comienza a escribir al final de
    éste. Al final agrega un salto de linea"""
def agrega_uno(elemento, ruta=datos.ruta):
    with open(ruta, 'a') as archivo:
        # asegura que el elemento sea un objeto tipo cadena
        archivo.write(str(elemento) + '\n')