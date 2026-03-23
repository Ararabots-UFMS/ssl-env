from pydantic import BaseModel

class EnvRequest(BaseModel):
    nome_ambiente: str
    forcar_rebuild: bool = False
    branch_git: str = "main"

    def short_desc(self) -> str:
        return f"{self.nome_ambiente} ({'rebuild' if self.forcar_rebuild else 'no-rebuild'})"