#project: CALCULATOR
import numpy as np
import re

print ("Type 'quit' to exit \n")

run = True
previous = 0

def performMath():
	global run
	global previous
	equation = ""
	if previous == 0:
	    equation = input('Enter equation quit: ')
	else:
	    equation = input(str(previous))

	if equation == 'quit':
	    print ('Bye')
	    run = False
	else:
	    equation = re.sub('[a-zA-Z,.:()" "]', '', equation) #quitamos texto
	    if previous == 0:
	        previous = eval(equation) #eval() realiza la operacion
#	    print 'You typed ', previous
	    else:
	      	previous = eval(str(previous) + equation) #operaciones encadenadas

while run:
	performMath()








