from sqlalchemy import create_engine , Column, String , Integer , Boolean , Float , ForeignKey , DateTime
from sqlalchemy.orm import declarative_base


db = create_engine("sqlite:///banco.db")

base = declarative_base()

class Usuario(base):
    __tablename__ = "usuarios"

    id = Column("id" , Integer , primary_key=True , autoincrement=True)
    nome = Column("nome" , String , nullable=False)
    email = Column("email" , String ,)
    senha = Column("senha" , String , nullable=False)

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


class Jogo(base):
    __tablename__="jogos"

    id = Column("id" , Integer , primary_key=True , autoincrement=True)        
    nome = Column("nome" , String , nullable=False)
    preco = Column("preço" , Float , nullable=False)
    descricao = Column("descrição" , String , nullable=False)
    categoria = Column("categoria" , String)

    def __init__(self , nome , preco , descricao , categoria):
        self.nome = nome
        self.preco = preco
        self.descricao = descricao
        self.categoria = categoria 


class Compra(base):
    __tablename__="compras"

    id = Column("id" , Integer , primary_key=True , autoincrement=True)
    id_compra = Column("id_compra" , Integer, ForeignKey("usuarios.id"))
    data_compra = Column("data_compra" , DateTime)
    valor_total = Column("valor_total" , Float)

    def __init__(self , id_compra , data_compra , valor_total):
        self.id_compra = id_compra
        self.data_compra = data_compra
        self.valor_total = valor_total


class Biblioteca(base):
    __tablename__ = 'bibliotecas'

    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    jogo_id = Column(Integer, ForeignKey('jogos.id'), nullable=False)
    horas_jogadas = Column(Integer, default=0) 

    def __init__(self , usuario_id , jogo_id , horas_jogadas):
        self.usuario_id = usuario_id
        self.jogo_id = jogo_id
        self.horas_jogadas = horas_jogadas

        