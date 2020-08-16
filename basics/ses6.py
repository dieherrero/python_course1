# -*- coding: utf-8 -*-

'''
busqueda y acceso a url con pdf y descargarlo
ejercutar en la terminal: python3 ses6.py url busqueda.pdf
en busqueda se guarda
'''

import sys
from os import popen
import requests

if __name__ == "__main__":
	link = sys.argv[1]
	try:
		name_file = sys.argv[1]
	except:
		f = popen('date + %d-%m-%Y').read()
		name_file = ''.join(['bop_', f[:-1], '.pdf'])
		
	r = requests.get(link) # abrir url
	myfile = open(name_file, 'wb')
	myfile.write(r.content)

