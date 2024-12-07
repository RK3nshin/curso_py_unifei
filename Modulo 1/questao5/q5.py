import pandas as pd

dados = {
    "Nome": ["João", "Maria", "José"],
    "Idade": [28, 34, 29],
    "Cidade": ["São Paulo", "Rio de Janeiro", "Curitiba"]
}

df = pd.DataFrame(dados)
df.to_csv("dados.csv", index=False)  
print("Arquivo 'dados.csv' salvo com sucesso.")

novo_df = pd.read_csv("dados.csv")
print("\nDados lidos do arquivo 'dados.csv':")
print(novo_df)