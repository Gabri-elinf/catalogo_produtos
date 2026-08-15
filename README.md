# catalogo_produtos
Catálogo de Produtos com Histórico de Preços
API desenvolvida em Python com FastAPI para cadastro de produtos, categorias e registro manual de preços. O projeto foi pensado como uma base simples para estudo de backend, documentação de API e evolução futura para um sistema de monitoramento de preços mais completo.
Objetivo
O objetivo deste projeto é praticar conceitos de desenvolvimento backend com Python, incluindo criação de rotas, organização inicial de API, uso de ambiente virtual, documentação automática e execução local com servidor ASGI. O FastAPI gera documentação interativa automaticamente em `/docs` e uma alternativa em `/redoc`, o que facilita o teste das rotas durante o desenvolvimento.

Funcionalidades planejadas
Cadastro de produtos.
Cadastro de categorias.
Registro manual de preços.
Consulta do preço atual.
Histórico de preços por produto.
Filtro por período.
Cálculo de variação de preço.
Exportação de dados para CSV.
Tecnologias utilizadas
Tecnologia	Finalidade
Python	Linguagem principal do projeto
FastAPI	Criação da API e documentação automática
Uvicorn	Servidor ASGI para rodar a aplicação localmente
SQLite	Banco de dados inicial para simplificar a configuração local
SQLAlchemy	Camada de modelagem e acesso ao banco
Pydantic	Validação de dados de entrada e saída

Estrutura inicial do projeto
```text
catalogo-de-produtos/
├── .venv/
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```
O ambiente virtual com `venv` isola as dependências do projeto para evitar conflitos com outras instalações Python no sistema.[cite:184]
Como executar o projeto
1. Criar e ativar o ambiente virtual
No Windows PowerShell:
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```
O módulo `venv` cria um ambiente virtual leve com conjunto independente de pacotes para o projeto.[cite:126]
2. Instalar as dependências
```powershell
pip install fastapi uvicorn
```
Para salvar as dependências atuais do projeto:
```powershell
pip freeze > requirements.txt
```
3. Executar a aplicação
```powershell
uvicorn main:app --reload
```
O Uvicorn é o servidor responsável por rodar a aplicação FastAPI localmente, e a opção `--reload` reinicia automaticamente o servidor quando o código é alterado durante o desenvolvimento.
Exemplo de `main.py`
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def inicio():
    return {"mensagem": "API funcionando"}
```
Esse exemplo mínimo já é suficiente para expor uma rota inicial e gerar a documentação automática da API.
Como testar no navegador
Com o servidor em execução, os principais endereços locais são:
API raiz: `http://127.0.0.1:8000/`
Swagger UI: `http://127.0.0.1:8000/docs`
ReDoc: `http://127.0.0.1:8000/redoc`
O FastAPI disponibiliza Swagger UI em `/docs` e ReDoc em `/redoc` por padrão, sem configuração extra necessária.

Próximos passos
As próximas etapas previstas para o projeto são:
Criar o CRUD de produtos.
Criar o CRUD de categorias.
Implementar o registro de preços.
Criar consultas de histórico.
Adicionar filtros e cálculos de variação.
Organizar a aplicação em módulos.
Criar testes básicos.
Publicar o projeto no GitHub.
Status do projeto
Projeto em fase inicial de estruturação, com ambiente virtual, instalação do FastAPI e preparação da primeira rota da API.
