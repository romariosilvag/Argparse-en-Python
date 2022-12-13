import argparse

def imprimir_argumentos(nombre,apellido,edad):
    """
    Imprimir argumentos

    Args:
        nombre (str): nombre de la persona
        apellido (str): apellido de la persona
        edad (int): edad de la persona
    """
    # Imprimimos el argumento de línea de comandos
    print(f'Hola, {nombre} {apellido}, Tu edad es {edad}')


def argparse_configuracion():
    """
    Configuracion de argumentos

    Returns:
        <class 'argparse.Namespace: retorna objeto con los argumentos
    """
    # Descripcion de argumentos
    parser = argparse.ArgumentParser(description='Imprimir Nombre, Apellido y Edad con Argumentos', epilog="Aqui se puede mostrar informacion adicional de los argumentos. \n https://docs.python.org/3/library/argparse. \n")

    # Agregamos argumentos de línea de comandos
    parser.add_argument('-n', '--name', type=str, default="Sin Dato", help='nombre de la persona', required=True)
    parser.add_argument('-ln', '--lan', type=str, default="Sin Dato", help='apellido de la persona')
    parser.add_argument('-e', '--edad', type=int, default=0, help='edad de la persona')

    # Parseamos los argumentos
    args = parser.parse_args()

    return args

def main():
    
    # llamar funcion de configuracion de argumentos
    args = argparse_configuracion()

    # llamar funcion para imprimir mensaje
    imprimir_argumentos(args.name,args.lan,args.edad)

if __name__ == '__main__':

    main()


"""
usage: argparse_example_two.py [-h] -n NAME [-ln LAN] [-e EDAD]

Imprimir Nombre, Apellido y Edad con Argumentos

optional arguments:
  -h, --help            show this help message and exit        
  -n NAME, --name NAME  nombre de la persona
  -ln LAN, --lan LAN    apellido de la persona
  -e EDAD, --edad EDAD  edad de la persona

Aqui se puede mostrar informacion adicional de los argumentos. 
https://docs.python.org/3/library/argparse.
"""