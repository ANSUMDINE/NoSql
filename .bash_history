sudo apt update
sudo apt install -y docker.io
sudo systemctl enable --now docker
sudo usermod -aG docker $USER
newgrp docker
docker run hello-world
docker run hello-world
docker pull docker.elastic.co/elasticsearch/elasticsearch:7.11.1
docker run -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.11.1
docker-compose up -d
nano docker-compose.yml
docker-compose up -d
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose --version
docker compose up -d
docker-compose --version
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose --version
ls -l /usr/local/bin/docker-compose
docker-compose --version
docker pull docker.elastic.co/elasticsearch/elasticsearch:7.11.1
docker run -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.11.1
docker-compose up -d
pip install elasticsearch
sudo apt install python3-pip
pip install requests elasticsearch
python3 -m venv myenv
sudo apt install python3.12-venv
python3 -m venv myenv
source myenv/bin/activate
pip install requests elasticsearch
mkdir project_nosql
cd project_nosql
python test_es.py
curl http://localhost:9200
pip install --upgrade elasticsearch
curl http://localhost:9200
python test_es.py
docker ps
pip show elasticsearch
pip install elasticsearch==7.11.1
python test_es.py
pip install --upgrade elasticsearch
python test_es.py
import elasticsearch
print(elasticsearch.__version__)

pip show elasticsearch
pip uninstall elasticsearch
pip install elasticsearch==7.11.1
pip install elasticsearch
docker run -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:8.17.1
docker pull docker.elastic.co/elasticsearch/elasticsearch:8.17.1
docker run -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:8.17.1
pip show elasticsearch
sudo netstat -tuln | grep 9300
sudo lsof -i :9300
sudo kill 10623
docker run -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:8.17.1
docker run -p 9200:9200 -p 9301:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:8.17.1
python test_es.py
docker ps
docker stop 533637902c8d
docker run -p 9200:9200 -p 9301:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:8.17.1
python test_es.py
docker run -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:8.17.1
python test_es.py
docker stop $(docker ps -q)
docker rm $(docker ps -a -q)
docker rmi $(docker images -q)
docker-compose up -d
docker pull docker.elastic.co/elasticsearch/elasticsearch:8.17.1
docker run -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:8.17.1
docker-compose down

docker-compose up -d
python test_es.py
pip show elasticsearch
docker stop $(docker ps -q)
docker rm $(docker ps -a -q)

docker-compose down
docker run -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:8.17.1
docker-compose up -d
docker-compose down
docker pull docker.elastic.co/elasticsearch/elasticsearch:8.17.1
docker run -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:8.17.1
docker-compose up -d
python test_es.py
docker ps
docker logs 9e560c664768
docker-compose up -d
git init
git add .
git init
git add .
git commit -m "commit"
git remote add origin https://github.com/ANSUMDINE/NoSql.git 

