# Ejemplo snake case y camel case
'''
class PerroAmigable:
    def __init__(self, nombre: str, edad: int) -> None:
        self.nombre = nombre
        self.edad = edad

    def saludar_amigo(self, amigo: "PerroAmigable") -> None:
        # se pone entre comillas porque aún no está definido
        print("¡Woof!")
        print("¡Hola " + amigo.nombre + "!")


def saludo_mutuo(perro_1: PerroAmigable, perro_2: PerroAmigable) -> None:
    perro_1.saludar_amigo(perro_2)
    perro_2.saludar_amigo(perro_1)
    print()


perro_juan = PerroAmigable("Juan", 21)
perro_pedro = PerroAmigable("Pedro", 20)
perro_jose = PerroAmigable("Jose", 22)

saludo_mutuo(perro_juan, perro_pedro)
saludo_mutuo(perro_jose, perro_pedro)
saludo_mutuo(perro_juan, perro_jose)
'''


# Mal ejemplo de nombres de variables
'''
def funcion(l: list) -> int:
    i = 0
    a = l[0]
    for j in range(1, len(l)):
        var = l[j]
        if var > a:
            i = j
            a = var
    return i
'''


# Buen ejemplo
'''
def indice_de_maximo(lista: list) -> int:
    indice_actual = 0
    maximo_actual = lista[0]
    for indice in range(1, len(lista)):
        elemento = lista[indice]
        if elemento > maximo_actual:
            indice_actual = indice
            maximo_actual = elemento
    return indice_actual
'''

# imports siempre al comienzo del archivo
# espacios luego de comas y alrededor de operadores matemáticos
# no pasarse de las 79 lineas, seguir el pep8
