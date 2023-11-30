import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
Funcionários = ["Paula", "Bruno","Theo", "Maicon"]

plt.pie(y, labels = Funcionários)
plt.legend(title= "Four Fruits:")
plt.show() 
