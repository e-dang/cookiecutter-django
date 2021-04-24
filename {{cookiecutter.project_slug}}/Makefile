PROJECT_DIR := `dirname $(abspath $(MAKEFILE_LIST))`
LOCAL := docker-compose -f local.yml
CLIENT := docker-compose -f client.yml
PRODUCTION := docker-compose -f production.yml
RUN := run --rm django

setup:
	./setup.sh

build-local:
	@cd $(PROJECT_DIR) && \
	$(LOCAL) build

build-client:
	@cd $(PROJECT_DIR) && \
	$(CLIENT) build

build-prod:
	@cd $(PROJECT_DIR) && \
	$(PRODUCTION) build

local-up:
	@cd $(PROJECT_DIR) && \
	$(LOCAL) up

prod-up:
	@cd $(PROJECT_DIR) && \
	$(PRODUCTION) up

local-down:
	@cd $(PROJECT_DIR) && \
	$(LOCAL) down

client-down:
	@cd $(PROJECT_DIR) && \
	$(CLIENT) down

prod-down:
	@cd $(PROJECT_DIR) && \
	$(PRODUCTION) down

down: client-down local-down prod-down

test-u:
	@cd $(PROJECT_DIR) && \
	$(LOCAL) $(RUN) pytest -m unit

test-i:
	@cd $(PROJECT_DIR) && \
	$(LOCAL) $(RUN) pytest -m integration

test-local:
	@cd $(PROJECT_DIR) && \
	$(LOCAL) $(RUN) /bin/bash -c "pytest -m unit && pytest -m integration"

test-f:
	@cd $(PROJECT_DIR); \
	$(LOCAL) up -d; \
	$(CLIENT) run --rm client

test: test-local test-f

coverage:
	@cd $(PROJECT_DIR) && \
	$(LOCAL) $(RUN) /bin/bash -c "coverage run -m pytest -m \"unit or integration\" && coverage report -m"

