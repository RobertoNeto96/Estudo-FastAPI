from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth" , tags=["auth"])

@auth_router.get("/")
async def Autenticação():
    """Essa função é destinada para rota de autenticação"""
    return {"mensagem:" "Voce acessou a rota padrao de Autenticação"}

@auth_router.post("/criar_conta")
async def criar_conta(email , senha)    