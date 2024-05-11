from pymongo import MongoClient


def get_mongodb():
    client = MongoClient("mongodb+srv://andriiliubov:K6LoCzTyrzjS5nIt@cluster0.exgrzep.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    db = client.Poets

    return db
