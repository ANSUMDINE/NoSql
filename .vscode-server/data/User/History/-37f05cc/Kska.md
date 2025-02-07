# Ingérer des données CSV avec Logstash et Elasticsearch

Ce projet montre comment ingérer des données CSV à partir d'un répertoire local et les indexer dans Elasticsearch en utilisant Logstash. Nous utiliserons Docker et Docker Compose pour orchestrer les services nécessaires, notamment Elasticsearch, Logstash et Kibana.

## Architecture du projet

L'architecture du projet est la suivante :

```
elk_csv/
├── data
│   ├── data.csv
│   └── data-json.log
├── docker-compose.yml
├── elasticsearch
│   └── elasticsearch.yml
└── logstash
    ├── logstash.conf
    └── logstash.yml
```

- **data/data.csv** : Le fichier CSV contenant les données à ingérer.
- **data/data-json.log** : Le fichier JSON (facultatif) à ingérer (si vous souhaitez tester avec JSON).
- **docker-compose.yml** : Fichier Docker Compose pour orchestrer les services.
- **elasticsearch/elasticsearch.yml** : Configuration d'Elasticsearch.
- **logstash/logstash.conf** : Fichier de configuration de la pipeline Logstash pour ingérer les données.
- **logstash/logstash.yml** : Fichier de configuration de Logstash.

## Prérequis

- [Docker](https://www.docker.com/get-started) installé sur votre machine.
- [Docker Compose](https://docs.docker.com/compose/install/) installé pour gérer les services.

## Configuration

1. **Clonez ce projet** :

   Clonez ou téléchargez ce répertoire sur votre machine locale.

   ```bash
   git clone <URL de votre repo>
   cd elk_csv
   ```

2. **Configurer `docker-compose.yml`** :

   Ce fichier définit les services nécessaires : Elasticsearch, Logstash et Kibana. Il configure les volumes et les réseaux pour permettre une communication fluide entre les services.

   Exemple du fichier `docker-compose.yml` :

   ```yaml
   version: "3"
   services:
     elasticsearch:
       image: elasticsearch:7.6.2
       container_name: elasticsearch
       hostname: elasticsearch
       restart: always
       environment:
         - "discovery.type=single-node"
       ports:
         - 9200:9200
         - 9300:9300
       networks:
         - dockerelk
       volumes:
         - ./elasticsearch/elasticsearch.yml:/usr/share/elasticsearch/config/elasticsearch.yml

     logstash:
       image: logstash:7.6.2
       container_name: logstash
       hostname: logstash
       ports:
         - 9600:9600
         - 8089:8089
       restart: always
       links:
         - elasticsearch:elasticsearch
       depends_on:
         - elasticsearch
       networks:
         - dockerelk
       volumes:
         - ./logstash/logstash.yml:/usr/share/logstash/config/logstash.yml
         - ./logstash/logstash.conf:/usr/share/logstash/pipeline/logstash.conf
         - ./data/data.csv:/usr/share/logstash/external-data/data.csv

     kibana:
       image: kibana:7.6.2
       container_name: kibana
       environment:
         - ELASTICSEARCH_HOSTS=http://elasticsearch:9200
       ports:
         - "5601:5601"
       networks:
         - dockerelk
       depends_on:
         - elasticsearch

   networks:
     dockerelk:
       driver: bridge
   ```

3. **Configurer Elasticsearch** :

   Le fichier `elasticsearch.yml` configure votre instance Elasticsearch pour une utilisation avec un seul nœud. Vous pouvez personnaliser les paramètres selon vos besoins.

   Exemple de configuration pour `elasticsearch.yml` :

   ```yaml
   cluster.name: docker-cluster
   node.name: docker-node
   node.master: true
   network.host: 0.0.0.0
   ```

4. **Configurer Logstash** :

   Le fichier `logstash.conf` définit la pipeline de Logstash pour ingérer les données CSV. Logstash lira le fichier CSV, le filtrera et les indexera dans Elasticsearch.

   Exemple de configuration pour `logstash.conf` :

   ```plaintext
   input {
     file {
       path => "/usr/share/logstash/external-data/data.csv"
       start_position => "beginning"
       sincedb_path => "/dev/null"
     }
   }

   filter {
     csv {
       separator => ","
       columns => ["order_id", "order_date", "customer_name", "product_name", "quantity", "price"]
     }

     date {
       match => ["order_date", "yyyy-MM-dd"]
       target => "order_date"
     }
   }

   output {
     elasticsearch {
       hosts => ["elasticsearch:9200"]
       index => "orders-%{+YYYY.MM.dd}"
     }
   }
   ```

5. **Configurer Logstash Monitoring** :

   Le fichier `logstash.yml` est utilisé pour configurer la surveillance de Logstash. Voici un exemple :

   ```yaml
   xpack.monitoring.elasticsearch.hosts: [ "http://elasticsearch:9200" ]
   ```

6. **Lancer les services Docker** :

   Exécutez la commande suivante pour démarrer Elasticsearch, Logstash et Kibana avec Docker Compose.

   ```bash
   docker-compose up
   ```

   Cette commande téléchargera les images nécessaires et lancera les services dans des conteneurs Docker.

7. **Vérifier les données dans Kibana** :

   Accédez à Kibana à l'adresse suivante dans votre navigateur : [http://localhost:5601](http://localhost:5601). Vous pouvez maintenant explorer les données indexées dans Elasticsearch.

   Si vous préférez interroger Elasticsearch directement via la ligne de commande, vous pouvez utiliser `curl` :

   ```bash
   curl -X GET "localhost:9200/orders-*/_search?pretty"
   ```

8. **Valider la configuration de Logstash** :

   Avant d'exécuter Logstash, vous pouvez valider la configuration avec la commande suivante :

   ```bash
   docker-compose exec logstash bin/logstash --config.test_and_exit -f /usr/share/logstash/pipeline/logstash.conf
   ```

   Si la configuration est correcte, vous verrez un message `Configuration OK`.

## Modification du format des données (JSON)

Si vous souhaitez tester l'ingestion de données au format JSON, vous pouvez adapter le fichier `logstash.conf` en modifiant l'entrée et le filtre comme suit :

Exemple de configuration pour un fichier JSON :

```yaml
input {
  file {
    path => "/usr/share/logstash/external-data/data-json.log"
    start_position => "beginning"
    sincedb_path => "/dev/null"
  }
}

filter {
  json {
    source => "message"
  }
}

output {
  elasticsearch {
    hosts => "elasticsearch:9200"
    index => "json-data"
  }
  stdout{}
}
```

Ensuite, ajoutez le fichier JSON à `docker-compose.yml` en tant que volume :

```yaml
logstash:
  ...
  volumes:
    - ./data/data-json.log:/usr/share/logstash/external-data/data-json.log
```

## Conclusion

Ce projet montre comment configurer une pipeline simple avec Logstash pour ingérer des données CSV (ou JSON) dans Elasticsearch, et comment visualiser ces données via Kibana. En utilisant Docker et Docker Compose, la mise en place est rapide et vous pouvez facilement adapter cette configuration à d'autres formats de données.
