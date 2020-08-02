import sqlite3

CREATE_BEANS_TABLE = "CREATE TABLE IF NOT EXISTS beans (id INTEGER PRIMARY KEY, name TEXT, method TEXT, rating INTEGER);"

INSERT_BEAN = "INSERT INTO beans (name, method, rating) VALUES (?, ?, ?);"

GET_ALL_BEANS = "SELECT * FROM beans;"
GET_BEANS_BY_NAME = "SELECT * FROM beans WHERE name = ?;"
GET_BEST_PREPARATION_FOR_BEAN = """
SELECT * FROM beans
WHERE name = ?
ORDER BY rating DESC
LIMIT 1;"""

# -- charts --

GET_METHODS_TO_RATINGS = "SELECT method, AVG(rating) FROM beans GROUP BY method;"
GET_COUNT_METHODS_USED = "SELECT method, COUNT(name) FROM beans GROUP by method;"


def connect(location="data.db"):
    return sqlite3.connect(location)


def create_tables(connection):
    with connection:
        connection.execute(CREATE_BEANS_TABLE)


def add_bean(connection, name, method, rating):
    with connection:
        connection.execute(INSERT_BEAN, (name, method, rating))


def get_all_beans(connection):
    with connection:
        return connection.execute(GET_ALL_BEANS).fetchall()


def get_beans_by_name(connection, name):
    with connection:
        return connection.execute(GET_BEANS_BY_NAME, (name,)).fetchall()


def get_best_preparation_for_bean(connection, name):
    with connection:
        return connection.execute(GET_BEST_PREPARATION_FOR_BEAN, (name,)).fetchone()


def get_methods_to_ratings(connection):
    with connection:
        return connection.execute(GET_METHODS_TO_RATINGS).fetchall()


def get_count_of_methods_used(connection):
    with connection:
        return connection.execute(GET_COUNT_METHODS_USED).fetchall()
