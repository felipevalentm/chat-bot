# Chatbot de Intenções em Python

Este projeto é um protótipo de chatbot que utiliza **reconhecimento de padrões** e **mapeamento de intenções** para interagir com o usuário via terminal. Ele demonstra a lógica fundamental de como IAs processam entradas de texto antes de evoluírem para modelos complexos.

## Funcionalidades

- **Tratamento de Texto:** Limpa automaticamente caracteres especiais (pontuação) e padroniza a entrada para letras minúsculas.
- **Tokenização Simples:** Quebra a frase do usuário em palavras individuais para análise de palavras-chave.
- **Mapeamento de Intenções:** Sistema baseado em dicionários que associa listas de palavras-chave a categorias como "saudação", "compra" ou "despedida".
- **Loop de Interação:** Execução contínua em terminal para conversas em tempo real.

## Como funciona a lógica

O código opera em quatro etapas principais:

1. **Limpeza:** Recebe o texto e remove sinais como `.`, `?`, `!` e `,`.
2. **Normalização:** Transforma tudo em minúsculo e divide a frase em uma lista de palavras.
3. **Busca Cruzada:** Percorre cada palavra dita pelo usuário e verifica se ela existe dentro das listas do dicionário `intencoes`.
4. **Resposta:** Ao identificar a intenção, busca a resposta correspondente no dicionário `resposta`.

## Pré-requisitos

- Python 3.x instalado.

## Como executar

1. Clone o repositório ou baixe o arquivo `.py`.
2. Abra o terminal na pasta do projeto.
3. Execute o comando:
   ```bash
   python nome_do_arquivo.py
