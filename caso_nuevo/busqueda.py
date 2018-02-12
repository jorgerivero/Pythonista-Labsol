#! /usr/bin/python3
# -*- coding: utf-8 -*-
""" Módulo de busquedas
    
    Regresa una tupla con los registros encontrados apertir
    de una cadena de caracteres"""
import caso_nuevo.datos as datos
def buscar(cadena, ruta=datos.ruta):
    lista = []
    def encontrar(cadena, alumno):    
        for campo in datos.campos_busqueda:
            if str(cadena).lower() in str(alumno[campo]).lower():
                lista.append(alumno)
                continue   
    with open(ruta, 'r') as archivo:
        for alumno in archivo:
            # evalua que sea un objeto valido
            alumno = eval(alumno)
            encontrar(cadena, alumno)
    return tuple(lista)