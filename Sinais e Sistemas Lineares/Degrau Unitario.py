import numpy as np               
import matplotlib.pyplot as plt   

# Cria um degrau como uma lambda function:
u = lambda t: 1*(t>=0)

# Determina os intervalos no tempo
t = np.arange(-5,10,0.01)

# Cria o grafico:
plt.plot(t, 2*u(t-1))
plt.grid()
plt.show()