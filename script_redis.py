import redis
from redis import ConnectionPool
# connexion avec le serveur redis
r = redis.Redis(host='localhost', port=6379, db=0)

# ajoutons quelques regles
r.set('user:1:name', 'John Doe')
r.set('user:1:email', 'john.doe@example.com')
# Ajoutons une clé avec un délai d’expiration (en secondes)
r.setex('session_key', 3600, 'session_data')
# Pour récupérer la valeur associée à une clé, utilisez la méthode get :
user_name = r.get('user:1:name')
user_email = r.get('user:1:email')
#La méthode get renvoie la valeur sous forme d’octets. Pour le convertir en chaîne, utilisez la méthode decode :
user_name = user_name.decode('utf-8')
user_email = user_email.decode('utf-8')
# Si vous souhaitez récupérer plusieurs clés à la fois, utilisez la méthode mget :
keys = ['user:1:name', 'user:1:email']
values = r.mget(keys)
# Convert byte values to strings
values = [value.decode('utf-8') for value in values]
