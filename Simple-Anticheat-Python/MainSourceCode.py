import os
import hashlib
import psutil
import requests
import time
import ctypes
import threading
from datetime import datetime
from pathlib import Path

# Cheats conhecidos para monitoramento
cheats_conhecidos = [
    "Cheat Engine", "Trainer", "Wallhack", "Aimbot", "Injector",
    "speedhack", "autoaim", "modded DLL", "external scripts"
]

# Funções importantes que podem ser manipuladas
funcoes_sistema = [
    "OpenProcess", "ReadProcessMemory", "WriteProcessMemory", "CreateRemoteThread"
]

# Integração com API de verificação
API_SECURITY_URL = "https://anticheatapi.com/validate"

# Monitoramento de memória e processos
def monitor_memoria_processos():
    while True:
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                if any(cheat.lower() in proc.info['name'].lower() for cheat in cheats_conhecidos):
                    log_activity(f"Trapaça detectada: {proc.info['name']} (PID: {proc.info['pid']})")
                    terminate_process(proc.info['pid'])
                if any(hook in proc.info['name'] for hook in funcoes_sistema):
                    log_activity(f"Hook detectado em função crítica: {proc.info['name']}")
                    terminate_process(proc.info['pid'])
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        time.sleep(5)

# Relatório de vulnerabilidades para um servidor remoto
def report_cheater(info):
    payload = {'info': info}
    try:
        response = requests.post(API_SECURITY_URL, json=payload)
        if response.status_code == 200:
            log_activity("Relatório enviado com sucesso.")
        else:
            log_activity("Erro ao enviar relatório.")
    except requests.exceptions.RequestException as e:
        log_activity(f"Erro ao reportar: {e}")

# Proteção do anti-cheat
def verificar_integridade_anticheat():
    anti_cheat_hash = calcular_hash_arquivo(__file__)
    while True:
        current_hash = calcular_hash_arquivo(__file__)
        if current_hash != anti_cheat_hash:
            log_activity("Tentativa de alteração do Anti-Cheat detectada!")
            report_cheater("Tentativa de modificação no sistema Anti-Cheat")
            time.sleep(10)

# Funções de log e gerenciamento de arquivos
def log_activity(message):
    with open("anticheat_logs.txt", "a") as log_file:
        log_file.write(f"[{datetime.now()}] {message}\n")
    print(message)

# Função para calcular hash de arquivos
def calcular_hash_arquivo(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

# Início do Anti-Cheat
if __name__ == "__main__":
    log_activity("Iniciando Anti-Cheat reestruturado...")
    log_activity("An Actual Script By BAHOST01!:fire:")
    # Executando as verificações em múltiplas threads
    threading.Thread(target=monitor_memoria_processos).start()
    threading.Thread(target=verificar_integridade_anticheat).start()
