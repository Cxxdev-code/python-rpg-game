from models.character import Character
import random

class Hero(Character):
    def __init__(self, name, health, level, skill, mana, weapon=None):
        super().__init__(name, health, level)
        self._skill = skill
        self._mana = mana
        self._weapon = weapon


    @property
    def mana(self):
        return self._mana


    @mana.setter
    def mana(self, value):
        self._mana = value


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

    @property
    def weapon(self):
        return self._weapon


    @weapon.setter
    def weapon(self, item):
        self._weapon = item


    def up_level(self):
        self._level += 1
        
        
    def attack(self, target):
        base_damage = random.randint(self.level * 2, self.level * 4)
        weapon_damage = self._weapon.dano if self._weapon else 0
        total_damage = base_damage + weapon_damage


        target.receive_attack(total_damage)


        print(f"{self.name} atacou 🎯 {target.name} causando 💥 {base_damage} de dano")


        if self._weapon:
            print(f" ➕ A arma {self._weapon.nome} adicionou {weapon_damage} de dano | Total: {total_damage}")


        
    def show_details(self):
        base_text = super().show_details()
        if self._weapon:
            weapon_text = f"Arma equipada: 🗡️ {self._weapon.nome} (Dano: {self._weapon.dano})"
        else:
            weapon_text = "Arma equipada: ❌ Nenhuma"

        return (
        f"{base_text}\n"
        f"Habilidade:📚 {self.skill}\n"
        f"Mana:🔵 {self._mana}\n"
        f"{weapon_text}"
        )
    
    def special_attack(self, target):
        mana_cost = 30

        if self._mana >= mana_cost:
            damage = random.randint(self.level * 5, self.level * 8)
            target.receive_attack(damage)
            
            self._mana -= mana_cost
            print(f"{self.name} usou a habilildade especial 📚 {self.skill} em 🎯 {target.name} e causou 💥 {damage} de dano")
            
        else:
            print("Mana insuficiente!")


    


    def to_dict(self):
        return {
        "Nome": self.name,
        "Vida": self.health,
        "Nivel": self.level,
        "Mana": self.mana,
        "Habilidade": self.skill,
        "Arma": self.weapon.to_dict() if self.weapon else "desarmado",
        }
        