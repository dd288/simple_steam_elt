docker-spin-up:
	docker compose --env-file env up --build -d

sleeper:
	sleep 20

up: docker-spin-up sleeper warehouse-migration

down:
	docker compose --env-file env down

shell: 
	docker exec -ti pipeline bash

format:
	docker exec pipeline python -m black -S --line-lenght 79 .

isort:
	docker exec pipeline isort .

type:
	docker exec pipeline mypy --ignore-missing-imports /code

lint:
	docker exec pipeline flake8 /code

ci:
	isort format type lint

stop-etl:
	docker exec pipeline service cron stop

################################################
# Database Migration

db-migration:
	@read -p "Enter migration name:" migration_name; docker exec pipeline yoyo new ./migrations -m "$$migration_name"

warehouse-migration:
	docker exec pipeline yoyo develop --no-config-file --database postgres://giannis:#lata1996prr@warehouse:5432/steam_warehouse ./migrations

warehouse-rollback:
	docker exec pipelinerunner yoyo rollback --no-config-file --database postgres://giannis:#lata1996prr@warehouse:5432/steam_warehouse ./migrations

################################################


