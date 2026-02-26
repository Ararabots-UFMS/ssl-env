import os
import platform
import subprocess
import sys
import urllib.request
import ctypes
import time

try:
    import questionary
except ImportError:
    print("Biblioteca questionary não encontrada, instale-a")
    sys.exit(1)

def setup_windows_x11():
    vcxsrv_path = r"C:\Program Files\VcXsrv\vcxsrv.exe"
    installer_path = "vcxsrv_installer.exe"
    
    # 1. Checa se está instalado
    if not os.path.exists(vcxsrv_path):
        print("Servidor X11 não detectado. Baixando instalador...")
        url = "https://downloads.sourceforge.net/project/vcxsrv/vcxsrv/1.20.14.0/vcxsrv-64.1.20.14.0.installer.exe"
        urllib.request.urlretrieve(url, installer_path)
        
        print("\n⚠️  Solicitando permissão de Administrador...")
        print("Verifique se há uma janela do Windows piscando na barra de tarefas para confirmar a instalação.")
        
        # Invoca o UAC (Tela de Administrador) usando o verbo "runas"
        retorno = ctypes.windll.shell32.ShellExecuteW(None, "runas", installer_path, "/S", None, 1)
        
        if retorno <= 32: # Na API do Windows, retornos <= 32 significam erro
            print("Erro: Permissão negada pelo usuário ou falha ao iniciar instalador.")
            sys.exit(1)

        print("Instalando silenciosamente em background... Aguarde.")
        
        # Aguarda até o arquivo do servidor existir na pasta (Timeout de 60 segundos)
        timeout = 60
        while not os.path.exists(vcxsrv_path) and timeout > 0:
            time.sleep(1)
            timeout -= 1
            
        if not os.path.exists(vcxsrv_path):
            print("\nErro: A instalação demorou muito ou falhou no meio do caminho.")
            sys.exit(1)
            
        # Limpa o arquivo de instalação
        if os.path.exists(installer_path):
            os.remove(installer_path) 
            
        print("✅ Instalação concluída com sucesso!")

    # 2. Inicia o VcXsrv oculto e sem controle de acesso
    print("Iniciando o servidor de janelas...")
    subprocess.Popen([
        vcxsrv_path, 
        ":0", "-ac", "-multiwindow", "-clipboard", "-wgl"
    ])

def check_docker():
    try:
        subprocess.run(["docker", "info"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def main():
    os_name = platform.system()
    print(f"Sistema detectado: {os_name}")

    if not check_docker():
        print("Docker não está instalado ou não está funcionando.")
        if os_name == "Windows":
            print("Abra o docker desktop para o correto funcionamento")
        elif os_name == "Linux":
            print("Verifique se o daemon do Docker está ativo (systemctl status docker).")
        sys.exit(1)

    if os_name == "Windows":
        print("--- Iniciando setup para windows ---")
        setup_windows_x11()
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
    
if __name__ == "__main__":
    main()