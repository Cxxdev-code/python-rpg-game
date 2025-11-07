# ⚔️ Projeto RPG de Console - Demonstrando POO em Python

[![Licença MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Feito com](https://img.shields.io/badge/Feito%20com-Python-blue)](https://www.python.org/)

## 👁️ Visão Geral

Este é um projeto simples de jogo de batalha por turnos (**Herói vs. Inimigo**) implementado para demonstrar a aplicação prática de conceitos de **Programação Orientada a Objetos (POO)** e modularização em Python. Ele serve como um excelente estudo de caso para a arquitetura de software em jogos simples de console.

---

## ✨ Conceitos Técnicos Destacados

Este projeto foi construído com foco nos pilares da POO e boas práticas de desenvolvimento:

| Conceito | Aplicação no Código |
| :--- | :--- |
| **Herança** | Classes `Hero` e `Enemy` herdam da classe base `Character`, reutilizando atributos (`name`, `health`, `level`) e lógica de ataque. |
| **Encapsulamento** | Uso de atributos internos (ex: `_health`, `_level`) e propriedades (`@property` / `@setter`) para controle de acesso e validação. |
| **Polimorfismo** | A classe `Hero` implementa o método `special_attack()` que modifica ou amplia o comportamento padrão definido em `Character`. |
| **Modularização** | O código está organizado em múltiplos módulos/arquivos (ex: pasta `models/`, classe `Game` separada da lógica de personagens) para melhor manutenibilidade. |
| **Usabilidade** | Integração com limpeza de terminal (`os.system('cls'/'clear')`) ou pausas de turno para oferecer experiência de console mais fluida. |

---

## 📁 Estrutura do Projeto

A organização do código é modular, separando a lógica de controle (`Game`) das entidades do jogo (`models/`):

| Arquivo/Diretório | Classe | Descrição |
| :--- | :--- | :--- |
| `main.py` | (Nenhum) | **Ponto de entrada.** Cria a instância de `Game` e inicia o loop principal do jogo. |
| `game.py` | `Game` | Gerencia o fluxo de jogo: inicialização, loop de batalha, contagem de derrotas, etc. |
| `models/` | (Diretório) | Contém as classes de modelo/entidade do jogo. |
| `models/character.py` | `Character` | **Classe base.** Contém atributos e métodos comuns para herói e inimigo. |
| `models/hero.py` | `Hero` | Herda de `Character`. Representa o herói do jogador com comportamentos específicos. |
| `models/enemy.py` | `Enemy` | Herda de `Character`. Representa o adversário e sua lógica própria. |

---

## 🚀 Como Executar o Jogo

Certifique-se de ter o **Python instalado (versão 3.6+ recomendada)**.

1.  **Clone o repositório:**

    ```bash
    git clone [https://github.com/Cxxdev-code/RPG_Game.git](https://github.com/Cxxdev-code/RPG_Game.git)
    ```

2.  **Navegue até a pasta do projeto:**

    ```bash
    cd RPG_Game
    ```

3.  **Execute o arquivo principal:**

    ```bash
    python main.py
    ```

---

## 📄 Licença

Distribuído sob a Licença **MIT**. Veja o arquivo `LICENSE` para mais informações.

## ✉️ Contato

* **Autor:** Cxxdev-code
* **GitHub:** [https://github.com/Cxxdev-code/RPG_Game](https://github.com/Cxxdev-code/RPG_Game)
