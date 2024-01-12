FROM python:3.11-alpine as dev
WORKDIR /src
RUN apk add --no-cache gcc musl-dev linux-headers
COPY . .
RUN pip install pipenv
RUN pipenv install --ignore-pipfile
# RUN pipenv requirements > requirements.txt
# RUN pip install -r requirements.txt
CMD ["pipenv", "run", "python", "./src/start.py", "dev"]