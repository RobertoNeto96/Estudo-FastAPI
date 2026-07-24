from fastapi import APIRouter
from models import Usuario, db
from sqlalchemy.orm import sessionmaker

auth_router = APIRouter(prefix="/auth" , tags=["auth"])

@auth_router.get("/")
async def Autenticação():
    """Essa função é destinada para rota de autenticação"""
    return {"mensagem:" "Voce acessou a rota padrao de Autenticação"}

@auth_router.post("/criar_conta")
async def criar_conta(nome: str , email: str , senha: str) 
    session = sessionmaker(bind=db)
    session = session()
    usuario = session.query(Usuario).filter(Usuario.email==email).first 
    if Usuario:
        return("Ja existe um usuario com esse e-mail")
    else: 
        novo_usuario = Usuario(nome , email , senha)
        session.add(novo_usuario)
        session.commit()
        return("Usuario cadastrado com sucesso")    