from models.character import Character
import random

class Hero(Character): 
    def __init__(self, name, health, level, skill, mana, arma = None):
        super().__init__(name, health, level)
        self._skill = skill 
        self._mana = mana
        self._arma = arma

    @property
    def mana(self): 
        return self._mana
    

    @mana.setter
    def mana(self, mana):
        self._mana = mana
    

    @property
    def skill(self): 
        return self._skill
    

    @property
    def arma(self):
        return self._arma
    

    @arma.setter
    def arma(self, item):
        self._arma = item


    def attack(self, target):
    
     dano_base = random.randint(self.level * 2, self.level * 4)
    
     dano_arma = self._arma.dano if self._arma else 0

     damage = dano_base + dano_arma

     target.receive_attack(damage)

     print(f"{self.name} atacou 🎯 {target.name} causando 💥 {dano_base} de dano")

     if self._arma:
         print(f"   ➕ A arma {self._arma.nome} adicionou {dano_arma} de dano | Total: {damage}")

    
    def show_details(self):
     detalhes_base = super().show_details()

     if self._arma:
         arma_texto = f"Arma equipada: 🗡️  {self._arma.nome} (Dano: {self._arma.dano})"
     else:
         arma_texto = "Arma equipada: ❌ Nenhuma"

     return (
         f"{detalhes_base}"
         f"\nHabilidade:📚 {self.skill}"
         f"\nMana:🔵 {self._mana}"
         f"\n{arma_texto}"
     )
    
   
    def special_attack(self, target):
        valor_habilidade = 30

        if self._mana >= valor_habilidade:
            damage = random.randint(self.level * 5, self.level * 8)
            target.receive_attack(damage)
            self._mana -= 30

            print(f"{self.name} usou a habilildade especial 📚 {self.skill} em 🎯 {target.name} e causou 💥 {damage} de dano") 
        else:
            print("Mana insuficiente!")


    def up_level(self):
        self._level += 1


    def to_dict (self):
        return {
            "Nome": self.name,
            "Vida": self.health,
            "Nivel": self.level,
            "Mana": self.mana,
            "Habilidade": self.skill,
            "Arma": self.arma.to_dict() if self.arma else "desarmado",
        }
