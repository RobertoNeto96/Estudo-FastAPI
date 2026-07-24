from sqlalchemy import create_engine, Column, String, Integer, Float, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base

# 1. Conexão
db = create_engine("sqlite:///banco.db")
base = declarative_base()

# 2. Tabelas
class Usuario(base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True)
    senha = Column(String, nullable=False)


class Jogo(base):
    __tablename__ = "jogos"

    id = Column(Integer, primary_key=True, autoincrement=True)        
    nome = Column(String, nullable=False)
    preco = Column(Float, nullable=False)
    descricao = Column(String, nullable=False)  # Sem acento!
    categoria = Column(String)


class Compra(base):
    __tablename__ = "compras"

    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))  # Ajustado para usuario_id
    data_compra = Column(DateTime)
    valor_total = Column(Float)


class Biblioteca(base):
    __tablename__ = "bibliotecas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    jogo_id = Column(Integer, ForeignKey("jogos.id"), nullable=False)
    horas_jogadas = Column(Integer, default=0)


# 3. Cria o banco de dados na sua pasta!
base.metadata.create_all(bind=db)