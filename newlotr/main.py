import requests
import random

API_KEY = "EpJZYL8_QwFZ05RCFL_j"

headers = {
    "Authorization": f"Bearer {API_KEY}"
}

name = "Bilbo Baggins"
id = ""

# Chamo a API para retornar o ID a partir do nome do personagem #
response = requests.get(f"https://the-one-api.dev/v2/character/", headers=headers)
characters = response.json()["docs"]

for char in characters:
    if char["name"] == name:
        id = char["_id"]

# Com o ID, chamo a api para colocar os quotes em uma lista #
quote_response = requests.get(f"https://the-one-api.dev/v2/character/{id}/quote", headers=headers)
quotes_list = quote_response.json()["docs"]
quotes_select_list = []
for quotes in quotes_list:
    quotes_select_list.append(quotes["dialog"])

# Seleciona aleatoriamente um quote do personagem #
print(f"{name}: {random.choice(quotes_select_list)}")
