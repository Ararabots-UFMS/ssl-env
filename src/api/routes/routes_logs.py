from fastapi import APIRouter

router_logs = APIRouter()


@router_logs.post("/build")
def build_vice():
    return {"status": "online", "mensagem": "O motor está rodando perfeitamente!"}

@router_logs.post("/lauch")
def lauch_vice():
    return {"status": "sucesso", "mensagem": "Comando para subir containers recebido."}

@router_logs.post("/clean-cache")
def limpar_cache():
    return {"status": "sucesso", "mensagem": "Cache do vice rodado."}