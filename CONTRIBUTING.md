# Contributing

## How to build and run docker file locally?

#### docker build -t tag-name .

#### docker run -dp 5000:5000 -w /app -v "$(pwd):/app" IMAGE_NAME sh -c "flask run"

#### docker run -p 5000:5000 flask-rest-api-queue-mail sh -c "flask run --host 0.0.0.0"
