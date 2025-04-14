# ---- GLOBALS ----
COMPOSE = docker compose -f docker-compose.yml

# ---- PHONY ----
.PHONY: build build-etl run-core run-rdg run-etl up up-etl up-core down logs logs-etl clean

# ---- BUILD ----

# Build all images
build:
	$(COMPOSE) build

# Build only ETL workers
build-etl:
	$(COMPOSE) build worker_etl_1 worker_etl_2 worker_etl_3

# ---- RUN ----

# Start only the core infrastructure (Kafka, Zookeeper, DB, Spark Master)
run-core:
	$(COMPOSE) up -d kafka zookeeper final_storage_db spark-master

# Start the random data generator (after core is up)
run-rdg:
	$(COMPOSE) up -d random_data_generator


# Start the single ETL worker app
run-etl:
	$(COMPOSE) up -d worker_etl

# Start the workers 
scale-workers:
	$(COMPOSE) up -d --scale spark-worker=$(n)

# Full pipeline startup: build everything and run all services
up:
	$(COMPOSE) up --build -d

# Start only ETL workers (without rebuilding)
up-etl:
	$(COMPOSE) up -d worker_etl_1 worker_etl_2 worker_etl_3

# Start only core infrastructure (without rebuilding)
up-core:
	$(COMPOSE) up -d kafka zookeeper final_storage_db spark-master

# ---- LOGS ----

# Logs for entire pipeline
logs:
	$(COMPOSE) logs -f

# Logs for only ETL workers
logs-etl:
	$(COMPOSE) logs -f worker_etl_1 worker_etl_2 worker_etl_3

# ---- SHUTDOWN / CLEAN ----

# Bring everything down
down:
	$(COMPOSE) down -v --remove-orphans

# Remove all unused containers, networks, images, etc.
clean:
	docker system prune -f