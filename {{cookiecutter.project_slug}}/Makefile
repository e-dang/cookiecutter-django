PROJECT_DIR := `dirname $(abspath $(MAKEFILE_LIST))`
LOCAL := docker-compose -f local.yml
CLIENT := docker-compose -f client.yml
STAGING := docker-compose -f staging.yml
PRODUCTION := docker-compose -f production.yml
RUN := run --rm django
API_SPEC := swagger.yml

setup:
	./setup.sh

build-local:
	@cd $(PROJECT_DIR) && \
	$(LOCAL) build

build-staging:
	@cd $(PROJECT_DIR) && \
	$(STAGING) build

build-client:
	@cd $(PROJECT_DIR) && \
	$(CLIENT) build

build-prod:
	@cd $(PROJECT_DIR) && \
	$(PRODUCTION) build

local-up:
	@cd $(PROJECT_DIR) && \
	$(LOCAL) up

staging-up:
	@cd $(PROJECT_DIR) && \
	$(STAGING) up

prod-up:
	@cd $(PROJECT_DIR) && \
	$(PRODUCTION) up

local-down:
	@cd $(PROJECT_DIR) && \
	$(LOCAL) down

staging-down:
	@cd $(PROJECT_DIR) && \
	$(STAGING) down

client-down:
	@cd $(PROJECT_DIR) && \
	$(CLIENT) down

prod-down:
	@cd $(PROJECT_DIR) && \
	$(PRODUCTION) down

down: client-down staging-down local-down prod-down

test-u:
	@cd $(PROJECT_DIR) && \
	$(LOCAL) $(RUN) pytest -m unit

test-i:
	@cd $(PROJECT_DIR) && \
	$(LOCAL) $(RUN) pytest -m integration

test-local:
	@cd $(PROJECT_DIR) && \
	$(LOCAL) $(RUN) /bin/bash -c "pytest -m unit && pytest -m integration"

test-f: local-down
	@cd $(PROJECT_DIR); \
	$(STAGING) up -d; \
	$(CLIENT) run --rm client

test: test-local test-f

coverage:
	@cd $(PROJECT_DIR) && \
	$(LOCAL) $(RUN) /bin/bash -c "coverage run -m pytest -m \"unit or integration\" && coverage report -m"

client:
	@cd $(PROJECT_DIR) && \
	$(LOCAL) $(RUN) python manage.py spectacular --file $(API_SPEC) && \
	docker run --rm -v ${PWD}:/local swaggerapi/swagger-codegen-cli-v3 generate -i /local/$(API_SPEC) -l python -o /local/test_client
	@-rm -r $(PROJECT_DIR)/swagger_client
	@mv $(PROJECT_DIR)/test_client/swagger_client $(PROJECT_DIR)/
	@-rm -r $(PROJECT_DIR)/test_client
