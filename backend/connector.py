from contextlib import contextmanager

import mariadb


@contextmanager
def mariadb_connection(params):
    connection = mariadb.connect(**params)
    try:
        yield connection
    finally:
        connection.close()
