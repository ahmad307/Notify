.PHONY: makemigrations
makemigrations:
	docker compose -f api/docker/local.yaml run --rm api python3 manage.py makemigrations

.PHONY: migrate
migrate:
	docker compose -f api/docker/local.yaml run --rm api python3 manage.py migrate

.PHONY: runproject
runproject:
	docker compose -f api/docker/local.yaml up

.PHONY: runproject-detached
runproject-detached:
	docker compose -f api/docker/local.yaml up -d

.PHONY: runproject-build
runproject-build:
	docker compose -f api/docker/local.yaml up --build

# git commands
.PHONY: push-origin
push-origin:
	git push origin $$(git symbolic-ref --short HEAD)

.PHONY: push-origin-force
push-origin-force:
	git push origin $$(git symbolic-ref --short HEAD) --force

.PHONY: pull-origin
pull-origin:
	git pull origin $$(git symbolic-ref --short HEAD)
