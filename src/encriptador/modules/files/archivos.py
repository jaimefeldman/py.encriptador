# -*- coding: utf-8 -*-
"""
    modulos.archivos
    ~~~~~~~~~~~~~~~~

    Manejador de archivos.

    :copyright: (c) 2023 By Jaime Feldman.
    :license: MIT, see LICENSE for more details.
"""

import pkg_resources
from termcolor import colored, cprint

def read_file(path):
    try:
        print(f"- intentando abrir:{path}")
        #with pkg_resources.resource_stream('saludador', 'resources/'+file) as fstream:
        contenido = pkg_resources.resource_string('saludador', path).decode("utf-8")
        print("[", colored("Leiendo archivo", "magenta"), "]")
        print(contenido)
            
    except FileNotFoundError: 
            print("Archivo no encontrado..")
    except Exception as e:
       print("Error al abrir el archivo:", e)
