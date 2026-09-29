# módulo os
import os

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

ruta = os.path.join("home", "pedro", "Libros", "python.pdf")
print(ruta)
