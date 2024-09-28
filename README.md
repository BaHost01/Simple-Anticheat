# Python Anti-Cheat

Este projeto é um **Anti-Cheat** simples em Python, projetado para detectar trapaças e programas maliciosos que interfiram no jogo. O Anti-Cheat realiza verificações periódicas de processos, acessos a sites suspeitos, hooks em funções críticas do sistema e modificações de memória. Ele também permite registrar logs de atividades suspeitas e enviar relatórios para um servidor de anti-cheat central.

## Funcionalidades

- **Verificação de Processos Suspeitos**: Detecta se processos como `Cheat Engine`, `Trainer`, ou `Injector` estão sendo executados.
- **Bloqueio de Sites de Cheats**: Verifica tentativas de acessar sites conhecidos de cheats e bloqueia essas conexões.
- **Verificação de Hooks**: Garante que funções críticas do sistema, como `ReadProcessMemory` e `WriteProcessMemory`, não foram alteradas.
- **Detecção de Modificações de Memória**: Identifica modificações suspeitas na memória do jogo e alerta.
- **Log de Atividades**: Cria logs de eventos suspeitos para futuras análises.
- **Relatório de Cheaters**: Envia informações para um servidor de anti-cheat sobre jogadores que tentam usar trapaças.

## Requisitos

- Python 3.x
- Bibliotecas Python:
  - `psutil`
  - `requests`
  - `ctypes`
  - `hashlib`


##Isso Foi Tudo
