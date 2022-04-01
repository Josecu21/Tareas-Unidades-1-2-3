'''Programa que lea un carácter por teclado y compruebe si es una letra mayúscula.'''
print('Comprobador')
n = str(input('Ingrese texto: '))
def Verificador(cad):
    cont = 0
    for i in cad:
        if i ==i.upper():
            cont += 1
            if i ==' ':
                cont -= 1
    print('El numero de mayusculas es',cont)
Verificador(n)
 
 