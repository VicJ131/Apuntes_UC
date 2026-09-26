'''
import ejemplo

print(ejemplo.mi_variable)
ejemplo.saludar()

instancia = ejemplo.MiClase("42")
print(instancia.argumento)
'''


# importación con un alias
'''
import ejemplo as ej

print(ej.mi_variable)
print(ej.saludar)

ejemplo = "Otra variable"
print(ejemplo)
'''


# importación parcial
'''
from ejemplo import mi_variable, MiClase


print(mi_variable)
instancia = MiClase(23)
print(instancia.argumento)
'''


# importacion de archivo dentro de carpeta
'''
import carpeta_con_modulo.modulo

print(carpeta_con_modulo.modulo.variable)
'''
'''
import carpeta_con_modulo.modulo as modulo

print(modulo.variable)
'''
'''
from carpeta_con_modulo import modulo

print(modulo.variable)
'''
'''
from carpeta_con_modulo.modulo import variable

print(variable)
'''

# quedé en importación completa sin referencia al módulo XXX
