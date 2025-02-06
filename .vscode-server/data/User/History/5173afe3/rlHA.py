import requests

# Faire une requête GET à Elasticsearch
res = requests.get('http://localhost:9200?pretty')

# Afficher la réponse du serveur
print(res.content)
