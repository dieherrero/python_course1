# -*- coding: utf-8 -*-

'''
mostar contenido de un archivo
ejercutar en la terminal: python3 ses1.py prueba.txt
'''

import sys

if __name__ == "__main__":
	with open(sys.argv[1], 'r', encoding= 'utf8') as f:
	    for line in f:
	        print(line[:-1])
	        
