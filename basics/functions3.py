import numpy as np

#infinite arguments function
def print_people(*people): #people ~ array
	for person in people:
	   print 'This person is', person


print_people('Diego', 'JC', 'Lucia')


