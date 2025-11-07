from models.character import Character

class Enemy(Character): 
    def __init__(self, name, health, level, kind): 
        super().__init__(name, health, level)
        self._kind = kind 

    @property
    def kind(self):
        return self._kind
    
    def show_details(self): 
        return f"{super().show_details()}\ntipo:🧬 {self.kind}" 