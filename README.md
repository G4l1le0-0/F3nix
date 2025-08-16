[README_1.1.md](https://github.com/user-attachments/files/21813647/README_1.1.md)
# **Sistema Bancário Simples em Python (Versão 1.1)**

Este projeto é uma simulação de um sistema bancário, desenvolvido inteiramente em Python. O objetivo inicial foi criar uma aplicação de console (CLI) para operações fundamentais. Esta versão evoluiu o sistema para uma estrutura mais robusta e modular, utilizando funções e adicionando novas funcionalidades de gerenciamento de usuários e contas.

Este sistema foi desenvolvido como parte de um desafio de programação da DIO, para praticar e aprofundar conceitos da linguagem Python.

## **Funcionalidades (Atualizado)**

O sistema foi refatorado e agora conta com um menu interativo com as seguintes opções:

### **1\. Depositar, Sacar e Extrato**

* As funcionalidades originais de **depósito**, **saque** e **extrato** foram mantidas, mas agora são gerenciadas por funções dedicadas, tornando o código mais limpo e organizado.  
* As regras de negócio (limite de R$ 500 por saque, máximo de 3 saques diários) continuam as mesmas.

### **2\. Novo Usuário**

* Permite cadastrar um novo cliente (usuário) no sistema.  
* O sistema solicita nome, data de nascimento, CPF e endereço.  
* **Validação de CPF:** Impede o cadastro de CPFs duplicados.  
* **Validação de Entradas:** Garante que os dados inseridos (CPF, nome, data de nascimento, endereço) sigam um formato e regras mínimas de validação.

### **3\. Nova Conta**

* Permite criar uma nova conta corrente.  
* A conta é vinculada a um usuário já cadastrado através do seu CPF.  
* Cada nova conta recebe um número sequencial e está associada à agência padrão "0001".

### **4\. Listar Contas**

* Exibe uma lista com todas as contas correntes cadastradas, mostrando a agência, o número da conta e o nome do titular.

### **5\. Sair**

* Encerra a aplicação de forma segura.

## **Tecnologias Utilizadas**

* **Linguagem:** Python 3  
* **Bibliotecas:** textwrap (para formatação do menu) e datetime (para validação de datas).  
* **Conceitos Aplicados:**  
  * **Modularização com Funções:** Todo o código foi separado em funções com responsabilidades únicas.  
  * **Estruturas de Dados:** Uso de listas e dicionários para armazenar e gerenciar os dados de usuários e contas em memória.  
  * **Argumentos de Função Específicos:** Aplicação de positional-only (/) e keyword-only (\*) na definição das funções de depósito, saque e extrato, conforme o desafio.  
  * Manipulação de strings e f-strings.  
  * Estruturas de controle (while, if/elif/else).  
  * Lógica de programação para validação de regras de negócio e entradas do usuário.

## **Como Executar**

1. Certifique-se de ter o Python 3 instalado em sua máquina.  
2. Clone este repositório ou baixe o arquivo challenge\_3.1.py.  
3. Abra um terminal na pasta onde o arquivo está localizado.  
4. Execute o seguinte comando:  
   python challenge\_3.1.py  
