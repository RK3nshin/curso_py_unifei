import streamlit as st
import pandas as pd
import kagglehub
import matplotlib.pyplot as plt

# Carregar base de dados
@st.cache_data
def carregar_dados():
    # Baixar a base de dados "Student Information Dataset" do Kaggle
    dataset_path = "zeeshier/student-information-dataset"
    download_path = kagglehub.dataset_download(dataset_path)

    # Caminho do arquivo CSV
    caminho_csv = f"{download_path}/students.csv"
    return pd.read_csv(caminho_csv)
    
def extrairIformacao(df_dados_alunos):
  
    df_dados_alunos["GraduationYear"] = df_dados_alunos["GraduationYear"].astype(str)

    # Extrair informações
    gpa_por_ano = df_dados_alunos.groupby("GraduationYear")["GPA"].median()
    estudades_por_depatamento = df_dados_alunos['Department'].value_counts()
    
    # Gerar informações para o gráfico de dispersão (Idade vs GPA)
    idade_gpa = media_gpa_por_idade = df_dados_alunos.groupby("Age")["GPA"].mean()
     
    # Filtrar alunos aprovados (GPA > 2.5) e reprovados (GPA <= 2.5)
    df_dados_alunos['Status'] = df_dados_alunos['GPA'].apply(lambda x: 'Aprovado' if x > 3.0 else 'Reprovado')
    status_por_departamento = df_dados_alunos.groupby('Department')['Status'].value_counts().unstack().fillna(0)

    
    return gpa_por_ano, estudades_por_depatamento, idade_gpa,status_por_departamento,df_dados_alunos

# Visualização
def main():
    info = extrairIformacao(carregar_dados())

    # Título principal do dashboard
    st.write("""
                # Dashboard - Análise de Dados dos Estudantes
                Uma análise detalhada sobre o desempenho acadêmico, idade e distribuição dos alunos.
                """)

    # Gráfico de Linha - Mediana das Notas (GPA) dos Alunos por Ano
    st.write("### Mediana das Notas (GPA) dos Alunos por Ano")
    st.line_chart(info[0])

    # Gráfico de Barras - Quantidade de Alunos por Departamento
    st.write("### Quantidade de Alunos por Departamento")
    st.bar_chart(info[1])

    # Gráfico de Dispersão - Idade vs GPA dos Alunos
    st.write("### Gráfico de Dispersão: Idade vs GPA dos Alunos")
    st.scatter_chart(info[2])

    # Gráficos de Pizza - Distribuição de Aprovados e Reprovados por Departamento
    for departamento in info[3].index:
        st.write(f"### {departamento}")
        
        dados_departamento = info[3].loc[departamento]
        fig_pizza, ax_pizza = plt.subplots(figsize=(6, 6))

        ax_pizza.pie(dados_departamento, 
                     labels=dados_departamento.index, 
                     autopct='%1.1f%%', 
                     startangle=90, 
                     colors=['#4CAF50', '#F44336'], 
                     wedgeprops={'edgecolor': 'black'})
        
        ax_pizza.set_title(f"Distribuição de Aprovados e Reprovados no Departamento de {departamento}", fontsize=14, fontweight='bold')
        
        st.pyplot(fig_pizza)
    
    #Exibir tabela de dados
    st.dataframe(info[4])



main()
