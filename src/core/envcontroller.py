# src/core/envcontroller.py
from core.container import iniciar_ambiente_docker
from core.platform_setup import limpar_cache_os, abrir_vscode

class EnvController:
    def __init__(self, nome_ambiente: str, forcar_rebuild: bool, branch_git: str = "main"):
        # O objeto guarda o "estado" do que precisa ser feito
        self.ambiente = nome_ambiente
        self.rebuild = forcar_rebuild
        self.branch = branch_git

    def preparar_ambiente(self):
        """Orquestra o show inteiro na ordem certa."""
        print(f"Iniciando setup do {self.ambiente}...")
        
        # 1. Limpeza
        limpar_cache_os()
        
        # 2. Git (Puxa o código)
        # git_utils.checkout_branch(self.branch)
        
        # 3. Docker
        iniciar_ambiente_docker(self.ambiente, forcar_rebuild=self.rebuild)
        
        # 4. Abre os programas
        abrir_vscode()
        
        return {"status": "sucesso", "mensagem": "Ambiente 100% pronto!"}