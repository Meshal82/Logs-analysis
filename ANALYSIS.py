#! /usr/bin/env python3


import psycopg2
DB = "news"
title_art = 'Top 3 articles of all time'
title_auth = 'Top authors of all time'
title_error = 'Days with more than 1% of bad requests'
q_Art = """SELECT art.title, count(*) AS n
    FROM log l , articles art
    WHERE l.status='200 OK'
    AND art.slug = substr(l.path, 10)
    GROUP BY art.title
    ORDER BY n desc
    Limit 3;"""
q_Auth = """SELECT auth.name , count(*) AS n
    FROM log l , articles art , authors auth
    WHERE l.status='200 OK'
    AND art.slug = substr(l.path, 10)
    AND auth.id = art.author
    GROUP BY auth.name
    ORDER  BY n desc
    ;"""
q_Eror = """ select * from error_percentage where perc > 1 ; """


def query_handler(sql_request):
    try:
        connection = psycopg2.connect(database=DB)
        curs = connection.cursor()
        curs.execute(sql_request)
        result = curs.fetchall()
        connection.close()
    except psycopg2.DatabaseError as e:
        print("connection failure ")
    return result


def print_resuluts(result, title):
    if (title == title_error):
        print(title, ": ")
        for name, value in result:
            print(" \"{}\" --- {} % ".format(name, value))
    else:
        print(title, ": ")
        for name, value in result:
            print(" \"{}\" --- {} views ".format(name, value))
    print("\n")


if __name__ == '__main__':
    result = query_handler(q_Art)
    print_resuluts(result, title_art)
    result = query_handler(q_Auth)
    print_resuluts(result, title_auth)
    result = query_handler(q_Eror)
    print_resuluts(result, title_error)
