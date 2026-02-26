import os
import platform
import subprocess
import sys
import urllib.request
import ctypes
import time

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

def reinicia_windows_x11():

def desliga_windows_x11():

    