docker-compose stop bot-dev 
docker-compose rm -f -s -v
docker-compose build bot-dev --no-cache 
docker image prune -f
docker-compose up bot-dev -d