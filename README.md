# Compilador em Python - IFB

Este é um projeto de construção de um compilador em Python para a disciplina de Compiladores no Instituto Federal de Brasília (IFB).

## Descrição

O objetivo deste projeto é implementar um compilador que seja capaz de traduzir código fonte escrito em uma linguagem específica em código de máquina ou em outra forma de código executável. O compilador será desenvolvido em Python, aproveitando a flexibilidade e facilidade de uso desta linguagem.

## Funcionalidades

O compilador a ser desenvolvido terá as seguintes funcionalidades:

1. Análise léxica: Identificação e classificação de tokens (palavras-chave, identificadores, operadores, delimitadores, etc.) presentes no código fonte.

2. Análise sintática: Verificação da estrutura gramatical correta do código fonte, aplicando regras da linguagem definida.

3. Análise semântica: Verificação de consistência e significado do código fonte, como tipos de dados, escopo de variáveis, entre outros.

4. Geração de código intermediário: Tradução do código fonte em uma representação intermediária, que facilite a otimização e geração do código final.

5. Otimização de código: Realização de otimizações no código intermediário para melhorar a eficiência do programa final.

6. Geração de código de máquina: Tradução do código intermediário em código de máquina, específico para a arquitetura alvo.

## Execução

Para executar o compilador, basta rodar o arquivo "runner.py" no terminal:

```bash
python runner.py
