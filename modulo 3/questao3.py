import matplotlib.pyplot as plt

def graficoDispensao(x,y):
    plt.figure(figsize=(8, 5))
    plt.scatter(x, y, color='red', edgecolor='black', s=100, label='Pontos (x, y)')
    plt.title('Relação entre Variáveis X e Y', fontsize=14)
    plt.xlabel('Eixo X', fontsize=12)
    plt.ylabel('Eixo Y', fontsize=12)
    plt.grid(True, linestyle='--')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    x = [1, 2, 3, 4, 5, 6, 7]
    y = [2, 3, 5, 6, 7, 8, 10]
    graficoDispensao(x,y)