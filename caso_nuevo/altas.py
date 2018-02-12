#! /usr/bin/python3
# -*-coding: utf-8 -*-
import caso_nuevo.datos as datos
import caso_nuevo.valida as valida

""" Módulo que contiene la funcion de altas.

    La función alta devuelve un objeto tipo dict y la única instruc-
    cion que invoca es un return, aqui se crea un objeto  tipo  dict
    apartir de una tupla iterable del objeto ""datos.orden"", apartir
    de su iteración se obtiene el nombre de cada uno de los campos --
    entonces se invoca la function ingresa(nombre_del_campo).
    
    La función ingresa, mantiene un loop infinito con la finalidad de
    verificar el tipo de valor sea correcto, como  se  definió  en el
    objeto tipo dict datos.campos y se evalua mediante  una expesión.
    
    Si se ingresa un valor y cuyo tipo de dato es distinto  de 'str' se
    intenta evaluar que los tipos de datos conincidan, entonces se crea
    su wrapper correspondiente en Python, en caso contrario se  procede
    a cachar la excepción, cualquiera que esta sea, se continua a soli-
    citar al usuario el valor de nueva cuenta. 
    
    En caso de ser el tipo de dato un 'str' o no se generó algun error
    o no tiró alguna excepción se procede a validar las reglas del tipo
    de dato como se indica en el modulo caso.valida
    
    Entonces, se regresará el valor tipeado en python al for inicial.
    
    El final, se crea el objeto tipo dict ...
    alumno_dict {campo: valor, campo2: valor2, .....}
    
    El objeto tipo dict será al macenado en el archivo {ruta}alumnos.txt,
    mediante el módulo:
    
     caso_nuevo.archivos.agrega_uno( alumno_dict )"""

def alta():
    """Realiza las altas."""
    
    
    def ingresa(campo):
        while True:
            mensaje = "Ingrese " + campo.lower() + ": " 
            dato = input(mensaje)
            if datos.campos[campo] != str:
                try:
                    if eval(dato) == datos.campos[campo](dato):
                        dato = datos.campos[campo](dato)
                    else:
                        continue
                except:
                    continue
            if valida.reglas(dato, campo):
                return dato
                  
    return {campo: ingresa(campo) for campo in datos.orden}
