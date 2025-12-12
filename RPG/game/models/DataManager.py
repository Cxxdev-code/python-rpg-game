import json
import os

class DataManager:
    def __init__(self, file_path):
       
        self._FILE_PATH = file_path

    def save_game(self, data):
       
        os.makedirs(os.path.dirname(self._FILE_PATH), exist_ok=True)

        
        with open(self._FILE_PATH, "w", encoding="utf-8") as file:
           
            json.dump(data, file, indent=4, ensure_ascii=False)

    def Load_Game(self):
        
        if not os.path.exists(self._FILE_PATH):
            print("⚠️ Nenhum save encontrado. Criando novo jogo...")
            return None
        
        try:
            
            with open(self._FILE_PATH, "r", encoding="utf-8") as file:
                data = json.load(file)

            required_fields = ["Nome", "Vida", "Nivel", "Mana", "Habilidade"]
            for field in required_fields:
                if field not in data:
                    print(f"⚠️ Campo ausente no save: {field}.")
                    return None

            print("💾 Save carregado com sucesso!")
            return data

        except json.JSONDecodeError:
            print("❌ Erro ao ler o arquivo de save (JSON corrompido).")
            return None

        except Exception as error:
            print(f"❌ Erro inesperado ao carregar o jogo: {error}")
            return None