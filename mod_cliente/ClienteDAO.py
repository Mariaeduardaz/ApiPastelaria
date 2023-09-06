from fastapi import APIRouter
from mod_cliente.Cliente import Cliente
import db
from mod_cliente.ClienteModel import ClienteDB

router = APIRouter()
# Criar as rotas/endpoints: GET, POST, PUT, DELETE

@router.get("/cliente/", tags=["Cliente"])
def get_cliente():
    return {"msg": "get todos executado"}, 200

@router.get("/cliente/{id}", tags=["Cliente"])
def get_cliente(id: int):
    try:
        session = db.Session()
        dados = session.query(ClienteDB).filter(ClienteDB.id_clinete == id).all()
        return dados, 200
    except Exception as e: 
        return {"erro": str(e)}, 400
    finally:
        session.close()

@router.post("/cliente/", tags=["Cliente"])
def post_cliente(corpo: Cliente):
    try:
        session = db.Session()
        dados = ClienteDB(None, corpo.nome, corpo.cpf, corpo.telefone, corpo.comprar_fiado, corpo.dia_fiado, corpo.senha)
        session.add(dados)
        session.commit()
        return {"id": dados.id_clinete}, 200
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()
    

@router.put("/cliente/{id}", tags=["Cliente"])
def put_cliente(id: int, corpo: Cliente):
    try:
        session = db.Session()
        dados = session.query(ClienteDB).filter(ClienteDB.id_clinete == id).one()
        dados.nome = corpo.nome
        dados.cpf = corpo.cpf
        dados.telefone  =corpo.telefone
        dados.compra_fiado = corpo.comprar_fiado
        dados.dia_fiado = corpo.dia_fiado
        dados.senha = corpo.senha
        session.add(dados)
        session.commit()
        return {"id": dados.id_clinete}, 200
    except Exception as e:
        session.rollback()
        return{"erro": str(e)}, 400
    finally:
        session.close()

@router.delete("/cliente/{id}", tags=["Cliente"])
def delete_cliente(id: int):
    try:
        session = db.Session()
        dados = session.query(ClienteDB).filter(ClienteDB.id_clinete == id).one()
        session.delete(dados)
        session.commit()
        return {"id": dados.id_clinete,
                "nome do cliente deletado": dados.nome},200
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()