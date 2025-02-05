from pymongo import MongoClient
import pymongo
import json

# Connexion à MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client.mydb
collection = db.mycollection

# Insertion d'un seul document
document = {"name": "John Doe", "email": "john.doe@example.com", "age": 30}
result = collection.insert_one(document)
print("Inserted document ID:", result.inserted_id)

# Insertion de plusieurs documents
documents = [
    {"name": "Alice", "email": "alice@example.com", "age": 25},
    {"name": "Bob", "email": "bob@example.com", "age": 35}
]
result = collection.insert_many(documents)
print("Inserted document IDs:", result.inserted_ids)

# Recherche d'un document spécifique
query = {"name": "John Doe"}
document = collection.find_one(query)
print("Found document:", document)

# Recherche de plusieurs documents avec une condition
query = {"age": {"$gt": 25}}  # Tous les documents où age > 25
documents = collection.find(query)
for doc in documents:
    print(doc)

# Mise à jour d'un document
document_query = {"name": "John Doe"}
update = {"$set": {"age": 31}}
result = collection.update_one(document_query, update)
print("Modified document count:", result.modified_count)

# Mise à jour de plusieurs documents
query = {"age": {"$gt": 25}}
update = {"$inc": {"age": 1}}  # Incrémente l'âge de 1
result = collection.update_many(query, update)
print("Modified document count:", result.modified_count)

# Suppression d'un document
query = {"name": "John Doe"}
result = collection.delete_one(query)
print("Deleted document count:", result.deleted_count)

# Suppression de plusieurs documents
query = {"age": {"$gt": 25}}
result = collection.delete_many(query)
print("Deleted document count:", result.deleted_count)

# Recherche avec une combinaison de conditions (AND)
query = {
    "$and": [
        {"age": {"$gt": 25}},
        {"email": {"$regex": "@example\\.com$"}}  # Email doit se terminer par @example.com
    ]
}
documents = collection.find(query)
for doc in documents:
    print(doc)

# Projection de champs spécifiques (exclut _id)
query = {"age": {"$gt": 25}}
projection = {"_id": 0, "name": 1, "email": 1}
documents = collection.find(query, projection)
for doc in documents:
    print(doc)

# Tri des documents par nom
query = {"age": {"$gt": 25}}
documents = collection.find(query).sort("name", pymongo.ASCENDING)
for doc in documents:
    print(doc)

# Chargement de données depuis un fichier JSON
with open("accounts.json", "r") as file:
    data = json.load(file)
result = collection.insert_many(data)
print("Inserted data with the following IDs:", result.inserted_ids)

# Création d'un index sur une ville dans l'adresse
index_name = "city_index"
collection.create_index("address.city", name=index_name)

# Recherche d'utilisateurs par ville
city = "Bradshawborough"
results = collection.find({"address.city": city})
for result in results:
    print(result)

# Recherche des utilisateurs avec un solde bancaire supérieur à un seuil
min_balance = 30000
results = collection.find({"balance": {"$gt": min_balance}})
for result in results:
    print(result)

# Agrégation : somme des soldes par ville
pipeline = [
    {"$group": {"_id": "$address.city", "total_balance": {"$sum": "$balance"}}},
    {"$sort": {"total_balance": -1}}  # Tri par total_balance décroissant
]
results = collection.aggregate(pipeline)
for result in results:
    print(f"{result['_id']}: {result['total_balance']}")

# Création d'un index unique sur l'email
collection.create_index("email", unique=True)

# Agrégation : comptage d'utilisateurs par âge pour ceux qui ont plus de 25 ans
pipeline = [
    {"$match": {"age": {"$gt": 25}}},
    {"$group": {"_id": "$age", "count": {"$sum": 1}}}
]
results = collection.aggregate(pipeline)
for result in results:
    print(result)
