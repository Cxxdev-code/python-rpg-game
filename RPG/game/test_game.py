from models.items import Item
import random
if __name__ == '__main__':
    armas =[ 
        {"nome": "Espada Curta", "tipo": "corpo a corpo", "dano": "1d6" },
        {"nome": "Espada Longa", "tipo": "corpo a corpo", "dano": "1d8" },
        { "nome": "Katana", "tipo": "corpo a corpo", "dano": "1d10" },
        { "nome": "Machado de Batalha", "tipo": "corpo a corpo", "dano": "1d8" },
        { "nome": "Maça", "tipo": "corpo a corpo", "dano": "1d8" },
        { "nome": "Lança", "tipo": "haste / perfurante", "dano": "1d6" },]
    dados_arma = random.choice((armas))

    item = Item( nome = dados_arma["nome"], tipo = dados_arma["tipo"], dano= dados_arma["dano"])

    
    

    print()
    #dicionario = {"nome": dados_arma["nome"], "tipo": dados_arma["tipo"], "dano": dados_arma["dano"]}
    ##print(item)