'''Escribe un programa que pida un nombre de usuario y una contraseña y si se ha 
introducido “pepe” y “passwd#” se indica “Has entrado al sistema”, sino se da un error.'''
print('Bienvenido al Sistema por motivo de seguridad ingrese su susuario y contraseña')
a=str(input('Usuario: '))
b=int(input('Contraseña: '))
if a=='pepe' and b==12345:
    print('Has entrado al sistema')
else:
    print('Error')

    