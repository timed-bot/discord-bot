docker rmi dev -f
docker image prune -f
docker container prune -f
docker build -t dev .
docker run dev