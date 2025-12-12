class Item:
    def __init__(self, nome: str, tipo: str, dano: int = 0):
        self._nome = nome        
        self._tipo = tipo        
        self._dano = dano        

    @property
    def nome(self):
        return self._nome

    @property
    def tipo(self):
        return self._tipo

    @property
    def dano(self):
        return self._dano

    def show_details(self):
        texto = f"\nItem: ⚔️  {self._nome}\nTipo: 🔧  {self._tipo}\nDano: 💥  {self._dano}\n"
        return texto

    def to_dict(self):
        return {
            "nome": self._nome,
            "tipo": self._tipo,
            "dano": self._dano
        }
