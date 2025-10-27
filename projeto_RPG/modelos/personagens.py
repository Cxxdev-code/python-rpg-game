import random
import os


class Personagem:
    def __init__(self,nome, vida, nivel):
        self._nome = nome
        self._vida = vida
        self._nivel = nivel

    @property
    def nome(self):
        return self._nome

    @property
    def vida(self):
        return self._vida
    
    @vida.setter
    def vida(self,nova_vida):
        self._vida = nova_vida
    
    @property
    def nivel(self):
        return self._nivel
    
    
    def exibir_detalhes(self):
        return f"\nNome: {self.nome} \nVida:❤️  {self.vida} \nNivel:💎 {self.nivel}"
    

    def receber_ataque(self,dano):
        self.vida -= dano
        if self.vida <=0:
            self.vida = 0  
    
    def atacar(self,alvo):
        dano = random.randint(self.nivel *2, self.nivel *4)
        alvo.receber_ataque(dano)
        print(f"{self.nome} atacou o 🎯 {alvo.nome} e causou 💥 {dano} de dano")

    
    
class Heroi(Personagem):
    def __init__(self,nome, vida, nivel, habilidade):
        super().__init__(nome, vida, nivel)
        self._habilidade = habilidade

    @property
    def habilidade(self):
        return self._habilidade
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nHailidade:📚 {self.habilidade}"
    
    def ataque_especial(self,alvo):
        dano = random.randint(self.nivel * 5, self.nivel * 8)
        alvo.receber_ataque(dano)
        print(f"{self.nome} usou a habilildade especial 📚 {self.habilidade} em 🎯 {alvo.nome} e causou 💥 {dano} de dano")


class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel, tipo):
        super().__init__(nome, vida, nivel)
        self._tipo = tipo

    @property
    def tipo(self):
        return self._tipo
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\ntipo:🧬 {self.tipo}"
