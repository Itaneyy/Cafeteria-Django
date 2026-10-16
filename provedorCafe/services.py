# services.py
import requests

def buscar_cafes_da_api():
    url = "https://api.sampleapis.com/coffee/hot"
    
    try:
        response = requests.get(url)
        
        # Verifica se a requisição deu certo (Status 200)
        if response.status_code == 200:
            return response.json() # Retorna a lista de cafés em formato de dicionário Python (JSON)
        else:
            return [] # Retorna lista vazia se der erro na API
            
    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão com a API: {e}")
        return []