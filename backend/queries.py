from typing import List

from config import FETCH_BATCH_SIZE
from models import Spectacle


def tuple_to_json(data: tuple, order):
    return {key_name: value for key_name, value in zip(order, data)}


def select_query(connection, table, fields, model, limit=0, offset=0, predicate=""):
    cursor = connection.cursor()
    query = f"SELECT {', '.join(fields)} " \
            f"FROM {table}"
    if predicate:
        query += predicate
    if limit:
        query += f" LIMIT {limit} "
        if offset:
            query += f" OFFSET{offset}"
    cursor.execute(query)
    loaded = []
    while records := cursor.fetchmany(FETCH_BATCH_SIZE):
        loaded += [
            model.parse_obj(tuple_to_json(record, fields))
            for record in records
        ]
    return loaded


async def get_spectacles(connection, ids: List[int] = None):
    predicate = f"WHERE ids IN ({', '.join(ids or [])})"
    cursor = connection.cursor()
    fields_order = ("id", "name", "description")
    query = f"SELECT {', '.join(fields_order)} FROM "\
            f"spectacles {predicate if ids else ''};"
    cursor.execute(query)
    records = cursor.fetchmany(FETCH_BATCH_SIZE)
    loaded = [
        Spectacle.parse_obj(tuple_to_json(record, fields_order))
        for record in records
    ]
    return loaded