git push -u origin main
git branch
git init
git remote origin https://github.com/ANSUMDINE/NoSql.git
git remote add origin https://github.com/ANSUMDINE/NoSql.git
git add .
git commit -m "message"
git config --global user.name "ANSUMDINE"
git config --global user.email "ansumdinesaidcombo@gmail.com"
git config --list
git commit -m "message"
git push origin main
git push origin master
cd ..
mkdir elk-csv && cd elk-csv
mkdir elk-csv
mkdir ~/elk-csv
cd elk-csv
ls
sudo cd elk-csv
sudo cd / elk-csv
source myenv/bin/activate
mkdir elk_csv
cd elk_csv
cd ..
desactive
deactivate
source myenv/bin/activate
cd project_nosql
git init
git add .
git commit -m " docker "
git push origin main
git push origin master
cd ..
mkdir elk_csv
cd elk_csv
pip show  elasticshow
pip show  elasticsearch
pip install elasticsearch==8.17.1
pip install elasticsearch==7.6.2
mkdir elasticsearch && cd elasticsearch
touch elasticsearch
cd ..
mkdir logstash && cd logstash
touch logstash.conf
bin/logstash --config.test_and_exit -f /path/to/your/logstash.conf
bin/logstash --config.test_and_exit -f /elk_csv/logstash/logstash.conf
pwd
/home/said/elk_csv/logstash --config.test_and_exit -f /elk_csv/logstash/logstash.conf
cd ..
docker-compose exec logstash /home/said/elk_csv/logstash --config.test_and_exit -f /usr/share/logstash/pipeline/logstash.conf
readlink -f elk_csv/logstash/logstash.conf
docker-compose exec logstash /home/said/elk_csv/logstash --config.test_and_exit -f /usr/share/logstash/pipeline/logstash.conf
docker-compose exec logstash ls -lah /usr/share/logstash/pipeline/
ls -lah logstash/logstash.conf
docker-compose down && docker-compose up -d
wget https://gist.githubusercontent.com/bdallard/d4a3e247e8a739a329fd518c0860f8a8/raw/82fb43adc5ce022797a5df21eb06dd8e755145ea/data-json.csv
wget https://gist.githubusercontent.com/bdallard/d4a3e247e8a739a329fd518c0860f8a8/raw/82fb43adc5ce022797a5df21eb06dd8e755145ea/data.csv
docker-compose down && docker-compose up -d
docker-compose up -d
ls
ls -lah logstash/logstash.conf
docker-compose exec logstash ls -lah /usr/share/logstash/pipeline/
logstash ls -lah
docker-compose exec logstash ls -lah /usr/share/logstash/pipeline/
docker-compose exec logstash bin/logstash --config.test_and_exit -f /usr/share/logstash/pipeline/logstash.conf
docker-compose exec logstash ls -l /usr/share/logstash/pipeline/
docker-compose exec logstash /bin/bash
docker-compose ps
docker logs logstash
docker ps -a
docker-compose up logstash
docker-compose up -d
docker-compose logs logstash
docker-compose up --build -d logstash
docker-compose exec logstash ls -l /usr/share/logstash/pipeline/
git init
git add .
git commit -m " message"
git push origin master
git push -u origin master
git remote -v
git remote add origin https://github.com/ANSUMDINE/NoSql.git
git push -u origin main
git push -u origin master
cd ..
git init
git add .
cd elk_csv
git push -u origin master
cd ..
git init 
git add elk_csv
git commit -m "message"
git push origin master
git push -u origin master
git remote -v
git remote add origin https://github.com/ANSUMDINE/NoSql.git
git push -u origin master
git pull origin master
git config pull.rebase false
git pull origin master
git add elk_csv
git commit
git status
git add .vscode-server/data/logs/20250206T121518/exthost1/vscode.git/Git.log
git commit -m "Votre message de commit"
git push -u origin master
deactivate
python /home/said/.vscode-server/extensions/ms-python.python-2024.22.2-linux-x64/python_files/printEnvVariablesToFile.py /home/said/.vscode-server/extensions/ms-python.python-2024.22.2-linux-x64/python_files/deactivate/bash/envVars.txt
/home/said/myenv/bin/python /home/said/elk_stack/send_logs.py
cd elk_stack
/home/said/myenv/bin/python /home/said/elk_stack/send_logs.py
docker-compose up up -d kibana
cd elk_csv
docker-compose up up -d kibana
docker-compose up -d
docker-compose exec logstash bin/logstash --config.test_and_exit -f /usr/share/logstash/pipeline/logstash.conf
bin/logstash --config.test_and_exit -f /path/to/your/logstash.conf
docker exec -it logstash /bin/bash
docker ps
docker-compose up -d
docker ps -a
docker rm -f elasticsearch
docker-compose up -d
docker ps -a
docker stop b759cad9afed90d30abed63c165e91263d8fc4b1a99c54a1fae0157030d464e4
docker rm b759cad9afed90d30abed63c165e91263d8fc4b1a99c54a1fae0157030d464e4
docker-compose up -d
docker-compose exec logstash bin/logstash --config.test_and_exit -f /usr/share/logstash/pipeline/logstash.conf
curl -X GET "0.0.0.0:9200/csv-data/_search?q=*" | jq
sudo apt update && sudo apt install -y jq
curl -X GET "0.0.0.0:9200/csv-data/_search?q=*" | jq
git add .
git commit -m " new"
git push -u origin master
cd ..
mkdir pipeline_ingestion
cd pipeline_ingestion
mkdir data
cd data
touch apache_logs.txt
cd ..
mkdir docker-compose.yml
touch docker-compose.yml
mkdir logstash
cd logstash
touch logstash.conf
cd ..
docker-compose down
docker-compose up -d
docker ps -a
docker stop 65dda65a0ee91eb29ae1ce11e2b2aade0c708a82ad857a66e04838d681efc360
docker rm 65dda65a0ee91eb29ae1ce11e2b2aade0c708a82ad857a66e04838d681efc360
docker-compose up -d
docker stop 51a57e4e9e83211906d29aaa17851ae817c3b79520792359093a4033dea66021
docker rm 51a57e4e9e83211906d29aaa17851ae817c3b79520792359093a4033dea66021
docker-compose up -d
docker stop ca9a5e54ac4baac31525c7b6af0ce06fb2c9abc4bd0be1d26595e5712f0726db
docker rm ca9a5e54ac4baac31525c7b6af0ce06fb2c9abc4bd0be1d26595e5712f0726db
docker-compose up -d
docker-compose down
docker-compose up -d
docker-compose down
docker-compose up -d
docker ps -a
docker rm -f 897fe4b8d75c
docker rm -f 8e9e9c0485c1
docker ps -a
docker rm -f d1612d65fd0e
docker-compose up -d
docker ps -a
docker-compose down
docker-compose up -d
docker-compose down
docker-compose up -d
docker ps 
clear
docker compose down -v
docker compose down 
docker-compose down -d
docker-compose down -v
docker-compose up -d
docker-compose down -v
docker-compose up -d
docker ps
cd ..
mkdir elk-stack && cd elk-stack
mkdir filebat && cd filebat
touch filebeat.yml
cd ..
mkdir logs && cd logs
touch  python_logs.log
cd ..
mkdir logstash && cd logstash
touch logstash.conf
cd ..
touch send_logs.py
python send_logs.py
clear
python send_logs.py
ls
clear
ls
cd ..
ls
cd elk_stack
ls
python send_logs.py
clea
cd elk_stack
docker-compose ps
docker-compose down -v
docker-compose up -d
cd ..
git commit -m "message"
git push -u origin master
clear
mkdir elastic && cd elastic
git clone https://github.com/Yankhoba92/elasticsearch
cd ..
git clone https://github.com/Yankhoba92/elasticsearch
mkdir elastic && cd elastic
deactived
mkdir elastic && cd elastic
