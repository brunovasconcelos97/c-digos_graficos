import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

plt.scatter(x, y)
plt.show()

#A observação no exemplo acima é o resultado da passagem de 13 carros.
#O eixo X mostra a idade do carro.
#O eixo Y mostra a velocidade do carro quando ele passa.
#Existe alguma relação entre as observações?
#Parece que quanto mais novo o carro, mais rápido ele anda, mas isso pode ser coincidência, afinal registramos apenas 13 carros.