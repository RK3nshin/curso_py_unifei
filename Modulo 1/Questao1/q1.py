
def ler_aquivo(nome):
    arquivo_notas = open(nome,"r")

    for nota in arquivo_notas:print(nota)
    arquivo_notas.close()

def add_arquivo(nome, linha):
    arquivo_notas = open(nome, "a")
    arquivo_notas.write(f"{linha}\n")
    arquivo_notas.close()

if __name__ == "__main__":
    
    print("Dados do arquivo de notas ")
    ler_aquivo("Questao1/notas.txt")
    print("Arquivo spos edição")
    add_arquivo("Questao1/notas.txt", "Maria: 10")
    ler_aquivo("Questao1/notas.txt")


