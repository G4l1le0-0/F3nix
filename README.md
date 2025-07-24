# Sistema Bancário Simples em Python

Este projeto é uma simulação de um sistema bancário básico, desenvolvido inteiramente em Python. O objetivo foi criar uma aplicação de console (CLI) que permite ao usuário realizar as operações fundamentais de uma conta bancária, como depósito, saque e visualização de extrato.

Este sistema foi desenvolvido como parte de um desafio de programação da DIO, para praticar conceitos fundamentais de lógica e da linguagem Python.

## Funcionalidades

O sistema oferece um menu interativo com as seguintes opções:

### 1. Depositar

* Permite ao usuário adicionar um valor à sua conta.
* O sistema valida a entrada para garantir que apenas valores positivos sejam depositados.

### 2. Sacar

* Permite ao usuário retirar um valor da conta.
* A operação de saque está sujeita a três regras de negócio:
    1.  **Saldo Suficiente:** O valor do saque não pode ser maior que o saldo atual da conta.
    2.  **Limite por Saque:** O valor de cada saque não pode exceder um limite predefinido (atualmente R$ 500.000,00 no código).
    3.  **Limite de Operações:** O usuário pode realizar um máximo de 3 saques.

### 3. Extrato

* Exibe um histórico de todas as transações realizadas.
* Mostra cada depósito e saque em ordem cronológica.
* Ao final, apresenta o saldo atual da conta de forma clara.

### 4. Sair

* Encerra a aplicação de forma segura.

## Tecnologias Utilizadas

* **Linguagem:** Python 3
* **Conceitos Aplicados:**
    * Manipulação de strings e f-strings para formatação.
    * Estruturas de controle (loops `while` e condicionais `if/elif/else`).
    * Tratamento de exceções com `try-except`.
    * Lógica de programação para validação de regras de negócio.

## Como Executar

1.  Certifique-se de ter o Python 3 instalado em sua máquina.
2.  Clone este repositório ou baixe o arquivo `.py`.
3.  Abra um terminal na pasta onde o arquivo está localizado.
4.  Execute o seguinte comando:
    ```bash
    python challenge_3.py
    
