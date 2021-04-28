PROJECT_DIR := `dirname $(abspath $(MAKEFILE_LIST))`
COMPOSE := docker-compose -f
RUN := run --rm django
MANAGE := python manage.py
LOCAL := $(COMPOSE) local.yml
CLIENT := $(COMPOSE) client.yml
STAGING := $(COMPOSE) staging.yml
PRODUCTION := $(COMPOSE) production.yml
API_SPEC := swagger.yml

ENVS := client local staging production
BUILD := $(addprefix build-,$(ENVS))
DOWN := $(addsuffix -down,$(ENVS))
UP := $(addsuffix -up,$(ENVS))
MIGRATE := $(addsuffix -migrate,$(filter-out client,$(ENVS)))
COLLECT_STATIC := $(addsuffix -collectstatic,$(filter-out client,$(ENVS)))

setup:
	./setup.sh

install-certs:
	@cd $(PROJECT_DIR) && \
	mkcert -install && \
	mkdir ./certs && \
	mkcert {{cookiecutter.local_https_domain_name}} && \
	mv ./{{cookiecutter.local_https_domain_name}}.pem ./certs/{{cookiecutter.local_https_domain_name}}.crt && \
	mv ./{{cookiecutter.local_https_domain_name}}-key.pem ./certs/{{cookiecutter.local_https_domain_name}}.key && \
	cp "$(shell mkcert -CAROOT)/rootCA.pem" ./certs

$(BUILD):
	@cd $(PROJECT_DIR) && \
	$(COMPOSE) $(subst build-,,$@).yml build

$(DOWN):
	@cd $(PROJECT_DIR) && \
	$(COMPOSE) $(subst -down,.yml,$@) down

$(STOP):
	@cd $(PROJECT_DIR) && \
	$(COMPOSE) $(subst -stop,.yml,$@) stop

$(UP):
	@cd $(PROJECT_DIR) && \
	$(COMPOSE) $(subst -up,.yml,$@) up

$(MIGRATE):
	@cd $(PROJECT_DIR) && \
	$(COMPOSE) $(subst -migrate,.yml,$@) $(RUN) $(MANAGE) migrate

$(COLLECT_STATIC):
	@cd $(PROJECT_DIR) && \
	$(COMPOSE) $(subst -collectstatic,.yml,$@) $(RUN) $(MANAGE) collectstatic --noinput

down: $(DOWN)

stop: $(STOP)

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
	$(STAGING) up -d; \
	$(CLIENT) run --rm client

test: test-local test-f

coverage:
	@cd $(PROJECT_DIR) && \
	$(LOCAL) $(RUN) /bin/bash -c "coverage run -m pytest -m \"unit or integration\" && coverage report -m"

swagger-client:
	@cd $(PROJECT_DIR) && \
	$(LOCAL) $(RUN) python manage.py spectacular --file $(API_SPEC) && \
	docker run --rm -v ${PWD}:/local swaggerapi/swagger-codegen-cli-v3 generate -i /local/$(API_SPEC) -l python -o /local/test_client
	@-rm -r $(PROJECT_DIR)/swagger_client
	@mv $(PROJECT_DIR)/test_client/swagger_client $(PROJECT_DIR)/
	@-rm -r $(PROJECT_DIR)/test_client
