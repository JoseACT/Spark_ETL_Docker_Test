# ---- GLOBALS ----
COMPOSE = docker-compose -f dockercompose/docker-compose.yml

# ---- BUILD ----
build:
	$(COMPOSE) build

# builds the ETL workers only
build-etl:
	$(COMPOSE) build worker_etl_1 worker_etl_2 worker_etl_3

# ---- RUN ----
# runs the entire pipeline
up:
	$(COMPOSE) up --build -d
# runs the ETL workers only
up-etl:
	$(COMPOSE) up -d worker_etl_1 worker_etl_2 worker_etl_3

# runs the infrastructure only (kafka, zookeeper, final_storage_db, spark-master)
up-core:
	$(COMPOSE) up -d kafka zookeeper final_storage_db spark-master

# shuts down the entire pipeline
down:
	$(COMPOSE) down -v --remove-orphans

# shows the logs of the entire pipeline
logs:
	$(COMPOSE) logs -f

# shows the logs of the ETL workers only
logs-etl:
	$(COMPOSE) logs -f worker_etl_1 worker_etl_2 worker_etl_3

# ---- CLEAN ----
clean:
	docker system prune -af --volumes

