import requests
from elasticsearch import Elasticsearch

# Faire une requête GET à Elasticsearch
res = requests.get('http://localhost:9200?pretty')

# Afficher la réponse du serveur
print(res.content)

# Connexion à Elasticsearch
es = Elasticsearch('http://localhost:9200')

# Créer un index avec des options
es.options(ignore_status=[400]).indices.create(index="first_index")

# Vérifier l'existence de l'index
print(es.indices.exists(index="first_index"))

# Supprimer l'index avec des options
print(es.options(ignore_status=[400, 404]).indices.delete(index="first_index"))