from fastapi import APIRouter
from mod_produto.Produto import Produto
router = APIRouter()
# Criar as rotas/endpoints: GET, POST, PUT, DELETE

@router.get("/produto/", tags=["Produtos"])
def get_produto():
    return {"msg": "get todos executado"}, 200

@router.get("/produto/{id}", tags=["Produtos"])
def get_produto(id: int, p: Produto):
    return {"msg": "get um executado", "id": id, "nome": p.nome, "descrição": p.descricao, "valor unitario": p.valor_unitario}, 200

@router.post("/produto/", tags=["Produtos"])
def post_produto():
    return {"msg": "post executado"}, 200

@router.put("/produto/{id}", tags=["Produtos"])
def put_produto(id: int):
    return {"msg": "put executado"}, 201

@router.delete("/produto/{id}", tags=["Produtos"])
def delete_produto(id: int):
    return {"msg": "delete executado"}, 201