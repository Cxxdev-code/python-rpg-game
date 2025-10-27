from modelos.personagens import Heroi, Inimigo

class jogo:
    def __init__(self):
        self.heroi = Heroi(nome = "Heroi",vida = 100,nivel =  5,habilidade= "bola de fogo") 
        self.inimigo = Inimigo(nome = "Dragão", vida = 100, nivel= 5, tipo= "voador")
    


    def iniciar_batalha(self):
        print("iniciando batalha!")
        while self.heroi.vida > 0 and self.inimigo.vida >0:
            print("detlahes do combate")
            print(self.heroi.exibir_detalhes())
            print(self.inimigo.exibir_detalhes())
            print("Pressione [enter] para atacar......")
            opc = (int(input("[1] para ataque normal---[2] para ataque especial: ")))
            
            if opc == 1:
                self.heroi.atacar(self.inimigo)
            elif opc == 2:
                self.heroi.ataque_especial(self.inimigo)
            else:
                print("ataque invalido")
            
            

            if self.inimigo.vida > 0:
                self.inimigo.atacar(self.heroi)
            
            
            input("\n[Resultado do Turno Acima] Pressione [Enter] para o próximo turno...")
                

        if self.heroi.vida > 0:
            print("Parabens voce ganhou")
        else:
            print("voce foi derrotado")


if __name__ == "__main__":
    gerenciador = jogo()
    gerenciador.iniciar_batalha()