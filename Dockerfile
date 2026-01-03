FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Cloud Run expects the container to listen on PORT, but for a worker/bot 
# we mainly need it not to crash. However, standard Cloud Run requires an HTTP server.
# For simply running the bot, we can use a worker pattern or a simple healthcheck server.
# Here we just run the main script.
CMD ["python", "main.py"]
