#!/bin/bash
GIT_DIR="./.git"
PRE_COMMIT_FILE="${GIT_DIR}/hooks/pre-commit"

if [[ ! -d ${GIT_DIR} ]]; then
    echo "Initializing git respository..."
    git init
fi

if ! command -v pre-commit; then
    echo "Please install pre-commit to continue..."
    exit 1
elif [[ ! -f ${PRE_COMMIT_FILE} ]]; then
    echo "Installing pre-commit into git repo hooks..."
    pre-commit install
fi

{% if cookiecutter.use_docker == 'y' %}
if ! command -v mkcert &> /dev/null; then
    echo "Please install mkcert - https://github.com/FiloSottile/mkcert#mkcert"
    exit 1
fi


echo "Creating CA certificates with mkcert..."
make install-certs


echo """
==================================================
  Add the following to /etc/hosts file:
  127.0.0.1 {{cookiecutter.local_https_domain_name}}
==================================================
"""
{% endif %}
