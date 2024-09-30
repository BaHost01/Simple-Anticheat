# Anti-Cheat Lua - Rework Completo

Este é o novo Anti-Cheat reestruturado em **Lua**, com melhorias significativas em segurança e detecção. O sistema agora conta com monitoramento de processos e hooks críticos, detecção de injeção de código, e proteção contra modificação do próprio Anti-Cheat.

## Funcionalidades

- **Monitoramento de processos e hooks críticos**: Verifica constantemente os processos em execução para detectar tentativas de trapaça e manipulação de funções críticas do sistema.
- **Detecção de injeção de código**: O Anti-Cheat monitora scripts e executáveis para evitar injeções maliciosas.
- **Proteção do Anti-Cheat**: Verifica a integridade do próprio Anti-Cheat, protegendo contra tentativas de modificação.
- **Relatórios automáticos**: Envia relatórios automaticamente para um servidor remoto em caso de detecção de cheats.
- **Suporte para Jogos do Roblox**: Inclui verificações de trapaça adaptadas para jogos dentro da plataforma Roblox.

## Instalação

1. Baixe ou clone o repositório:
    ```bash
    git clone https://github.com/seuusuario/anticheat-lua-rework.git
    cd anticheat-lua-rework
    ```

2. Execute o script Lua:
    ```bash
    lua anticheat.lua
    ```

## Relatando Trapaças

Caso você encontre trapaças não detectadas pelo sistema, envie um email para [cleasantos1994@gmail.com](mailto:cleasantos1994@gmail.com) ou entre em contato via Discord: `agente0981`.

## Contribuições

Contribuições são bem-vindas. Abra um pull request no GitHub para propor suas melhorias ou correções.
