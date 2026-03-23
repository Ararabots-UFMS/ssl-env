# src/core/adapters/system/linux.py
import os
import subprocess
from core.adapters.system.base import SystemAdapter

class LinuxAdapter(SystemAdapter):
    def __init__(self):
        # Diferente do Windows, não precisamos de caminhos de instaladores aqui
        pass

    # --- MÉTODOS PÚBLICOS (O Contrato do base.py) ---

    def setup_display(self) -> None:
        """Configura a variável DISPLAY para o X11 no Linux."""
        print("--- Iniciando setup de display para Linux ---")
        
        # No Linux, se a variável DISPLAY não existir, assumimos o display local padrão
        if not os.environ.get("DISPLAY"):
            print("Variável DISPLAY não encontrada. Configurando para ':0'.")
            os.environ["DISPLAY"] = ":0"
        else:
            print(f"Display já configurado: {os.environ.get('DISPLAY')}")

    def abrir_programa(self, nome_programa: str, caminho: str = ".") -> bool:
        # Implementaremos depois
        pass

    def limpar_cache(self) -> bool:
        # Implementaremos depois
        pass

    def obter_ip_host(self) -> str:
        # Implementaremos depois
        pass
        
    # --- MÉTODOS ESPECÍFICOS DO LINUX (Se precisar no futuro) ---
    
    def reiniciar_servico_x11(self) -> None:
        """Exemplo de método específico caso precise reiniciar o X11 no Linux futuramente."""
        pass