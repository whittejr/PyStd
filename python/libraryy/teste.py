import requests
import sys

default_url = "https://itunes.apple.com/search?entity=song&limit=1&term="
url = sys.argv[1] if len(sys.argv) > 1 else default_url

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Erro ao buscar o arquivo JSON")