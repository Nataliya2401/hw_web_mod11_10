from pymongo import MongoClient


def get_mongodb():
    username = 'sabotab2000'
    password = 'FY0bThduF3hbN6dq'
    database_name = 'hw_web11_8'
    domain = 'sabotab2401.qnlmxn8.mongodb.net'
    uri = f"mongodb+srv://{username}:{password}@{domain}/{database_name}?retryWrites=true&w=majority"
    try:
        client = MongoClient(uri)
        db = client.hw_web11_8
    except:
        print('Connection to database failed')
        quit()
    return db
