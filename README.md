# logs_analysis
Código desenvolvido para o Projeto Análise de Logs para o Curso de Web Full-Stack da Udacity

## Visão geral do projeto
Esse projeto foi desenvolvido para criar uma ferramenta de relatórios que imprime relatórios (em texto sem formatação) com base nos dados do banco de dados.
Esta ferramenta de relatórios é um programa em Python usando o módulo psycopg2 para se conectar ao banco de dados.

### Pré-requisito
 - Python
 - psycipg2
 - Vagrant
 - VirtualBox
 - Base de dados postgresql

### Setup
 - Instalar Vagrant e VirtualBox
 - Clonar repositório git

## Para executar
Iniciar a VM com o comando 'vagrant up', e depois conectar no servidor com o comando 'vagrant ssh'

Carregar os dados na base de dados usando o comando 'psql -d news -f newsdata.sql' 

A base de dados tem três tabelas:
 - Authors
 - Articles
 - Log

Para executar o programa basta executar o comando 'python logs_analysis.py em linha de comando.

## Autor

* **Fabio Rego** - *Trabalho inicial* - [fabiotavarespr](https://github.com/fabiotavarespr)

Veja a lista de pessoas que [contribuiram](https://github.com/fabiotavarespr/Movie/contributors) nesse projeto.
