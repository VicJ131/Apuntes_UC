'''
variable_numerica: int = 42
nombre: str = "Julián"

def direccion(calle: str, numero: int) -> str:
    return f'{calle.strip().title()} {numero}'
'''
'''
class Computador:
    def __init__(self) -> None:
        self.energia: int = 100

    def reducir_energia(self) -> None:
        self.energia -= 1

variable: Computador = Computador()
'''
#modulo typing
'''
from typing import Any

variable: Any = None
variable = 1
variable = 2.0
variable = "3"
'''
'''
from typing import Union
from typing import Callable

def dividir_numeros(numerador: Union[int, float], denominador: Union[int, float]) -> float:
    return numerador / denominador


funcion_dividir: Callable[[Union[int, float], Union[int, float]], float] = dividir_numeros
print(funcion_dividir(1.0, 2))
'''
'''
from typing import Optional


variable: Optional[int] = None
vaiable = 1
'''
# listas y collections
'''
from typing import List

lista: List[int] = [1, 2, 3, 4, 5, 6]
'''
# clases y autoreferencia
'''
from typing import Optional


class Persona:
    def __init__(self: Persona) -> None:
        self.bff: Optional[Persona] = None

    def asignar_bff(self: Persona, otro: Persona) -> None:
        self.bff = otro
'''
'''
from __future__ import annotations
from typing import Optional


class NuevaPersona:
    def __init__(self: NuevaPersona) -> None:
        self.bff: Optional[NuevaPersona] = None

    def asignar_bff(self: NuevaPersona, otro: NuevaPersona) -> None:
        self.bff = otro
'''
