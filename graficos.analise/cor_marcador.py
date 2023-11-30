#Você pode usar o argumento palavra-chave markeredgecolorou o mais curto 
# mec para definir a cor da borda dos marcadores:

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r')
plt.show()

#azul com borda vermelha
#plt.plot(ypoints, marker = 'o', ms = 20, mfc = 'r')

#vermelho com borda vermelha
#plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r', mfc = 'r')

#verde 
#plt.plot(ypoints, marker = 'o', ms = 20, mec = '#4CAF50', mfc = '#4CAF50')

#rosa
#plt.plot(ypoints, marker = 'o', ms = 20, mec = 'hotpink', mfc = 'hotpink')