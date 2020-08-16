# -*- coding: utf-8 -*-

'''
busqueda url
ejercutar en la terminal: python3 ses4.py UTC url busqueda.txt
en busqueda se guarda
'''

import sys
import os
import requests

if __name__ == "__main__":
	r = requests.get(sys.argv[2]) # abrir url
	with open(sys.argv[3], 'w+', encoding='utf8') as f:
		for line in r.text.split('\n'):
			if sys.argv[1] in line:
				f.write(''.join([line.strip(), '\n']))
	
	
