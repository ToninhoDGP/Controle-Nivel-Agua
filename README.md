# 🚰 Sistema de Monitoramento de Reservatório

Este projeto foi desenvolvido como parte das atividades da **Agenda 11** do curso de **Desenvolvimento de Sistemas (Etec)**. O objetivo é simular um painel de controle que monitora os níveis de água de um reservatório, utilizando feedback visual colorido no terminal para indicar diferentes estados de criticidade.

## 🚀 Funcionalidades

- **Monitoramento por Níveis:** Exibição detalhada de 5 níveis de armazenamento, do crítico ao alerta máximo.
- **Feedback Visual:** Utilização de cores específicas para cada nível, facilitando a interpretação rápida do operador.
- **Modularização:** Código organizado em funções para garantir clareza e facilitar futuras expansões.
- **Simulação Realista:** Estrutura baseada em listas e dicionários, simulando como dados seriam recebidos de sensores reais.

## 🛠️ Tecnologias e Conceitos Utilizados

- **Python 3**: Linguagem base do projeto.
- **Colorama**: Biblioteca utilizada para a estilização de cores no terminal.
- **Estruturas de Dados**: Uso de listas e dicionários para organização das informações.
- **Programação Estruturada**: Aplicação de funções e lógica de decisão (`if/elif`).
- **Git & GitHub**: Controle de versão e documentação do projeto.

## 📋 Arquitetura do Sistema

Em um ambiente industrial real, este software seria a camada de interface. Ele foi projetado para:
1. Receber dados de sensores (simulados neste projeto por valores definidos no código).
2. Processar a criticidade do nível informado.
3. Alertar o usuário visualmente através do console.

## 🔧 Como Executar o Projeto

1. Certifique-se de ter o Python instalado em sua máquina.
2. Instale a biblioteca necessária via terminal:
  
   pip install colorama