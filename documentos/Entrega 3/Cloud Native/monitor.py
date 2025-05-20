import requests
import time
import os
import subprocess

# Configurações
URL_SERVIDOR = "https://edupay-backend.replit.app/healthcheck"  # Altere para sua URL real
INTERVALO_VERIFICACAO = 60  # segundos
COMANDO_RESTART = "kill 1"  # para Replit ou 'npm start' ou 'python main.py' para servidores locais

def servidor_esta_online():
    try:
        resposta = requests.get(URL_SERVIDOR, timeout=5)
        return resposta.status_code == 200
    except Exception as e:
        print(f"[ERRO] Falha ao verificar servidor: {e}")
        return False

def reiniciar_servidor():
    print("[INFO] Reiniciando o servidor...")
    os.system(COMANDO_RESTART)

def monitorar():
    while True:
        if servidor_esta_online():
            print("[OK] Servidor está online.")
        else:
            print("[ALERTA] Servidor está fora do ar. Reiniciando...")
            reiniciar_servidor()
        time.sleep(INTERVALO_VERIFICACAO)

if __name__ == "__main__":
    print("🔄 Iniciando rotina de verificação do servidor...")
    monitorar()
