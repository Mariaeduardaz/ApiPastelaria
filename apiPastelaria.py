from fastapi import FastAPI
from settings import HOST, PORT, RELOAD
# import das classes com as rotas/endpoints
from mod_funcionario import FuncionarioDAO
from mod_cliente import ClienteDAO
from mod_produto import ProdutoDAO

app = FastAPI()

# mapeamento das rotas/endpoints
app.include_router(FuncionarioDAO.router)
app.include_router(ClienteDAO.router)
app.include_router(ProdutoDAO.router)

import db
db.criaTabelas()

# rota padrão
@app.get("/")
def root():
  return {"detail":"API Pastelaria", "Swagger UI": "http://127.0.0.1:8000/docs", "ReDoc": "http://127.0.0.1:8000/redoc" }

if __name__ == "__main__":
  import uvicorn
  uvicorn.run('apiPastelaria:app', host=HOST, port=int(PORT), reload=RELOAD)    

    