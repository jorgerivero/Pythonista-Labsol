#! /usr/bin/python3
# -*- coding: utf-8 -*-

#El valor de ruta es la ruta donde se encuentra el archivo datos.txt
#Ejemplo en Windows: "C:\Users\Josech\Documentos\Python\datos.txt"

""" Módulo que contiene 4 objetos en el ámbito global, la cual
    es muy útil para controlar el flujo, orden,  validacion  y
    almacenaje de los registros capturados en un archivo.
    
    Donde:
    
    ruta, contiene la ubicación del archivo que  contiene  los
          registros almacenados, ejemplo: caso_nuevo/alumnos.txt
    
    orden, contiene una tupla con los nombres de los atributos
          del alumno
        
    campos, contiene un objeto tipo dict {llave: valor, ...} en
          el cual, la llave es el nombre del campo y el valor es
          tipo de valor que corresponde a cada campo, ejemplo:
          
          "Nombre": str
          "Primer Apellido": str 
          "Segundo Apellido": str
          "Carrera": str 
          "Semestre": int
          "Promedio": float
          "Al Corriente": bool
          
     carreras, contiene una tupla, con los nombres de las carreras
          validas a capturar"""

ruta = "caso_nuevo/alumnos.txt"

orden = ("Nombre", "Primer Apellido", "Segundo Apellido", "Carrera",
"Semestre", "Promedio", "Al Corriente")

campos = {"Nombre": str, "Primer Apellido": str, "Segundo Apellido": str,
         "Carrera": str, "Semestre": int, "Promedio": float,
         "Al Corriente": bool}

carreras = ("Sistemas", "Derecho", "Actuaría", "Arquitectura",
    "Administración")

campos_busqueda = ("Nombre", "Primer Apellido", "Segundo Apellido")