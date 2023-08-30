from fastapi import APIRouter
router = APIRouter()
# Criar os endpoints de produto: GET, POST, PUT, DELETE
@router.get("/produto/", tags=["Produto"])
def get_produto():
  return {"msg": "get todos executado"}, 200
@router.get("/produto/{id}", tags=["Produto"])
def get_produto(id: int):
  return {"msg": "get um executado"}, 200
@router.post("/produto/", tags=["Produto"])
def post_produto():
  return {"msg": "post executado"}, 200
@router.put("/produto/{id}", tags=["Produto"])
def put_produto(id: int):
  return {"msg": "put executado"}, 201
@router.delete("/produto/{id}", tags=["Produto"])
def delete_produto(id: int):
  return {"msg": "delete executado"}, 201