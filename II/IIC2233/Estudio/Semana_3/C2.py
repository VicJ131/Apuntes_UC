# Stacks
'''
stack = []

stack.append(1)
stack.append(2)
stack.append(3)

print(stack)

elemento = stack.pop()
print(f'Hicimos pop de {elemento}')
print(f'El stack quedó: {stack}')

tope_stack = stack[-1]
print(f'Tope del stack: {tope_stack}')
print(f'Stack: {stack}')

print(f'El stack tiene {len(stack)} elementos.')


def is_empty(s):
    return len(s) == 0


print(f"¿El stack está vacío? {is_empty(stack)}")
'''

# Ejemplos reales de uso


class Navegador:

    def __init__(self, current_url='https://www.google.com'):
        self.__urls_stack = []
        self.__current_url = current_url

    def __cargar_url(self, url):
        self.__current_url = url
        print(f'Cargando URL: {url}')

    def ir(self, url):
        self.__urls_stack.append(self.__current_url)
        print('Ir ->', end=' ')
        self.__cargar_url(url)

    def volver(self):
        last_url = self.__urls_stack.pop()
        print('Back->', end=' ')
        self.__cargar_url(last_url)

    def mostrar_pagina_actual(self):
        print(f'Página actual: ')

# CONTINUAR EJEMPLOOO
