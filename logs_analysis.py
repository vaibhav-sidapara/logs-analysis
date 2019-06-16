# Logs Analysis Project
# -*- coding: utf-8 -*-  "" To support UTF-8 characters like: —
# !/usr/bin/env python


import psycopg2


def select_query(query):
    # Connecting to database
    try:
        connection = psycopg2.connect(database="news")
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
    except (Exception, psycopg2.Error) as error:
        print ("Error while fetching data from PostgreSQL", error)
    finally:
        # Closing database connection.
        if(connection):
            cursor.close()
            connection.close()


def popular_articles():
    results = select_query("SELECT title, count(*) as views "
                           "FROM articles JOIN log "
                           "ON articles.slug  = substring(log.path, 10) "
                           "WHERE log.status = '200 OK'"
                           "GROUP BY title ORDER BY views DESC LIMIT 3;")
    print('\nDisplaying the most popular articles of all time:')
    for i in results:
        print(' "' + str(i[0]) + '" — ' + str(i[1]) + ' views')


def popular_authors():
    results = select_query("SELECT authors.name, count(*) as views "
                           "FROM articles JOIN authors "
                           "ON articles.author = authors.id JOIN log "
                           "ON articles.slug = substring(log.path, 10) "
                           "WHERE log.status = '200 OK' "
                           "GROUP BY authors.name ORDER BY views DESC;")
    print('\nDisplaying the most popular authors of all time:')
    for i in results:
        print(' "' + str(i[0]) + '" — ' + str(i[1]) + ' views')


def request_errors():
    # Create Views as shown in the README file.
    results = select_query("SELECT error_logs_view.date, "
                           "round(100.0 * error_logs_view.error_count"
                           "/ logs_view.log_count, 2) "
                           "as percent "
                           "FROM logs_view, error_logs_view "
                           "WHERE logs_view.date = error_logs_view.date "
                           "AND error_count > log_count / 100")
    print('\nThe days when more than 1% of requests lead to error:')
    for i in results:
        print(' ' + str(i[0]) + ' — ' + str(i[1]) + '% errors')


if __name__ == '__main__':
    popular_articles()
    popular_authors()
    request_errors()
