
from models.hero import Hero
from models.enemy import Enemy
from models.DataManager import DataManager
from models.items import Item
from colorama import init, Fore, Style
import random
import os
import time


init()


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


class Game:
    def __init__(self):
        path = os.path.join("RPG","Data","save.json")
        self.data_manager = DataManager(path)
        self._death = 0
        player_data = self.data_manager.Load_Game()
        if player_data:
            weapon_data = player_data["Arma"]
            weapon = None
            if weapon_data and weapon_data != "desarmado":
                weapon = Item(
                weapon_data["nome"],
                weapon_data["tipo"],
                weapon_data["dano"],
                )
                
                self.hero = Hero(
                player_data["Nome"],
                player_data["Vida"],
                player_data["Nivel"],
                player_data["Habilidade"],
                player_data["Mana"],
                weapon,
                )
        else:
            self.hero = Hero("Arthur", 100, 12, "Golpe Inicial", 100)
            self.enemy = None


    def __str__(self):
        return (
        f"Herói: {self.hero.name} | "
        f"Nível: {self.hero.level} | "
        f"Inimigos derrotados: {self._death}"
        )


    @property
    def death(self):
        return self._death


    @death.setter
    def death(self, amount):
        self._death += amount
        if self._death % 3 == 0:
            print("Você atingiu mais 3 inimigos derrotados. Subindo de nível\n")
            self.hero.up_level()
            
    def random_items(self):
        weapons = [
        {"nome": "Espada Curta", "tipo": "corpo a corpo", "dano": 16},
        {"nome": "Espada Longa", "tipo": "corpo a corpo", "dano": 18},
        {"nome": "Katana", "tipo": "corpo a corpo", "dano": 10},
        {"nome": "Machado de Batalha", "tipo": "corpo a corpo", "dano": 18},
        {"nome": "Maça", "tipo": "corpo a corpo", "dano": 20},
        {"nome": "Lança", "tipo": "haste / perfurante", "dano": 15},
        ]
        
        selected = random.choice(weapons)
        return Item(selected["nome"], selected["tipo"], selected["dano"])
    def death(self, deaths):
        self._death += deaths
        if self.death % 2 == 0:
                    print("Você atingiu mais 2 inimigos derrotados. Subindo de nível!")
                    self.hero.up_level()


    def handle_victory(self):
        print(Fore.GREEN + "Parabéns! Você ganhou a batalha!\n" + Style.RESET_ALL)
        self.death += 1
    
        if self._death % 3 == 0: 
            item = self.random_items()
            print(f"Você encontrou: {item.show_details()}")
            
            
            while True:
                try:
                    equip_choice = input("Deseja equipar esta arma? [s] [n]").lower().strip()
                    if equip_choice == "s":
                        self.hero.weapon = item
                        print(Fore.CYAN + "Arma equipada!\n" + Style.RESET_ALL)
                        break
                    elif equip_choice == "n":
                        print("Arma jogada no lixo..\n")
                        break 
                    else:
                        print("Digite apenas 's' ou 'n' para continuar.\n")
                except Exception: 
                    print("Ocorreu um erro inesperado ao processar a escolha.\n")

        
        while True:
            try:
                save_choice = input("Deseja salvar o jogo? [s] [n]:").lower().strip()
                
                if save_choice == "s":
                    
                    self.hero.health = 100
                    self.hero.mana = 100
                    self.data_manager.save_game(self.hero.to_dict()) 
                    print(Fore.YELLOW + "Jogo salvo com sucesso!\n" + Style.RESET_ALL)
                    
                    break 
                    
                elif save_choice == "n":
                    print("Espere o próximo ponto de salvamento!\n")
                    break 

                
                else:
                    print("Digite apenas 's' ou 'n' para salvar.\n")
                    
            except Exception as e:
                
                print(f"❌ Erro ao tentar salvar o jogo: {e}\n")
                break 


    def get_enemy_level(self):
        hero_level = self.hero.level
        min_lvl = 1 if hero_level < 3 else hero_level // 2
        max_lvl = hero_level + random.randint(0, 2)
        return random.randint(min_lvl, max_lvl)

    def spawn_random_enemy(self):
        templates = [
        {"name": "Goblin", "base_health": 20, "health_per_level": 7, "kind": "terra"},
        {"name": "Esqueleto", "base_health": 15, "health_per_level": 5, "kind": "terra"},
        {"name": "Orc", "base_health": 30, "health_per_level": 9, "kind": "terra"},
        {"name": "Dragão", "base_health": 50, "health_per_level": 15, "kind": "voador"},
        {"name": "Lobo", "base_health": 18, "health_per_level": 7, "kind": "animal"},
        ]


        chosen = random.choice(templates)
        lvl = self.get_enemy_level()
        health = chosen["base_health"] + chosen["health_per_level"] * (lvl - 1)


        return Enemy(chosen["name"], health, lvl, chosen["kind"])

    def run_battle_loop(self):
        while self.hero.health > 0 and self.enemy.health > 0:
            clear_screen()
            print("--- Detalhes do Combate ---")
            print(self.hero.show_details())
            print(self.enemy.show_details())


            input("Pressione [Enter] para " + Fore.RED + "atacar..." + Style.RESET_ALL)


            try:
                choice = int(input("[1] Ataque Normal | [2] Ataque Especial: "))
                if choice == 1:
                    self.hero.attack(self.enemy)
                elif choice == 2:
                    self.hero.special_attack(self.enemy)
                else:
                    print(Fore.RED + "Ação inválida." + Style.RESET_ALL)
            except ValueError:
                print(Fore.RED + "Ação inválida. Turno perdido." + Style.RESET_ALL)


            if self.enemy.health <= 0:
                break

            else:   
                self.enemy.attack(self.hero)
                input("[Resultado do Turno Acima] Pressione [Enter] para o próximo turno...")
        
    def start_battle(self):
        while True:
            self.enemy = self.spawn_random_enemy()
            print(Fore.MAGENTA + f"Iniciando batalha contra {self.enemy.name}!" + Style.RESET_ALL)
            time.sleep(1)

            self.run_battle_loop()

            if self.hero.health > 0 and self.enemy.health <= 0:
                self.handle_victory()
            else:
                print(Fore.RED + "Você foi derrotado! Fim de jogo." + Style.RESET_ALL)

            while True:
                cont = input("Deseja continuar [s/n]? ").strip().lower()
                if cont in ("s"):
                    clear_screen()
                    print("Preparando nova batalha...")
                    time.sleep(1)
                    self.hero.health = 100
                    self.hero.mana = 100
                    break
                if cont in ("n"):
                    print("Fim do jogo. Até a próxima!")
                    break
                
                else:
                    print("Digite apenas as letras correspondentes")
                    

if __name__ == "__main__":
    manager = Game()
    manager.start_battle()


