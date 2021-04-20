#! /bin/bash

echo "LOCALHOST TIME: "$(date -R)
start=$(date +%s)

command -v docker > /dev/null && echo "docker found" || { echo "docker not found"; exit 1; }
command -v docker-compose > /dev/null && echo "docker-compose found" || { echo "docker-compose not found"; exit 1; }

echo "------------clean remain env------------"
if [[ $(docker ps | grep mg_) != "" ]]; then
  docker-compose -p message_guest -f docker-compose.yml down
fi
if [[ $(docker images | grep mg_ | awk '{print $1}') != "" ]]; then
  docker image rm $(docker images | grep mg_ | awk '{print $1}')
fi

echo "------------build the web------------"
docker run -it --rm -v $(pwd)/../web:/web node:15.4.0-stretch bash -c "cd /web && yarn install && yarn versions && yarn build || cat /root/.npm/_logs/*.log" || { echo "web build fail"; exit 1; }

echo "------------copy the dist to nginx------------"
cp -r ../web/dist ../nginx

echo "------------build nginx------------"
docker build -t mg_nginx ../nginx

echo "------------build server------------"
docker build -t mg_server ../server

export HTTP_PORT='8000'
export MONGODB_ADDR='mongodb://mg_mongo:27017/guest_book'
export REDIS_ADDR='redis://mg_redis:6379/0'
docker-compose -p message_guest -f docker-compose.yml up -d

end=$(date +%s)
echo "TOTAL SPEND TIME: "$(expr $end - $start)" seconds"
