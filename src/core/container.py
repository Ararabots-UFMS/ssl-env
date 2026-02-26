
import os
import platform
import subprocess
import sys
import ctypes
import time

AMBIENTES_CONFIG = {
    "ssl_dev": ["ssl-gui", "vision", "grSim", "ssl-vice", "game-controller"],
    "ssl_prod": ["ssl-db-prod", "ssl-api-prod", "ssl-proxy"],
    "lugobots_dev": ["lugo-core", "lugo-simulator"],
    "eletronica_dev": ["eletronica-worker", "eletronica-db"]
}

def check_docker():
    try:
        subprocess.run(["docker", "info"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False
    
def iniciar_container(nome_do_container: str):
    """Inicia um container específico"""
    print(f"Iniciando container individual: {nome_do_container}")
    try:
        r = subprocess.run(["docker", "start", nome_do_container], capture_output=True, text=True)
        if r.returncode == 0:
            print(r.stdout.strip())
            return True
        else:
            print(r.stderr.strip() or r.stdout.strip())
            return False
    except FileNotFoundError:
        print("Docker não encontrado.")
        return False

def parar_container(nome_do_container: str):
    """Parar um container específico"""
    print(f"Parando container: {nome_do_container}")
    try:
        r = subprocess.run(["docker", "stop", nome_do_container], capture_output=True, text=True)
        if r.returncode == 0:
            print(r.stdout.strip())
            return True
        else:
            print(r.stderr.strip() or r.stdout.strip())
            return False
    except FileNotFoundError:
        print("Docker não encontrado.")
        return False

def iniciar_ambiente(nome_ambiente: str):
    """Inicia todos os containers de um ambiente baseado na configuração."""
    
    if nome_ambiente not in AMBIENTES_CONFIG:
        print(f"Erro: Ambiente '{nome_ambiente}' não existe.")
        return False
        
    lista_de_containers = AMBIENTES_CONFIG[nome_ambiente]
    print(f"=== Iniciando o ambiente: {nome_ambiente} ===")
    
    for container in lista_de_containers:
        iniciar_container(container)
        
    print(f"=== Ambiente {nome_ambiente} totalmente iniciado! ===")
    return True

def parar_ambiente(nome_ambiente: str):
    """Para todos os containers de um ambiente."""
    if nome_ambiente not in AMBIENTES_CONFIG:
        return False

    print(f"=== Encerrando o ambiente: {nome_ambiente} ===")
    for container in reversed(AMBIENTES_CONFIG[nome_ambiente]): # Reverso para não quebrar dependências
        parar_container(container)
    return True

def reiniciar_docker():
    """Limpa todos os valores de docker no computador"""
    print("Executando o prune e tentando reiniciar o daemon Docker...")
    try:
        subprocess.run(["docker", "system", "prune", "-af", "--volumes"], check=False)
    except FileNotFoundError:
        print("Docker não encontrado para prune.")
        return False
    
    system = platform.system().lower()
    try:
        if system == "windows":
            subprocess.run(["powershell", "-Command", "Restart-Service -Name com.docker.service"], check=False)
        elif system == "linux":
            subprocess.run(["systemctl", "restart", "docker"], check=False)
        else:
            print("Plataforma desconhecida, ignora reinício automático do daemon.")
    except Exception as e:
        print(f"Erro ao tentar reiniciar Docker: {e}")
        return False
    
    print("Reinicio solicitado, aguarde.")
    return True

def obter_status_container(nome_do_container: str):
    """Verifica se um container específico está rodando (Running, Exited, etc)."""
    try:
        r = subprocess.run(["docker", "inspect", "-f", "{{.State.Status}}", nome_do_container], capture_output=True, text=True)

        if r.returncode == 0:
            return r.stdout.strip()
        return None
    except FileNotFoundError:
        print("Docker não encontrado.")
        return None

def listar_containers_do_ambiente(nome_ambiente: str):
    """Retorna uma lista de quais containers de um ambiente estão no ar."""
    if nome_ambiente not in AMBIENTES_CONFIG:
        print(f"Erro: Ambiente '{nome_ambiente}' não existe.")
        return None
    resultado = {}
    for c in AMBIENTES_CONFIG[nome_ambiente]:
        resultado[c] = obter_status_container(c)
    return resultado

def build_ambiente(nome_ambiente: str):
    """Força o build das imagens de um ambiente específico."""
    if nome_ambiente not in AMBIENTES_CONFIG:
        print(f"Erro: Ambiente '{nome_ambiente}' não existe.")
        return False
    sucesso = True
    for servico in AMBIENTES_CONFIG[nome_ambiente]:
        print(f"Build de serviço: {servico}")
        r = subprocess.run(["docker", "compose", "build", servico], capture_output=True, text=True)
        print(r.stdout.strip())
    return sucesso

def executar_comando_no_container(nome_do_container: str, comando: str):
    """Roda um comando pontual dentro de um container que já está rodando."""
    try:
        r = subprocess.run(["docker", "exec", "-i", nome_do_container, "sh", "-c", comando], capture_output=True, text=True)
        return (r.returncode, r.stdout, r.stderr)
    
    except FileNotFoundError:
        return (1, "", "Docker não encontrado.")
    