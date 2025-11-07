from models.character import Character
from models.hero import Hero
from models.enemy import Enemy
import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
class Game:
    def __init__(self):
              self.hero = Hero(name = "Heroi", health = 100, level = 5, skill= "bola de fogo", mana = 100)
              self._death = 0


    def __str__(self):
        return (f"Herói: {self.hero.name} | "
                f"Nível: {self.hero.level} | "
                f"Inimigos derrotados: {self._death}")
         
    @property
    def death(self):
         return self._death
    
    @death.setter
    def death(self,mortes):
        self._death += mortes
        if self.death % 2 == 0:
                    print("Você atingiu mais 2 inimigos derrotados. Subindo de nível!")
                    self.hero.up_level()


    

    def start_battle(self):
        

        while True:
            self.enemy = Enemy(name = "Dragão", health = 20, level= 5, kind= "voador")
            print("iniciando batalha!")
            while self.hero.health > 0 and self.enemy.health > 0:

                print("detlahes do combate:")
                print(self.hero.show_details())
                print(self.enemy.show_details())
                
                iniciar = str(input("Pressione [enter] para atacar......"))
                clear_screen()

            
                try:
                    opc = (int(input("[1] para ataque normal---[2] para ataque especial: ")))
                
                    if opc == 1:
                        self.hero.attack(self.enemy)
                    elif opc == 2:
                        self.hero.special_attack(self.enemy)
                    else:
                        print("ataque invalido")
            
                except ValueError:
                    print("Opção inválida.")
            
                if self.enemy.health > 0:
                    self.enemy.attack(self.hero)
            
            
                input("\n[Resultado do Turno Acima] Pressione [Enter] para o próximo turno...")
                

            if self.hero.health > 0:
                print("Parabens voce ganhou!")
                self.death = 1
                print(self)

            else:
                print("voce foi derrotado!")
        
            resposta = input("Deseja continuar [s/n]? ").strip().lower()
            if resposta == "s" or resposta == "sim":
                print("Preparando nova batalha...")
                # resetar herói ou atualizar conforme necessidade
                self.hero.health = 100
                self.hero.mana = 100
                continue
            else:
                print("Fim do jogo. Até a próxima!")
                break
            


if __name__ == "__main__":
    manager = Game()
    manager.start_battle()


