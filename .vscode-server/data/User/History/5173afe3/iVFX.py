import requests
from elasticsearch import Elasticsearch

# Faire une requête GET à Elasticsearch
res = requests.get('http://localhost:9200?pretty')

# Afficher la réponse du serveur
print(res.content)

# Connexion à Elasticsearch
es = Elasticsearch('http://localhost:9200')

