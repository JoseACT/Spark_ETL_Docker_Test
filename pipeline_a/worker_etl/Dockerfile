FROM bitnami/spark:latest

WORKDIR /app
COPY . /app/

CMD ["/opt/bitnami/spark/bin/spark-submit", "/app/main.py"]
