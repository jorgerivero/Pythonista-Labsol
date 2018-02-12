#! /usr/bin/python3
# -*- coding: utf-8 -*-
""" Módulo de busquedas
    
    Regresa una tupla con los registros encontrados apertir
    de una cadena de caracteres"""
import caso.datos as datos
def buscar(cadena):
    lista = []
    def encontrar(cadena, alumno):    
        for campo in datos.campos_busqueda:
            if str(cadena).lower() in str(alumno[campo]).lower():
                lista.append(alumno)
                continue
    for alumno in datos.alumnos:
        encontrar(cadena, alumno)
    return tuple(lista)