# src/core/adapters/system/base.py
from abc import ABC, abstractmethod

class SystemAdapter(ABC):
    """
    Contrato obrigatório para qualquer Sistema Operacional suportado.
    """

    @abstractmethod
    def setup_display(self) -> None:
        """Configura variáveis de ambiente e servidores X11 necessários."""
        pass

    @abstractmethod
    def abrir_programa(self, nome_programa: str, caminho: str = ".") -> bool:
        """
        Abre um programa externo (ex: 'code' para VSCode).
        Retorna True se conseguiu abrir, False caso contrário.
        """
        pass

    @abstractmethod
    def limpar_cache(self) -> bool:
        """Limpa arquivos temporários do sistema."""
        pass
        
    @abstractmethod
    def obter_ip_host(self) -> str:
        """Retorna o IP da máquina host (útil para o Docker se comunicar com o X11)."""
        pass