# **Sistema Bancário Simples em Python (Versão 1.2)**

Este projeto é uma simulação de um sistema bancário, desenvolvido inteiramente em Python. O objetivo desta versão foi refatorar completamente o sistema, migrando de uma estrutura puramente funcional para uma arquitetura baseada em **Programação Orientada a Objetos (POO)**.

Esta evolução alinha o projeto com práticas de desenvolvimento mais robustas, melhorando a organização, a reutilização de código e a manutenibilidade, seguindo um diagrama de classes predefinido.

## **Funcionalidades**

As funcionalidades do sistema para o usuário final permanecem as mesmas, mas agora são sustentadas por uma estrutura de classes e objetos. O menu interativo continua a oferecer as seguintes opções:

### **1\. Depositar, Sacar e Extrato**

* As operações de **depósito**, **saque** e **extrato** agora são métodos das classes Conta e ContaCorrente.  
* A lógica de negócio (limite de R$ 500 por saque, máximo de 3 saques diários) está encapsulada dentro da classe ContaCorrente, tornando as regras mais claras e isoladas.

### **2\. Novo Usuário**

* Permite cadastrar um novo cliente, que agora é representado pelo objeto PessoaFisica.  
* O sistema continua a validar CPFs para evitar duplicatas.

### **3\. Nova Conta**

* Permite criar uma nova ContaCorrente.  
* A conta é diretamente vinculada a um objeto Cliente (ou PessoaFisica), fortalecendo a relação entre os dados.

### **4\. Listar Contas**

* Exibe uma lista de todas as contas criadas, utilizando o método \_\_str\_\_ da classe ContaCorrente para uma formatação limpa e padronizada.

### **5\. Sair**

* Encerra a aplicação.

## **Principais Mudanças da Versão 1.2**

A principal mudança foi a **adoção da Programação Orientada a Objetos**. O código, que antes era dividido em funções que manipulavam dicionários e listas, agora é estruturado em classes que representam as entidades do sistema bancário.

## **Tecnologias e Conceitos Aplicados**

* **Linguagem:** Python 3  
* **Bibliotecas:** textwrap, datetime, abc (para classes abstratas).  
* **Conceitos de POO Aplicados:**  
  * **Classes e Objetos:** O sistema foi modelado com classes como Cliente, PessoaFisica, Conta, ContaCorrente, Historico e Transacao.  
  * **Herança:** A classe PessoaFisica herda de Cliente, e ContaCorrente herda de Conta, reutilizando atributos e métodos.  
  * **Encapsulamento:** Atributos sensíveis (como \_saldo) são protegidos e acessados através de métodos ou propriedades (@property), garantindo maior controle sobre os dados.  
  * **Polimorfismo e Classes Abstratas:** Foi criada uma classe abstrata Transacao com as filhas Saque e Deposito, permitindo que o sistema trate diferentes tipos de transação de maneira uniforme.  
  * **Métodos Mágicos:** Uso do \_\_init\_\_ (construtor) e \_\_str\_\_ (representação em string) para gerenciar o ciclo de vida e a exibição dos objetos.

## **Como Executar**

1. Certifique-se de ter o Python 3 instalado em sua máquina.  
2. Baixe o arquivo .py da versão 1.2.  
3. Abra um terminal na pasta onde o arquivo está localizado.  
4. Execute o seguinte comando:  
   python nome\_do\_arquivo.py  
