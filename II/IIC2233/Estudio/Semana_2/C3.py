# módulo os
import os
from pathlib import Path

# path absoluto
'''
path_absoluto = '/home/archivo.txt'

with open(path_absoluto, 'rt') as archivo:
    lineas = archivo.readlines()

lineas
'''

# path relativo
'''
path_relativo = 'data/archivo.txt'

with open(path_relativo, 'rt') as archivo:
    contenido = archivo.read()

print(contenido)
'''
'''
path1 = '/carpeta1/carpeta2/imagen.jpg'

dirname1 = os.path.dirname(path1)
basename1 = os.path.basename(path1)

print(f'path: {path1}')
print(f'dirname: {dirname1}')
print(f'basename: {basename1}')


# Extensiones de archivo

nombre_sin_extension, extension = os.path.splitext(basename1)
print(nombre_sin_extension)
print(extension)
'''
'''
path = 'data/archivo_de_texto.jpg'

with open(path, 'w') as f:
    f.writelines(['linea1\n', 'linea2\n', 'linea3\n'])
'''


# portabilidad de paths
'''
ruta = os.path.join("home", "pedro", "Libros", "python.pdf")
print(ruta)
'''


# Navegación entre directorios
'''
lista_de_contenidos = os.listdir(os.path.join("data", "gato"))
print(lista_de_contenidos)
'''

'''
for raiz, directorios, archivos in os.walk("data", topdown=True):
    print("Raíz:", raiz)
    print()
    print("Archivos:")
    for archivo in archivos:
        print(os.path.join(raiz, archivo))
    print()
    print("Directorios:")
    for directorio in directorios:
        print(os.path.join(raiz, directorio))
    print("-" * 30)
'''

# Ejemplo de lectura y escritura básico
'''
ruta_juego_1 = os.path.join("data", "gato", "juego_1.txt")
archivo = open(ruta_juego_1, "rt")
print(archivo.readlines())
archivo.close()
'''

'''
ruta_juego_1 = os.path.join("data", "gato", "juego_1.txt")
with open(ruta_juego_1, "rt") as archivo:
    lineas = archivo.readlines()

tablero = []
for linea in lineas:
    fila = linea.strip().split(',')
    print(fila)
    tablero.append(fila)

tablero[2][2] = 'O'
for fila in tablero:
    print(fila)

ruta_juego_2 = os.path.join("data", "gato", "juego_2.txt")

with open(ruta_juego_2, "wt") as archivo:
    for fila in tablero:
        fila_en_texto = ",".join(fila) + "\n"
        print(fila_en_texto, end='')
        archivo.write(fila_en_texto)
'''


# Pathlib

# from pathlib import Path
'''
path = Path("data/archivo.txt")

print("Nombre del archivo:", path.name)
print("Extensión del archivo:", path.suffix)
print("Es un directorio:", path.is_dir())
print("Es un archivo:", path.is_file())

path_absoluto = path.absolute()
print("Ruta absoluta:", path_absoluto)

if path.exists():
    print("El archivo existe en la ruta indicada")

print("\nLeer el contenido de un archivo de texto:")
contenido = path.read_text()
print(contenido)

print("\nRecorriendo el directorio de la carpeta data:")
directorio = Path("./data/")
for archivo in directorio.iterdir():
    print(archivo)
'''

'''
with path.open(mode='r') as archivo:
    contenido = archivo.read()
    print(contenido)
'''

path1 = Path("./data/nuevo_archivo.txt")
with path1.open(mode='w') as archivo:
    archivo.write("¿Podría funcionar mejor?\n")
    archivo.write("¡Recordar que el modo 'w' sobrescribe lo existente!")

with path1.open(mode='r') as archivo:
    contenido = archivo.read()
    print(contenido)
