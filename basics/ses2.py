# -*- coding: utf-8 -*-

'''
copiar archivos
ejercutar en la terminal: python3 ses2.py origen.txt destino.txt
'''

import sys

if __name__ == "__main__":
    f,g = open(sys.argv[1], 'r'), open(sys.argv[2], 'w+')
    for line in f:
	    g.write(line)
    
    g.close()
    

