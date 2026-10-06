# Tuplas
'''
a = tuple()
b = (0, 1, 2)
c = (0, )
d = 0, 'uno'

print(type(a), a)
print(type(b), b, b[0], b[1])
print(type(c), c)
print(type(d), d, d[0], d[1])
'''
'''
a = ('Chile', 2, 4.15, 'Agosto')
a[2] = 'semestre'
'''
'''
tupla1 = (1, "b", 5, "j")
tupla2 = (1, "b", 5, "j")
tupla3 = (2, "b", 5, "j")

print(tupla1.__hash__())
print(tupla2.__hash__())
print(tupla3.__hash__())
'''
'''
lista1 = [1, "b", 5, "j"]

print(lista1.__hash__())
'''
'''
meses = (2023, "semestre", 2, ['Ago', 'Sep', 'Oct', 'Nov', 'Dic'])

meses[3][0] = 'Ene'
print(meses)
print(type(meses))
print(meses.__hash__())
'''
'''
meses = (2023, "semestre 2", 2, ('Ago', 'Sep', 'Oct', 'Nov', 'Dic'))
print(meses.__hash__())
'''
# Desempaquetamiento de elementos
'''
from typing import Tuple


def calcular_geometria(a: float, b: float) -> Tuple[float]:
    area = a * b
    perimetro = (2 * a) + (2 * b)
    punto_medio_a = a / 2
    punto_medio_b = b / 2

    return (area, perimetro, punto_medio_a, punto_medio_b)


data = calcular_geometria(20.0, 10.0)
print(f'1: {data}')
print(type(data))

p = data[1]
print(f'2: {p}')

a, p, mpa, mpb = data
print(f'3: {a}, {p}, {mpa}, {mpb}')

a, p, mpa, mpb = calcular_geometria(20.0, 10.0)
print(f'4: {a}, {p}, {mpa}, {mpb}')
'''
# Operador de desempaquetado
'''
from random import randint

relleno = [randint(0, 100) for _ in range(7, 15)]

datos_limitrofes = (
    'El verdadero tesoro',
    *relleno,
    'son los amigos que hicimos en el camino'
)

print('Tupla con informacion:', datos_limitrofes)

primer_elemento, *relleno, ultimo_elemento = datos_limitrofes

print('Relleno almacenado:', relleno)
print('Relleno desempaquetado:', *relleno)
print(f'Mensaje oculto: {primer_elemento} {ultimo_elemento}')
'''
'''
# Usando función de multiplicar para *
tupla_multiplicación = ('U', 'w'*5, 'U')
print(''.join(tupla_multiplicación))

# Usando para desempaquetar
tupla_desempaquetamiento = (1, *'2N3N4N5N6'.split('N'), 7)
print(tupla_desempaquetamiento)
'''

# Slicing de tuplas
'''
data = (400, 20, 1, 4, 10, 11, 12, 500)
print(f'data: {data}')

a = data[1:3]
print(f'1. data[1:3]: {a}')

a = data[3:]
print(f'2. data[3:]: {a}')

a = data[:5]
print(f'3. data[:5]: {a}')

a = data[2::2]
print(f'4. data[2::2]: {a}')

a = data[1:6:2]
print(f'5. data[1:6:2]: {a}')

a = data[::-1]
print(f'6. data[::-1]: {a}')
'''

# Named tuples
'''
from collections import namedtuple
from random import choices
from string import ascii_letters

ChileanRegister = namedtuple('ChileanRegister_type', ['RUT', 'name', 'age'])

MyRegister = namedtuple('MyRegister_type', 'unique_id, nickname, age')

c1 = ChileanRegister('13427974-5', 'Christian', 20)
c2 = MyRegister(''.join(choices(ascii_letters, k=9)), 'lucasvsj', 5)

print(f'{c1.name}:\t{c1.RUT}')
print(type(c1))
print(f'{c2.nickname}:\t{c2.unique_id}')
print(type(c2))
'''
