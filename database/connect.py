import json
from uuid import uuid4

DB_FILE = "db.json"


def read_db():
    try:
        with open(DB_FILE, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    return data


def write_db(data):
    with open(DB_FILE, 'w') as file:
        json.dump(data, file, indent=2)


def get_all():
    return read_db()


def get_one(id):
    data = read_db()
    item = next((item for item in data if item["id"] == id), None)
    return item


def get_last_10():
    data = read_db()
    last_10_items = data[-10:]
    return last_10_items


def create(uz, ru):
    data = read_db()
    new_item = {
        "id": str(uuid4()),
        "uz": uz,
        "ru": ru
    }
    data.append(new_item)
    write_db(data)
    return new_item


def update(id, uz=None, ru=None):
    data = read_db()
    item = next((item for item in data if item["id"] == id), None)

    if item:
        if uz is not None:
            item["uz"] = uz
        if ru is not None:
            item["ru"] = ru

        write_db(data)

    return item


def delete(id):
    data = read_db()
    item = next((item for item in data if item["id"] == id), None)

    if item:
        data.remove(item)
        write_db(data)

    return item
