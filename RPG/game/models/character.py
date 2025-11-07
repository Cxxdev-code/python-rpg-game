import random

class Character: 
    def __init__(self, name, health, level): 
        self._name = name
        self._health = health
        self._level = level

    @property
    def name(self):
        return self._name

    @property
    def health(self):
        return self._health
    
    @health.setter
    def health(self, new_health): 
        self._health = new_health
    
    @property
    def level(self):
        return self._level
    
    
    def show_details(self): 
        return f"\nNome: {self.name} \nVida:❤️ {self.health} \nNivel:💎 {self.level}"
    
    
    def receive_attack(self, damage):
        self.health -= damage
        if self.health <=0:
            self.health = 0  
    
    
    def attack(self, target): 
        damage = random.randint(self.level *2, self.level *4)
        target.receive_attack(damage)
        print(f"{self.name} atacou o 🎯 {target.name} e causou 💥 {damage} de dano") 

    
        