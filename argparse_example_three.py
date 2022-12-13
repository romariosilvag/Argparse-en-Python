# size.py

import argparse

"""
Especificar una lista de valores de entrada permitidos

Otra posibilidad interesante en las CLI de argparse es que puede crear un dominio de valores permitidos para un argumento u opción específica. 
Puede hacer esto proporcionando una lista de valores aceptados utilizando el argumento de opciones de .add_argument().

Aquí hay un ejemplo de una aplicación pequeña con una opción de tamaño que solo acepta algunos valores de entrada predefinidos:
"""

parser = argparse.ArgumentParser()

parser.add_argument("--size", choices=["S", "M", "L", "XL"], default="M")

args = parser.parse_args()

print(f"size : {args.size}")


