# ⚔️ Projeto RPG de Console - Demonstrando POO em Python

## Visão Geral
Este é um projeto simples de jogo de batalha por turnos (Heroi vs. Inimigo) implementado para demonstrar a aplicação prática de conceitos avançados de **Programação Orientada a Objetos (POO)** e modularização em Python.

É um projeto ideal para portfólio, mostrando a capacidade de estruturar código limpo e organizado.

## ✨ Conceitos Técnicos Destacados

Este projeto foi construído focando nos pilares da POO:

| Conceito | Aplicação no Código |
| :--- | :--- |
| **Herança** | Classes `Hero` e `Enemy` herdam da classe base `Character`, reutilizando atributos (`name`, `health`, `level`) e o método `attack()`. |
| **Encapsulamento** | Uso de atributos privados (`_name`, `_health`, `_level`) e propriedades (`@property` e `@health.setter`) para garantir que os dados sejam acessados e alterados de forma controlada. |
| **Polimorfismo** | A classe `Hero` implementa um método único (`special_attack()`) que modifica o comportamento de ataque padrão definido na classe `Character`. |
| **Modularização** | O código está separado em dois arquivos: `models/characters.py` (Classes e Lógica POO) e `main.py` (Lógica de Jogo e Execução). |
| **Usabilidade** | Limpeza de terminal dinâmica (`os.system`) a cada turno, proporcionando uma experiência de console mais limpa. |

## 📁 Estrutura do Projeto


# 🚀 Como Executar o Jogo

Certifique-se de ter o Python instalado (versão 3.6+).

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/Cxxdev-code/python-rpg-game.git](https://github.com/Cxxdev-code/python-rpg-game.git)
    ```

2.  **Navegue até a pasta do projeto:**
    ```bash
    cd python-rpg-game
    ```

3.  **Execute o arquivo principal:**
    ```bash
    python main.py
    ```
---
