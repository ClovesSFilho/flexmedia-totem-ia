import sqlite3
import pandas as pd

# conectar ao banco
conn = sqlite3.connect('data/interacoes.db')

# carregar dados da tabela
df = pd.read_sql_query("SELECT * FROM interacoes", conn)

conn.close()

print("\n==============================")
print("ANÁLISE DO TOTEM FLEXMEDIA")
print("==============================")

# total de interações
print("\nTotal de interações registradas:")
print(len(df))

# categorias mais usadas
print("\nCategorias mais escolhidas:")
print(df["categoria"].value_counts())

# taxa de aceitação
taxa_aceite = df["aceitou_recomendacao"].mean() * 100

print("\nTaxa de aceitação das recomendações:")
print(f"{taxa_aceite:.2f}%")