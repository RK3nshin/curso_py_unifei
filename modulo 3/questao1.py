import matplotlib.pyplot as plt


def graficoLinha(x,y):
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, marker='o', linestyle='-', color='blue', label='y = 2x')

    plt.title('Gráfico de linha', fontsize=14)
    plt.xlabel('Eixo X', fontsize=12)
    plt.ylabel('Eixo Y', fontsize=12)

    plt.grid(True, linestyle='--')
    plt.legend()

    plt.show()

if __name__ == "__main__":
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]
    graficoLinha(x,y)
