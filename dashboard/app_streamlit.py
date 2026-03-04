import sqlite3
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# conectar ao banco
conn = sqlite3.connect('data/interacoes.db')

df = pd.read_sql_query("SELECT * FROM interacoes", conn)

conn.close()

st.title("Totem Inteligente - Dashboard de Interações")

# métricas
total = len(df)
taxa_aceite = df["aceitou_recomendacao"].mean() * 100

st.metric("Total de interações", total)
st.metric("Taxa de aceitação", f"{taxa_aceite:.2f}%")

# categorias mais escolhidas
st.subheader("Categorias mais escolhidas")

categorias = df["categoria"].value_counts()

fig, ax = plt.subplots()
categorias.plot(kind="bar", ax=ax)

st.pyplot(fig)

# aceitação das recomendações
st.subheader("Aceitação das recomendações")

aceite = df["aceitou_recomendacao"].value_counts()

fig2, ax2 = plt.subplots()
aceite.plot(kind="bar", ax=ax2)

st.pyplot(fig2)