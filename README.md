### Argparse en Python

la libreria **argparse** es parte de la biblioteca estándar de Python y permite que su código acepte argumentos de línea de comando. Esto hace que su código sea fácil de configurar en tiempo de ejecución. Hay varias formas de hacer esto en Python, pero argparse es la más poderosa y requiere un código adicional mínimo. Este proyecto tiene varios ejemplos para su implementación.

El soporte del módulo **argparse** para las interfaces de líneas de comandos es construido alrededor de una instancia de argparse.ArgumentParser. Este es un contenedor para las especificaciones de los argumentos y tiene opciones que aplican el analizador como un todo:

	parser = argparse.ArgumentParser(
                    prog = 'ProgramName',
                    description = 'What the program does',
                    epilog = 'Text at the bottom of help')


El método **ArgumentParser.add_argument()** adjunta especificaciones de argumentos individuales al analizador. Soporta argumentos posicionales, opciones que aceptan valores, y banderas de activación y desactivación:

	parser.add_argument('filename')           # positional argument
	parser.add_argument('-c', '--count')      # option that takes a value
	parser.add_argument('-v', '--verbose', action='store_true')  # on/off flag

El método **ArgumentParser.parse_args()** corre el analizador y coloca los datos extraídos en un objeto **argparse.Namespace:**

	args = parser.parse_args()
	print(args.filename, args.count, args.verbose)

### Enlaces rápidos para **add_argument()**

| Nombre  | Descripción  | Valores |
| ------------ | ------------ | ------------ |
|  action |  Especifica como debe ser manejado un argumento | 'store', 'store_const', 'store_true', 'append', 'append_const', 'count', 'help', 'version'  |
| choices | Limita los valores a un conjunto específico de opciones  | ['foo', 'bar'], range(1, 10), o una instancia de Container |
| const  | Guarda un valor constante |   |
| default | Valor por defecto usado cuando un argumento no es proporcionado | Defaults to None |
| dest | Especifica el nombre del atributo usado en el espacio de nombres del resultado |  |
| help | Mensaje de ayuda para un argumento |   |
| metavar | Alterna la visualización del nombre para el argumento como es mostrado en la ayuda |   |
| nargs | Número de veces que puede ser usado un argumento | int, '?', '*', '+', o argparse.REMAINDER  |
|  required | Indica si un argumento es requerido u opciona |  True o False |
|  type |  Convierte automáticamente un argumento al tipo dado | int, float, argparse.FileType('w'), o una función invocable|


ArgumentParser.add_argument(name or flags...[, action][, nargs][, const][, default][, type][, choices][, required][, help][, metavar][, dest])

Define cómo se debe interpretar un determinado argumento de línea de comandos. Cada parámetro tiene su propia descripción más detallada a continuación, pero en resumen son:

- name or flags - Ya sea un nombre o una lista de cadena de caracteres de opción, e.g. foo o -f, --foo.
- action - El tipo básico de acción a tomar cuando este argumento se encuentra en la línea de comandos.
- nargs - El número de argumentos de la línea de comandos que deben ser consumidos.
- const - Un valor fijo requerido por algunas selecciones de action y nargs.
- default - El valor producido si el argumento está ausente en la línea de comando y si está ausente en el objeto de espacio de nombres.
- type - El tipo al que debe convertirse el argumento de la línea de comandos.
- choices - Un contenedor con los valores permitidos para el argumento.
- required - Si se puede omitir o no la opción de la línea de comandos (sólo opcionales).
- help - Una breve descripción de lo que hace el argumento.
- metavar - Un nombre para el argumento en los mensajes de uso.
- dest - El nombre del atributo que será añadido al objeto retornado por parse_args().

### Ejemplo

Archivo python
> argparse_example.py

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

Ejecutar en terminal: 

> python argparse_example.py -n Pablo -ln Perez -e 23

Salida: 

> Hola, Pablo Perez, Edad 23

Documentación : https://docs.python.org/es/3/library/argparse.html
