import requests
from elasticsearch import Elasticsearch

# Faire une requête GET à Elasticsearch
res = requests.get('http://localhost:9200?pretty')

# Afficher la réponse du serveur
print(res.content)

# Connexion à Elasticsearch
es = Elasticsearch('http://localhost:9200')

#create
es.indices.create(index="first_index",ignore=400)

#verify
print (es.indices.exists(index="first_index"))

#delete
print (es.indices.delete(index="first_index", ignore=[400,404]))
