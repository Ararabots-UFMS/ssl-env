import sys
from api.server import ServidorOrquestrador

def main():
    if len(sys.argv) < 2:
        print("Uso: orquestrador [daemon | up | down]")
        return

    comando = sys.argv[1]

    if comando == "daemon":
        print("Ligando motor! Iniciando API na porta 8080...")
        servidor = ServidorOrquestrador(porta=8080)
        servidor.iniciar()

    elif comando == "up":
        print("Enviando requisição HTTP para daemon (localhost:8080/up)...")

    elif comando == "down":
        print("Enviando requisição HTTP para daemon (localhost:8080/down)...")

    else:
        print(f"Comando '{comando}' não reconhecido.")

if __name__ == "__main__":
    main()