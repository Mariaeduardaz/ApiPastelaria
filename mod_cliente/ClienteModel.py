import db
from sqlalchemy import Column, VARCHAR, CHAR, Integer, BOOLEAN

class ClienteDB(db.Base):


    __tablename__ = 'tb_cliente'
    id_clinete = Column(Integer, primary_key=True, autoincrement=True, index=True)
    nome = Column(VARCHAR(100), nullable=False)
    cpf = Column(CHAR(11),unique=True, nullable=False)
    telefone = Column(CHAR(11), unique=True, nullable=False)
    compra_fiado  = Column(BOOLEAN, nullable=False)
    dia_fiado = Column(Integer, nullable=True)
    senha = Column(VARCHAR(200), nullable=False)

    def __init__(self, id_cliente, nome, cpf, telefone, compra_fiado, dia_fiado, senha):
        self.id_clinete = id_cliente
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.compra_fiado = compra_fiado
        self.dia_fiado = dia_fiado
        self.senha = senha

