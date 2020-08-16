import numpy as np
testing = open ("gw1L1.txt","r")
length1 = len(testing.read()) #len da la longitud del archivo, no funciona con el archivo, da el numero de bytes
print(length1) #check
mat = np.array(np.random.rand(1,5)) #matriz aleatoria
matord = np.sort(mat) #ordena la matriz
print('M= ', mat)
print(matord)

