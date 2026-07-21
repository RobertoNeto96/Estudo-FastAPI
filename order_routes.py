from fastapi import APIRouter

order_router = APIRouter(prefix="/order" , tags=["order"])

@order_router.get("/")
async def Ordens():
    return {"mensagem:" "Voce acessou a rota padrao de ordens"}