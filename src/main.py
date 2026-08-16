# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def inicio():
#     return {"mensagem": "API funcionando"}


import sqlite3
from fastapi import FastAPI
from pydantic import BaseModel
from src.db import get_connection


app = FastAPI()

@app.get("/")
def home():
    return {"mensagem": "API de catálogo de produtos"}

@app.get("/produtos")
def listar_produtos():
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            p.id_produto,
            p.nome,
            p.descricao,
            p.ativo,
            p.data_criacao
        FROM produtos p
        ORDER BY p.nome
    """)

    produtos = []
    for row in cursor.fetchall():
        item = dict(row)
        item["ativo"] = bool(item["ativo"])
        produtos.append(item)

    conn.close()
    return {"produtos": produtos}


@app.get("/categorias")
def listar_categorias():
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            c.id_categoria,
            c.nome,
            c.data_criacao
        FROM categorias c
        ORDER BY c.id_categoria
    """)

    categorias = []
    for row in cursor.fetchall():
        item = dict(row)
        categorias.append(item)

    conn.close()
    return {"categorias": categorias}

class ProdutoCreate(BaseModel):
    id_produto: int
    nome: str
    descricao: str | None = None
    id_categoria: int
    ativo: bool = True

@app.post("/produtos")
def criar_produto(produto: ProdutoCreate):
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO produtos (id_produto, nome, descricao, id_categoria, ativo)
            VALUES (?, ?, ?, ?, ?)
        """, (
            produto.id_produto,
            produto.nome,
            produto.descricao,
            produto.id_categoria,
            int(produto.ativo)
        ))

        conn.commit()

        cursor.execute("""
            SELECT
                p.id_produto,
                p.nome,
                p.descricao,
                c.nome AS categoria,
                p.ativo,
                p.data_criacao
            FROM produtos p
            JOIN categorias c ON c.id_categoria = p.id_categoria
            WHERE p.id_produto = ?
        """, (produto.id_produto,))

        novo_produto = dict(cursor.fetchone())
        novo_produto["ativo"] = bool(novo_produto["ativo"])

        return {
            "mensagem": "Produto criado com sucesso",
            "produto": novo_produto
        }

    except sqlite3.IntegrityError as e:
        raise HTTPException(status_code=400, detail=f"Erro de integridade: {str(e)}")

    finally:
        conn.close()