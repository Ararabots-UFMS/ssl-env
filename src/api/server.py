import uvicorn
from fastapi import FastAPI
from api.routes.routes_env_setup import router_env_setup
from api.routes.routes_logs import router_logs
from api.routes.routes_vice_utils import router_utils

app = FastAPI(title="Motor do Orquestrador", docs_url="/docs", description="API de configuração de env do Arara")

app.include_router(router_utils, prefix="/api/utils")
app.include_router(router_logs, prefix="/api/logs")
app.include_router(router_env_setup, prefix="/api/env-setup")

class ServidorOrquestrador:
    def __init__(self, host="0.0.0.0", porta=8080):
        self.host = host
        self.porta = porta
    
    def iniciar(self):
        print(f"Iniciando o Daemon na porta {self.porta}...")
        uvicorn.run(app, host=self.host, port=self.porta)

    def carregar_certificados(self):
        print("Carregado certificados (Não implementado)")

    def configurar_logs_servidor(self):
        print("Configurando logs do servidor (Não implementado)")