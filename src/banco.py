import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS pessoas (
                    id INTEGER PRIMARY KEY,
                    nome TEXT,
                    localidade TEXT,
                    data TEXT,
                    profissao TEXT
                )''')


def inserir_pessoa(id, nome, localidade, data, profissao):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO pessoas (id, nome, localidade, data, profissao) VALUES (?, ?, ?, ?, ?)", (id, nome, localidade, data, profissao))
    conn.commit()
    conn.close()

def listar_pessoas():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pessoas")
    rows = cursor.fetchall()
    for row in rows:
        print(f"ID: {row[0]}, Nome: {row[1]}, Localidade: {row[2]}, Data: {row[3]}, Profissão: {row[4]}")
    conn.close()

def pesquisa_id(id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pessoas WHERE id=?", (id,))
    row = cursor.fetchone()
    #if row is not None:
    #    print(f"ID: {row[0]}, Nome: {row[1]}, Localidade: {row[2]}, Data: {row[3]}, Profissão: {row[4]}")
    #else:
    #    print("erro")
    conn.close()
    return row


def deleta_id(id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM pessoas WHERE id=?", (id,))
    conn.commit()
    conn.close()

#inserir_pessoa(1,"joão","sampa","sabado domingo","medico")
dado=pesquisa_id(1)
print(dado)
deleta_id(1)
conn.close()
