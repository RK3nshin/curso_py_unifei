import pandas as pd

dados = {
    "Aluno": ["João", "Maria", "José", "Ana"],
    "Nota 1": [7.5, 8.2, 6.9, 9.1],
    "Nota 2": [8.0, 7.5, 6.5, 9.5]
}

df = pd.DataFrame(dados)

print("Coluna Aluno:")
print(df["Aluno"])

print("\nPrimeira linha do DataFrame:")
print(df.iloc[0])

media_jose = df.query('Aluno == "José"')[["Nota 1", "Nota 2"]].mean(axis=1).iloc[0]

print(f"\nMédia das notas do aluno José: {media_jose:.2f}")
