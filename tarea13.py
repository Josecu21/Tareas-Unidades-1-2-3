'''Pedir un número por teclado y mostrar la tabla de multiplicar'''

n = int(input('Ingrese un número entero: '))
for i in range(1,11):
    print(f'{i} x {n} = {i*n}')

   