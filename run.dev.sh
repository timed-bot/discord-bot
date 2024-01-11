sudo docker rmi dev -f
sudo docker image prune -f
sudo docker container prune -f
sudo docker build -t dev .
sudo docker run dev