'''Crea una aplicación que permita adivinar un número. 
En primer lugar la aplicación solicita un número entero por teclado. 
A continuación va pidiendo números y va respondiendo si 
el número a adivinar es mayor o menor que el introducido. 
El programa termina cuando se acierta el número.'''

a=int(input('Ingrese un número entero: '))
def adivi():
    b=int(input('Adivine el número: '))
    if b==a:
        print('Correcto')
    elif b>a:
        print('Prediccion incorrecta el número es mayor, vuelva a intentarlo ')
        return adivi()
    else:
        print('Prediccion incorrecta el número es menor, vuelva a intentarlo ')
        return adivi()
adivi()

    
        
    
    