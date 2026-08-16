#Conexão com o banco de dados
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "data" / "catalogo_produtos.db"

SQL_DIR = BASE_DIR / "sql"
SCHEMA_PATH = SQL_DIR / "schema.sql"
INSERT_PATH = SQL_DIR / "insert_produtos.sql"

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def execute_sql_file(file_path):
    conn = get_connection()
    cursor = conn.cursor()

    with open(file_path, "r", encoding="utf-8") as file:
        cursor.executescript(file.read())

    conn.commit()
    conn.close()

def init_db():
    execute_sql_file(SCHEMA_PATH)
    print("Banco e tabelas criados com sucesso!")

def insert_test_data():
    execute_sql_file(INSERT_PATH)
    print("Dados de teste inseridos com sucesso!")
    
if __name__ == "__main__":
    init_db()
    insert_test_data()