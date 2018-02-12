#! /usr/bin/python3
# -*- coding: utf-8 -*-
""" Módulo que contiene 4 objetos en el ámbito global, la cual
    es muy útil para controlar el flujo, orden,  validacion  y
    almacenaje de los registros capturados unicamente en memoria.
    
    Los objetos representan dos tuplas, un dict y una lista
    correspondientes a carreras, orden, campos y alumnos."""

carreras = ("Sistemas", "Derecho", "Actuaría", "Arquitectura", "Administración")

orden = ("Nombre", "Primer Apellido", "Segundo Apellido", "Carrera", "Semestre",
         "Promedio", "Al Corriente")

campos = {"Nombre": str, "Primer Apellido": str, "Segundo Apellido": str,
         "Carrera": str, "Semestre": int, "Promedio": float,
         "Al Corriente": bool}

alumnos = [{"Nombre":"Eduardo", "Primer Apellido": "Sánchez",
          "Segundo Apellido": "Ramos", "Carrera": "Sistemas",
          "Semestre": 6, "Promedio": 7.5, "Al Corriente": True},
          {"Nombre": "Alberto", "Primer Apellido": "Durán",
          "Segundo Apellido": "Montellano", "Carrera": "Derecho",
          "Semestre": 2, "Promedio": 6.3, "Al Corriente": True},
          {"Nombre": "Joaquín", "Primer Apellido": "Ausencio",
          "Segundo Apellido": "Olvera", "Carrera": "Actuaría",
          "Semestre": 2, "Promedio": 5.2, "Al Corriente": False},
          {"Nombre": "Emiliano", "Primer Apellido": "Rentería",
          "Segundo Apellido": "", "Carrera": "Administración",
          "Semestre": 4, "Promedio": 8.7, "Al Corriente": True},
          {"Nombre": "Patricio", "Primer Apellido": "Ayala",
          "Segundo Apellido": "Arriaga", "Carrera": "Sistemas",
          "Semestre": 5, "Promedio": 8.0, "Al Corriente": True}]