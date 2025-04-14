FROM bitnami/spark:latest

# Set working directory
WORKDIR /app

# Copy Python code and requirements
COPY . /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run commands
CMD ["/opt/bitnami/spark/bin/spark-submit", \
     "--packages", \
     "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0,org.postgresql:postgresql:42.7.2", \
     "/app/main.py"]
