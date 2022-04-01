'''Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde.

Por ejemplo: 1000 minutos son 16 horas y 40 minutos'''
print('ingrese los minutos')
contador=0
a=int(input())
h=int(a/60)
m=int(a%60)
print(h,'horas',m,'minutos')

