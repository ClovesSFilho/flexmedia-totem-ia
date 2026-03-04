import sqlite3
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# conectar ao banco
conn = sqlite3.connect('data/interacoes.db')

df = pd.read_sql_query("SELECT * FROM interacoes", conn)

conn.close()

# transformar variáveis categóricas em numéricas
df = pd.get_dummies(df, columns=["categoria", "preferencia", "recomendacao"])

# definir X e y
X = df.drop(["id", "timestamp", "aceitou_recomendacao"], axis=1)
y = df["aceitou_recomendacao"]

# dividir treino e teste
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# criar modelo
modelo = RandomForestClassifier()

# treinar modelo
modelo.fit(X_train, y_train)

# prever resultados
predicoes = modelo.predict(X_test)

# calcular acurácia
acuracia = accuracy_score(y_test, predicoes)

print("\n==============================")
print("MODELO DE MACHINE LEARNING")
print("==============================")

print(f"\nAcurácia do modelo: {acuracia:.2f}")