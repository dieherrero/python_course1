#calculator and conditionals
import numpy as np

print'This program is a calculator, division second number between first. '
num1=float(input('number 1: '))
num2=float(input ('number 2: '))

#if/else:
if num2==0:
	print('Not possible to divide by 0.')
elif num1==0: 
	print 'The result is 0'
else:
	sol=num1/num2
	print 'resultado de la division:',sol



#for/while loop:

A = np.random.random(5) #Array de aleatorios

print 'Array A:'

for i in A:
	i=10.0*i
	print i  #se multiplican los aleatorios x10 y los imprime

#ahora vamos a hacer que solo multiplice  los 5 primeros elementos de un array aleatorio

B= np.random.random(15)

run= True
index = 1


print 'B:'

for j in B:
	while run:
		if index >= 5:
			run = False 
		else:
			j=100*j
			index += 1


	print j #error, multiplica muchas veces por 100 el primero y el resto no

















