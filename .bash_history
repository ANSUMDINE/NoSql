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
