from fastapi import APIRouter

import os
import platform
import subprocess
import sys
import urllib.request
import ctypes
import time
import core.windows_setup as windows_setup

router_env_setup = APIRouter()


@router_env_setup.post("/setup-ssl-dev")
def setup_ssl_dev():
    os_name = platform.system()
    print(f"Sistema detectado: {os_name}")

    if not windows_setup.check_docker():
        print("Docker não está instalado ou não está funcionando.")
        if os_name == "Windows":
            print("Abra o docker desktop para o correto funcionamento")
        elif os_name == "Linux":
            print("Verifique se o daemon do Docker está ativo (systemctl status docker).")
        sys.exit(1)

    if os_name == "Windows":
        print("--- Iniciando setup para windows ---")
        windows_setup.setup_windows_x11()
        os.environ["DISPLAY"] = "host.docker.internal:0.0"

    elif os_name == "Linux":
        print("--- Iniciando setup para linux ---")
        if not os.environ.get("DISPLAY"):
            os.environ["DISPLAY"] = ":0"

    else:
        print(f"Sistema operacional {os_name} não suportado oficialmente.")

    opcoes_ambientes = {
        "Ambiente de desenvolvimento de software" : ["ssl-vice", "ssl-vision", "ssl-gui", "grSim", "game-controller"],
        "Ambiente de produção de software" : ["ssl-vice-prod"],
        "Ambiente de desenvolvimento de hardware" : ["ssl-eletronica-dev"],
        "Ambiente de desenvolvimento do lugobots" : ["ssl-lugobots-dev"],
        "Ambiente de produção do lugobots" : ["ssl-lugobots-prod"]
    }

    respostas = questionary.checkbox(
        "Selecione quais recursos do projeto você deseja subir agora (Use Espaço para selecionar e Enter para confirmar):",
        choices=list(opcoes_ambientes.keys())
    ).ask()

    if not respostas:
        print("Nenhum recurso selecionado, encerrando automação.")
        sys.exit(0)
    
    servicos_para_subir = set()

    for escolha in respostas:
        for servico in opcoes_ambientes[escolha]:
            servicos_para_subir.add(servico)

    lista_final_servicos = list(servicos_para_subir)

    print(f"\nSubindo os seguintes containeres: {', '.join(lista_final_servicos)}")

    print("\nExecutando Docker Compose...\n")

    comando = ["docker", "compose", "up", "-d", "--build"] + lista_final_servicos

    try:
        subprocess.run(comando, env=os.environ, check=True)
        print("\n✅ Setup finalizado com sucesso!")
        print("Para ver os logs de todos os serviços, digite: docker compose logs -f")
    except subprocess.CalledProcessError:
        print("\n Não foi possível iniciar os containers pelo Docker Compose.")
    return {"status": "online", "mensagem": "O motor está rodando perfeitamente!"}

@router_env_setup.post("/lauch")
def lauch_vice():
    return {"status": "sucesso", "mensagem": "Comando para subir containers recebido."}

@router_env_setup.post("/clean-cache")
def limpar_cache():
    return {"status": "sucesso", "mensagem": "Cache do vice rodado."}