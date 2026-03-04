import sqlite3

conn = sqlite3.connect('data/interacoes.db')

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS interacoes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    categoria TEXT,
    preferencia TEXT,
    tempo_interacao INTEGER,
    recomendacao TEXT,
    aceitou_recomendacao INTEGER
)
""")

conn.commit()
conn.close()

print("Banco de dados criado com sucesso.")