from models.character import Character
import random

class Hero(Character): 
    def __init__(self, name, health, level, skill, mana):
        super().__init__(name, health, level)
        self._skill = skill 
        self._mana = mana

    @property
    def skill(self): 
        return self._skill
    
    
    def show_details(self):
        return f"{super().show_details()}\nHailidade:📚 {self.skill}\nMana: {self._mana}"
    
   
    def special_attack(self, target):
        abilityValue = 30

        if self._mana >= abilityValue:
            damage = random.randint(self.level * 5, self.level * 8)
            target.receive_attack(damage)
            self._mana -= 30

            print(f"{self.name} usou a habilildade especial 📚 {self.skill} em 🎯 {target.name} e causou 💥 {damage} de dano") 
        else:
            print("Mana insuficiente!")

    def up_level(self):
        self._level += 1
