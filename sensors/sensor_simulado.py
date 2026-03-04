import sqlite3
import random
from datetime import datetime

categorias = ["comer", "comprar", "descansar"]
preferencias = ["doce", "salgado", "presente", "para mim"]
recomendacoes = ["Starbucks", "McDonalds", "Renner", "Nike", "Livraria"]

conn = sqlite3.connect('data/interacoes.db')
cursor = conn.cursor()

categoria = random.choice(categorias)
preferencia = random.choice(preferencias)
tempo_interacao = random.randint(3, 20)
recomendacao = random.choice(recomendacoes)
aceitou = random.choice([0,1])

cursor.execute("""
INSERT INTO interacoes 
(timestamp, categoria, preferencia, tempo_interacao, recomendacao, aceitou_recomendacao)
VALUES (?, ?, ?, ?, ?, ?)
""", (
    datetime.now(),
    categoria,
    preferencia,
    tempo_interacao,
    recomendacao,
    aceitou
))

conn.commit()
conn.close()

print("Interação registrada no sistema.")