# ⚔️ Projeto RPG de Console - Demonstrando POO em Python

## Visão Geral  
Este é um projeto simples de jogo de batalha por turnos (Herói vs. Inimigo) implementado para demonstrar a aplicação prática de conceitos avançados de **Programação Orientada a Objetos (POO)** e modularização em Python.

É um excelente projeto para portfólio, mostrando a capacidade de estruturar código limpo e organizado.

## ✨ Conceitos Técnicos Destacados  
Este projeto foi construído com foco nos pilares da POO:

| Conceito           | Aplicação no Código                                                                 |
| :----------------- | :--------------------------------------------------------------------------------- |
| **Herança**         | Classes `Hero` e `Enemy` herdam da classe base `Character`, reutilizando atributos (`name`, `health`, `level`) e lógica de ataque. |
| **Encapsulamento**  | Uso de atributos internos (ex: `_health`, `_level`) e propriedades (`@property` / `@setter`) para controle de acesso e validação. |
| **Polimorfismo**    | A classe `Hero` implementa método `special_attack()` que modifica ou amplia o comportamento padrão definido em `Character`. |
| **Modularização**   | O código está organizado em múltiplos módulos/arquivos (ex: pasta `models/`, classe `Game` separada da lógica de personagens) para melhor manutenibilidade. |
| **Usabilidade**     | Integração com limpeza de terminal (`os.system('cls'/'clear')`) ou pausas de turno para oferecer experiência de console mais fluida. |

## 📁 Estrutura do Projeto  

python-rpg-game/
│
├─ models/
│ ├─ character.py # Classe base Character e possivelmente outras classes comuns
│ ├─ hero.py # Classe Hero (herói do jogador)
│ └─ enemy.py # Classe Enemy (inimigo)
│
├─ game.py # Classe Game que gerencia o fluxo de jogo (inicialização, loop de batalha, etc.)
├─ main.py # Ponto de entrada para iniciar o jogo
└─ README.md # Este arquivo de documentação

## 🚀 Como Executar o Jogo  
Certifique-se de ter o Python instalado (versão 3.6+ recomendada).  
1. **Clone o repositório:**  
   ```bash
   git clone https://github.com/Cxxdev-code/python-rpg-game.git
2. **Navegue até a pasta do projeto:**
    ```bash
  cd python-rpg-game
3.**Execute o arquivo principal:**
   python main.py
Footer
© 2025 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
C
