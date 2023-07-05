import os
import django

from pymongo import MongoClient

# from ..quotes.utils import get_mongodb

uri = "mongodb+srv://sabotab2000:FY0bThduF3hbN6dq@sabotab2401.qnlmxn8.mongodb.net/hw_web11_8?retryWrites=true&w=majority"
client = MongoClient(uri)
db = client.hw_web11_8

# показуємо нашому скрипту, де наші моделі

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hw_10.settings")
django.setup()


from quotes.models import Author, Tag, Quote # noqa  - спец коментар для pycharma, щоб не підкреслівав

# для застосування цієї міграції в корені проекту: py -m utils.from_mongo_postgres


def full_authors():
    # db = get_mongodb()
    authors = db.author.find()
    for a in authors:
        Author.objects.get_or_create(
            fullname=a['fullname'],
            born_date=a['born_date'],
            born_location=a['born_location'],
            description=a['description']
        )
        print(a['fullname'])


def full_tags_and_quotes():
    quotes = db.quotes.find()

    # q:  {'_id': ObjectId('649038a1d07dbbe295e7a025'),
    #          'tags': ['books', 'children', 'difficult', 'grown-ups', 'write', 'writers', 'writing'],
    #          'author': ObjectId('64903897d07dbbe295e79fc4'),
    #          'quote': '“You have..."
    #       '}

    for q in quotes:
        tags = []
        for tag in q['tags']:
            t, *_ = Tag.objects.get_or_create(name=tag)
            tags.append(t)
            # print(q)
            # for t in tags:
            #     print(f"{t.name}-{t.id}")

        q_exist = bool(len(Quote.objects.filter(quote=q['quote'])))

        if not q_exist:
            author = db.author.find_one({'_id': q['author']})   # в монго_дб знайшли автора цитати
            print(author['_id'], author['fullname'])  # mongo_db
            # в постгресі шукаємо по фулнейму, (використовуємоORM django) бо автори вже занесені в постгрес
            a = Author.objects.get(fullname=author['fullname'])
            print(a.fullname)    # postgres - django
            # створюємо цитату
            quote = Quote.objects.create(
                quote=q['quote'],
                author=a
            )
            for tag in tags:
                quote.tags.add(tag)


# if __name__ == '__main__':
    # full_tags_and_quotes()
    # full_authors()

