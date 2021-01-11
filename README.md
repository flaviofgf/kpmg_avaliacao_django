# AVALIAÇÃO PYTHON: KPMG

---

## Objetivo
Este projeto visa responder à avaliação da KPMG.

Ele consiste em uma API com 2 endpoints retornando dados sumarizados de um dado dataset.
E um endpoint com a documentação da API.

Acesse a documentação da API no [Swagger](http://localhost:8000/swagger)
([http://localhost:8000/swagger](http://localhost:8000/swagger))

O acesso à API requer o basic auth e o acesso ao swagger requer login no admin do django.
O usuário e senha para as duas autenticações é `admin`.

# Iniciando
1. Subir o docker:
~~~
docker-compose up
~~~
2. Acesse à documentação da API `/swagger`:
   1. Clique em `Django Login`.
   2. Use usuário:`admin` e senha:`admin`.
1. Acesse os endpoints da API:
    1. Use usuário:`admin` e senha:`admin`.
