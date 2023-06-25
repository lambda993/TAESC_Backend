docker-build:
	docker rmi -f taesc_backend
	docker build -t taesc_backend .

docker-start:
	docker compose up

docker-stop:
	docker compose down

docker-shell:
	docker compose run taesc /bin/bash
