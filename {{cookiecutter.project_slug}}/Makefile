PROJECT_DIR := `dirname $(abspath $(MAKEFILE_LIST))`
LOCAL := docker-compose -f local.yml
PRODUCTION := docker-compose -f production.yml
RUN := run --rm django

build-local:
	@cd $(PROJECT_DIR) && \
	$(LOCAL) build

build-prod:
	@cd $(PROJECT_DIR) && \
	$(PRODUCTION) build

start-local:
	@cd $(PROJECT_DIR) && \
	$(LOCAL) up

start-prod:
	@cd $(PROJECT_DIR) && \
	$(PRODUCTION) up

test-local:
	@cd $(PROJECT_DIR) && \
	$(LOCAL) $(RUN) pytest

test-prod:
	@cd $(PROJECT_DIR) && \
	$(PRODUCTION) $(RUN) pytest