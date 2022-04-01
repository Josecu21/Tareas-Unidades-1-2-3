'''Escribir un programa que lea un año indicar si es bisiesto. 
Nota: un año es bisiesto si es un número divisible por 4, pero no si es divisible por 100, 
excepto que también sea divisible por 400.'''

def bisiesto(n):
    if n & 400 ==0:
        return True
    elif n % 100 ==0:
        return False
    elif n % 4 ==0:
        return True
    else:
        return False
n = int(input('Ingrese año: '))
print('El año %i es bisiesto ?: %s' % (n,bisiesto(n)))