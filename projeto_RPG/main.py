from models.character import Hero, Enemy


class Game:
    def __init__(self):
        self.hero = Hero(name = "Heroi", health = 100, level = 5, skill= "bola de fogo")
        self.enemy = Enemy(name = "Dragão", health = 100, level= 5, kind= "voador")
    

    def start_battle(self):
        print("iniciando batalha!")
        
        while self.hero.health > 0 and self.enemy.health > 0:
            
            print("detlahes do combate")
            print(self.hero.show_details())
            print(self.enemy.show_details())
            
            print("Pressione [enter] para atacar......")
            
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
        else:
            print("voce foi derrotado!")


if __name__ == "__main__":
    manager = Game()
    manager.start_battle()