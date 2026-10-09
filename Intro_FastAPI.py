from fastapi import FastAPI
from pydantic import BaseModel
import json from pathlib import Path

app = FastAPI()

class Novavenda(BaseModel):
    item: str
    preco: float

vendas = {
    1: {"item": "lata de refrigerante", "preco": 5.00},
    2: {"item": "lata de cerveja", "preco": 3.50},
    3: {"item": "sanduíche", "preco": 10.00},
    4: {"item": "batata frita", "preco": 7.00}
}

@app.get("/")
def home():
    return {"vendas": len(vendas)}

@app.get("/vendas/{id_venda}")
def pegar_venda(id_venda:int):
    return vendas[id_venda]

@app.post("/vendas/")
def cadastrar_venda(nova_venda: Novavenda):
    id_venda = len(vendas) + 1
    vendas[id_venda] = {"item": nova_venda.item, "preco": nova_venda.preco}
    return vendas[id_venda]
  