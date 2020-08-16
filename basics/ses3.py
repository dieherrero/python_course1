# -*- coding: utf-8 -*-

'''
contar palabras
ejercutar en la terminal: python3 ses3.py origen.txt 
'''

import sys

if __name__ == "__main__":
	with open(sys.argv[1], 'r') as f:
		w = 0
		for line in f:
			words = line.split()
			w += len(words)
		
	print(w)
