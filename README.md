# AVALIAÇÃO PYTHON: KPMG

## Objetivo

Este projeto visa responder à avaliação da KPMG.

Ele consiste em uma API com 2 endpoints retornando dados sumarizados de um dado dataset. E um endpoint com a
documentação da API.

Acesse a documentação da API no [Swagger](http://localhost:8000/swagger)
([http://localhost:8000/swagger](http://localhost:8000/swagger))

O acesso à API requer o basic auth e o acesso ao swagger requer login no admin do django. O usuário e senha para as duas
autenticações é `admin`.

## Iniciando

1. Implantar o docker-compose:

~~~
docker-compose up
~~~

2. Acesse à documentação da API `/swagger`:
    1. Clique em `Django Login`.
    2. Use usuário:`admin` e senha:`admin`.
1. Acesse os endpoints da API:
    1. Use usuário:`admin` e senha:`admin`.
    2. Poderá determinar o tipo da resposta da API utilizando:
        1. Sufixo na url: [
           `.json`,
           `.csv`
           ]
        2. Cabeçalho da requisição: [
           `accept: application/json`,
           `accept: text/csv`
           ]