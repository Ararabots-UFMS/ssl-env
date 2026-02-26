from fastapi import APIRouter

router_utils = APIRouter()


@router_utils.post("/build")
def build_vice():
    return {"status": "online", "mensagem": "O motor está rodando perfeitamente!"}

@router_utils.post("/lauch")
def lauch_vice():
    return {"status": "sucesso", "mensagem": "Comando para subir containers recebido."}

@router_utils.post("/clean-cache")
def limpar_cache():
    return {"status": "sucesso", "mensagem": "Cache do vice rodado."}