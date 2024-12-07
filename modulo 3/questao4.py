import numpy as np
import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt

dados = np.random.dirichlet(1000)
arquivo = 'histograma_dados.png'

plt.figure(figsize=(8, 5))
plt.hist(dados, bins=30, color='purple')
plt.title('Distribuição de Dados - Histograma', fontsize=14)
plt.xlabel('Valores', fontsize=12)
plt.ylabel('Frequência', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.savefig(arquivo)
plt.show()




