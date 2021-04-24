FROM jwilder/nginx-proxy:alpine

RUN mkdir -p /etc/nginx/vhost.d && \
    mkdir -p /etc/nginx/certs

COPY ./certs /etc/nginx/certs
COPY ./compose/staging/nginx/{{cookiecutter.local_https_domain_name}}_location /etc/nginx/vhost.d
