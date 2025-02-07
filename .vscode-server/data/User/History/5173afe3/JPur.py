import requests
from elasticsearch import Elasticsearch

# Faire une requête GET à Elasticsearch
res = requests.get('http://localhost:9200?pretty')
# Afficher la réponse du serveur
print(res.content)

# Connexion à Elasticsearch
es = Elasticsearch('http://localhost:9200')

# Créer un index si il n'existe pas
try:
    es.indices.create(index="first_index", ignore=400)
except Exception as e:
    print(f"Erreur lors de la création de l'index : {e}")

# Vérifier si l'index existe
exists = es.indices.exists(index="first_index")
print(f"L'index existe ? {exists}")

# Supprimer l'index s'il existe
try:
    response = es.indices.delete(index="first_index", ignore=[400, 404])
    print(f"Réponse après suppression : {response}")
except Exception as e:
    print(f"Erreur lors de la suppression de l'index : {e}")
