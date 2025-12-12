import json
import os
class DataManager:
    def __init__(self, caminho_arquivo):
        self._CAMINHO_ARQUIVO = caminho_arquivo

    def Save_Game(self, dados):

        os.makedirs(os.path.dirname(self._CAMINHO_ARQUIVO), exist_ok=True)

        with open(self._CAMINHO_ARQUIVO, "w", encoding="utf-8") as file:
            json.dump(dados, file, indent=4, ensure_ascii=False)

    def Load_Game(self):

        if not os.path.exists(self._CAMINHO_ARQUIVO):
            print("⚠️ Nenhum save encontrado. Criando novo jogo...")
            return None
        
        try:
            # 2️⃣ Abre e carrega o JSON
            with open(self._CAMINHO_ARQUIVO, "r", encoding="utf-8") as file:
                dados = json.load(file)

            campos_obrigatorios = ["Nome", "Vida", "Nivel", "Mana", "Habilidade"]
            for campo in campos_obrigatorios:
                if campo not in dados:
                    print(f"⚠️ Campo ausente no save: {campo}.")
                    return None

            print("💾 Save carregado com sucesso!")
            return dados

        except json.JSONDecodeError:
            print("❌ Erro ao ler o arquivo de save (JSON corrompido).")
            return None

        except Exception as erro:
            print(f"❌ Erro inesperado ao carregar o jogo: {erro}")
            return None
