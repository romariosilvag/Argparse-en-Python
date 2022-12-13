import argparse

# Creamos un objeto parser
parser = argparse.ArgumentParser()

# Descripcion de argumentos
parser = argparse.ArgumentParser(description='Imprimir Nombre, Apellido y Edad con Argumentos')

# Agregamos argumentos de línea de comandos
parser.add_argument('-n', '--name', type=str, default="Sin Dato", help='nombre de la persona')
parser.add_argument('-ln', '--lan', type=str, default="Sin Dato", help='apellido de la persona')
parser.add_argument('-e', '--edad', type=int, default=0, help='edad de la persona')

# Parseamos los argumentos
args = parser.parse_args()

# Imprimimos el argumento de línea de comandos
print(f'Hola, {args.name} {args.lan}, Edad {args.edad}')


"""
usage: argparse_example.py [-h] [-n NAME] [-ln LAN] [-e EDAD]

Imprimir Nombre, Apellido y Edad con Argumentos

optional arguments:
  -h, --help            show this help message and exit      
  -n NAME, --name NAME  nombre de la persona
  -ln LAN, --lan LAN    apellido de la persona
  -e EDAD, --edad EDAD  edad de la persona
"""