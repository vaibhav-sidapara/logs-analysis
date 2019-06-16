# Logs Analysis Project
# -*- coding: utf-8 -*- To support UTF-8 characters like: —
# !/usr/bin/env python


import psycopg2


def select_query(query):
    # Connecting to database
    try:
        connection = psycopg2.connect(database="news")
        print("\nPostgreSQL connection is open")
        cursor = connection.cursor()
        cursor.execute(query)
        print("PostgreSQL query execute")
        return cursor.fetchall()
    except (Exception, psycopg2.Error) as error:
        print ("Error while fetching data from PostgreSQL", error)
    finally:
        # Closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


def popular_articles():
    results = select_query("SELECT title, count(*) as views "
                           "FROM articles JOIN log "
                           "ON articles.slug = substring(log.path, 10) "
                           "GROUP BY title ORDER BY views DESC LIMIT 3;")
    print('\nDisplaying the most popular articles of all time:')
    for i in results:
        print(' ' + str(i[0]) + ' — ' + str(i[1]) + ' views')


def popular_authors():
    results = select_query("SELECT authors.name, count(*) as views "
                           "FROM articles JOIN authors "
                           "ON articles.author = authors.id JOIN log "
                           "ON articles.slug = substring(log.path, 10) "
                           "WHERE log.status LIKE '200 OK' "
                           "GROUP BY authors.name ORDER BY views DESC;")
    print('\nDisplaying the most popular authors of all time:')
    for i in results:
        print(' ' + str(i[0]) + ' — ' + str(i[1]) + ' views')


if __name__ == '__main__':
    popular_articles()
    popular_authors()
