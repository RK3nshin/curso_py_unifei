import matplotlib.pyplot as plt

def graficoBarras(categorias,valores):
    plt.figure(figsize=(8, 5))
    plt.bar(categorias, valores, color='skyblue', edgecolor='black')
    plt.title('Comparação de Categorias', fontsize=14)
    plt.xlabel('Categorias', fontsize=12)
    plt.ylabel('Valores', fontsize=12)
    plt.grid()
    plt.show()

if __name__ == "__main__":
   categorias = ['A', 'B', 'C', 'D']
   valores = [10, 25, 5, 15]
   graficoBarras(categorias,valores)

#


