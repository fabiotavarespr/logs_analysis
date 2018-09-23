#!/usr/bin/env python3
# encoding: utf-8
"""Projeto de Analise de Log do Curso de nanodegree Full Stack da Udacity"""
import psycopg2


def conectar_na_base_de_dados():
    """Conectando ao banco de dados news e retornando o cursor."""
    try:
        database = psycopg2.connect("dbname=news")
        cursor = database.cursor()
    except Exception:
        print("Falha a conectar ao banco de dados PostgreSQL.")
        return None
    else:
        return cursor


def tres_artigos_mais_populares(db_cursor):
    """Query que retorna quais são os três artigos mais
         populares de todos os tempos.
    """
    query = """
            SELECT articles.title,
                   count(*)
            FROM   log,
                   articles
            WHERE  log.path = '/article/' || articles.slug
            GROUP BY articles.title
            ORDER BY count(*) DESC
            LIMIT 3;
    """
    db_cursor.execute(query)
    results = db_cursor.fetchall()

    print('==============================================')
    print('Três artigos mais populares de todos os tempos')
    print('==============================================')

    for result in results:
        print('"{title}" - {count} views'
              .format(title=result[0], count=result[1]))

    return


def autor_mais_popular(db_cursor):
    """Query que retorna quem são os autores de
        artigos mais populares de todos os tempos
    """
    query = """
            SELECT authors.name,
                   count(*)
            FROM   log,
                   articles,
                   authors
            WHERE  log.path = '/article/' || articles.slug
              AND articles.author = authors.id
            GROUP BY authors.name
            ORDER BY count(*) DESC;
    """
    db_cursor.execute(query)
    results = db_cursor.fetchall()

    print('====================================================')
    print('Autores de artigos mais populares de todos os tempos')
    print('====================================================')

    for result in results:
        print('{author} - {count} views'
              .format(author=result[0], count=result[1]))

    return


def dias_mais_1pc_com_erro(db_cursor):
    """Query que retorna em quais dias mais de 1% das
        requisições resultaram em erros
    """
    query = """
            WITH num_requests AS (
                SELECT time::date AS day, count(*)
                FROM log
                GROUP BY time::date
                ORDER BY time::date
              ), num_errors AS (
                SELECT time::date AS day, count(*)
                FROM log
                WHERE status != '200 OK'
                GROUP BY time::date
                ORDER BY time::date
              ), error_rate AS (
                SELECT num_requests.day,
                  num_errors.count::float / num_requests.count::float * 100
                  AS error_pc
                FROM num_requests, num_errors
                WHERE num_requests.day = num_errors.day
              )
            SELECT * FROM error_rate WHERE error_pc > 1;
    """
    db_cursor.execute(query)
    results = db_cursor.fetchall()

    print('===================================================')
    print('Dias mais de 1% das requisições resultaram em erros')
    print('===================================================')

    for result in results:
        print('{date:%B %d, %Y} - {error_rate:.1f}% errors'.format(
            date=result[0],
            error_rate=result[1]))

    return


if __name__ == "__main__":
    CURSOR = conectar_na_base_de_dados()
    if CURSOR:
        tres_artigos_mais_populares(CURSOR)
        autor_mais_popular(CURSOR)
        dias_mais_1pc_com_erro(CURSOR)
        CURSOR.close()
