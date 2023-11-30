import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o')
plt.show()

#Você pode usar o argumento palavra-chave marker
# para enfatizar cada ponto com um marcador especificado:

#Marque cada ponto com uma estrela:
#plt.plot(ypoints, marker = '*')

