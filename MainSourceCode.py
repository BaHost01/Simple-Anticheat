import os
import sys
import hashlib
import time
import psutil
import ctypes
import requests
from datetime import datetime
from ctypes import wintypes

# Base de dados de cheats conhecidos e sites
cheats_conhecidos = [
    'cheatengine', 'injector', 'trainer', 'aimbot', 'wallhack', 'esp', 'flyhack',
    'www.cheatsite1.com', 'www.hacks4you.com'
]

# Função para verificar processos e sites conhecidos
def verificar_processos_e_sites():
    print("Verificando processos e tentativas de acesso a sites suspeitos...")
    processos_suspeitos = [proc.lower() for proc in cheats_conhecidos]
    
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if any(proc_name in proc.info['name'].lower() for proc_name in processos_suspeitos):
                print(f"ALERTA: Processo suspeito encontrado: {proc.info['name']} (PID: {proc.info['pid']})")
                log_suspeito(f"Processo suspeito: {proc.info['name']} detectado.")
                return False
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    print("Nenhum processo ou site suspeito encontrado.")
    return True

# Verifica acessos suspeitos a sites de cheats
def bloquear_acesso_a_sites():
    sites_bloqueados = cheats_conhecidos
    print("Bloqueando acesso a sites de cheats...")

    for site in sites_bloqueados:
        try:
            response = requests.get(f"http://{site}")
            if response.status_code == 200:
                print(f"ALERTA: Tentativa de acessar o site {site} bloqueada.")
                log_suspeito(f"Tentativa de acessar site de cheats: {site}")
        except requests.ConnectionError:
            continue

# Função para registrar eventos suspeitos
def log_suspeito(mensagem):
    with open("anticheat_logs.txt", "a") as log_file:
        log_file.write(f"{datetime.now()} - {mensagem}\n")

# Função para reportar cheaters
def reportar_cheater(mensagem):
    # Exemplo de comunicação com servidor externo para reportar cheaters
    servidor_url = "http://seuservidordeanticheat.com/report"
    dados = {"mensagem": mensagem, "data": str(datetime.now())}
    
    try:
        response = requests.post(servidor_url, data=dados)
        if response.status_code == 200:
            print("Cheater reportado com sucesso.")
        else:
            print("Falha ao reportar cheater.")
    except requests.RequestException as e:
        print(f"Erro ao reportar cheater: {e}")

# Função para verificar hooks em funções críticas
def verificar_hooks_funcao(funcao_nome):
    print(f"Verificando se a função {funcao_nome} foi hookada...")
    kernel32 = ctypes.windll.kernel32
    funcao_endereco = kernel32.GetProcAddress(kernel32.GetModuleHandleA(b'kernel32.dll'), funcao_nome.encode('utf-8'))
    
    # Verificar se o primeiro byte da função foi modificado
    if funcao_endereco != 0:
        primeiro_byte = ctypes.cast(funcao_endereco, ctypes.POINTER(ctypes.c_char)).contents.value
        if primeiro_byte == b'\xE9':  # 0xE9 é o opcode para o comando JMP, comum em hooks
            print(f"ALERTA: Função {funcao_nome} foi hookada!")
            log_suspeito(f"Hook detectado na função: {funcao_nome}")
            return False
    print(f"A função {funcao_nome} está limpa.")
    return True

# Função para verificar hooks em várias funções críticas
def verificar_hooks():
    funcoes_criticas = ['ReadProcessMemory', 'WriteProcessMemory', 'VirtualProtect', 'CreateRemoteThread']
    for funcao in funcoes_criticas:
        if not verificar_hooks_funcao(funcao):
            return False
    return True

# Verifica modificações de memória (Anti-cheat básico)
def verificar_memoria_suspeita():
    print("Verificando modificações de memória suspeitas...")
    kernel32 = ctypes.windll.kernel32
    processos = psutil.process_iter(['pid', 'name'])
    for proc in processos:
        try:
            process_handle = kernel32.OpenProcess(0x0010, False, proc.info['pid'])  # 0x0010 = PROCESS_VM_READ
            if process_handle:
                memoria_base = kernel32.VirtualAllocEx(process_handle, None, 0, 0x3000, 0x04)
                if memoria_base:
                    print(f"ALERTA: Modificação de memória detectada no processo {proc.info['name']} (PID: {proc.info['pid']})")
                    log_suspeito(f"Modificação de memória detectada: {proc.info['name']}")
                    return False
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    print("Nenhuma modificação de memória suspeita encontrada.")
    return True

# Loop principal do Anticheat
def anticheat_loop(arquivo_hash):
    while True:
        if not verificar_processos_e_sites():
            print("Encerrando jogo devido a trapaça detectada.")
            sys.exit()

        bloquear_acesso_a_sites()

        if not verificar_hooks():
            print("Encerrando jogo devido a hooks detectados.")
            sys.exit()

        if not verificar_memoria_suspeita():
            print("Encerrando jogo devido a manipulação de memória.")
            sys.exit()

        print("Nenhuma trapaça detectada. Verificação completa.")
        time.sleep(10)  # Verifica novamente após 10 segundos

# Exemplo de verificação de integridade de arquivos
arquivo_hash = {
    "C:/caminho/para/jogo/game.exe": "e99a18c428cb38d5f260853678922e03abd8334d",
    "C:/caminho/para/jogo/assets/texture.png": "d4735e3a265e16eee03f59718b9b5d03dc017607"
}

# Iniciar o loop do anticheat
if __name__ == "__main__":
    print("Anticheat Iniciado.")
    anticheat_loop(arquivo_hash)
