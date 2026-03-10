# Python + SQLite | Gerenciamento de Tabelas

Este repositório contém exercícios práticos de estudo sobre manipulação de banco de dados SQLite utilizando Python.  
O objetivo é demonstrar a criação e modificação da estrutura de tabelas através de comandos SQL executados via Python.

## Tecnologias utilizadas

- Python 3
- SQLite3 (biblioteca padrão do Python)
- SQL (DDL – Data Definition Language)

## Estrutura do projeto
├── banco/
│ └── banco.db
├── comandos_db.py
├── add_coluna.py
└── ordem_coluna.py

## Descrição dos arquivos

### comandos_db.py
Script responsável por criar as tabelas do banco de dados:

- **Pessoa**
- **Marca**
- **Veiculo**

Também define:
- chaves primárias
- chaves estrangeiras
- tipos de dados

### add_coluna.py
Demonstra como alterar a estrutura de uma tabela existente utilizando: ALTER TABLE


Neste caso, adiciona a coluna `motor` à tabela `Veiculo`.

### ordem_coluna.py
Exemplo de recriação de tabela para alterar a ordem das colunas.  
O script remove a tabela `Veiculo` e a recria com a nova estrutura.

## Conceitos praticados

- Criação de tabelas (`CREATE TABLE`)
- Alteração de tabelas (`ALTER TABLE`)
- Exclusão de tabelas (`DROP TABLE`)
- Definição de chaves primárias
- Definição de chaves estrangeiras
- Integração entre Python e SQLite

## Objetivo

Este projeto faz parte do meu processo de aprendizado em banco de dados e desenvolvimento em Python, com foco em compreender como aplicações podem manipular e estruturar bancos de dados relacionais.
