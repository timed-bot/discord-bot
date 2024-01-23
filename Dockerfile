FROM python:3.11-alpine as dev
WORKDIR /src
RUN apk add --no-cache gcc musl-dev linux-headers
COPY . .
RUN pip install pipenv
RUN pipenv install --ignore-pipfile
# RUN pipenv requirements > requirements.txt
# RUN pip install -r requirements.txt
CMD ["pipenv", "run", "python", "./src/start.py", "dev"]

FROM redis:latest as redis-dev
# Copy your custom configuration file into the container
# COPY redis.conf /usr/local/etc/redis/redis.conf
# Expose the Redis port (default is 6379)
EXPOSE 6379
# Start Redis with the custom configuration file
# CMD ["redis-server", "/usr/local/etc/redis/redis.conf"]
CMD ["redis-server"]