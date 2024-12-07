import csv

def ler_e_print_csv(arquivo):
    with open(arquivo, mode='r') as file:
        reader = csv.reader(file)
        for linha in reader:
            print(", ".join(linha))

def aplicar_desconto(arquivo_origem, arquivo_destino):
    with open(arquivo_origem, mode='r') as file:
        reader = csv.reader(file)
        linhas = list(reader)  

    with open(arquivo_destino, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        for linha in linhas:
            if linha[0] == "ID":  
                writer.writerow(linha)
            else:
                id_produto, produto, preco = linha
                preco_com_desconto = float(preco) * 0.9
                writer.writerow([id_produto, produto, f"{preco_com_desconto:.2f}"])


arquivo_original = "Questao2/produtos.csv"
arquivo_com_desconto = "Questao2/produtos_desconto.csv"

print("Dados originais:")
ler_e_print_csv(arquivo_original)

aplicar_desconto(arquivo_original, arquivo_com_desconto)

print("\nDados com desconto:")
ler_e_print_csv(arquivo_com_desconto)
