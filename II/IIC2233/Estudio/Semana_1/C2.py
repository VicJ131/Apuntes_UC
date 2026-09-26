#Context manager
'''
with open("IO_archivo_ejemplo_3", "r") as file:
    contenido = file.read()
'''
#Es equivalente a:
'''
file = open("IO_archivo_ejemplo_3", "r")
try:
    contenido = file.read()
finally:
    file.close()
'''

#ejecución de dir en objeto tipo archivo
'''
file = open("IO_archivo_ejemplo_3", "w")
print(dir(file))
file.close()
'''

#uso de método with en clase propia
'''
import string
import random
from types import TracebackType
from typing import List, Optional, Type


class StringUpper:

    def __init__(self) -> None:
        print("1. Inicializando context manager")
        self.data = []

    def __enter__(self) -> List[str]:
        print("2. Abriendo context manager y definiendo qué elemento será el 'as XXXX'")
        return self.data

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
          print("5. Cerrando context manager")
          i = 0
          for char in self.data:
              self.data[i] = char.upper()
              i+= 1



with StringUpper() as s_upper:
    print("3. Primera línea dentro del context manager")

    for i in range(20):
        #aleatorio un ascii en minúscula
        #y se agrega a lista
        s_upper.append(random.choice(string.ascii_lowercase))

    print("\t" + str(s_upper))
    print("4. Última línea del context manager")

print("\t" + str(s_upper))
'''

#módulos para emular el tener un archivo

from io import StringIO, BytesIO


file_in = StringIO("información como texto y más")

file_out = BytesIO()

char = file_in.read(1)
while char:
    file_out.write(char.encode("ascii", "ignore"))
    char = file_in.read(1)

buffer_ = file_out.getvalue()
print(buffer_)
