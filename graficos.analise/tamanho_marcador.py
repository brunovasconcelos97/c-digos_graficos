#Você pode usar o argumento palavra-chave markersizeou 
#a versão mais curta mspara definir o tamanho dos marcadores:
#Defina o tamanho dos marcadores para 20:

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 10)
plt.show()
