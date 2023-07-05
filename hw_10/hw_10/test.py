from bson.objectid import ObjectId

from hw_10.quotes.utils import get_mongodb

id__ = '64903897d07dbbe295e79fc6'
id2 = '64903894d07dbbe295e79f94'



def main(_id):
    db = get_mongodb()
    quote = db.quotes.find_one({'_id': ObjectId(id__)})
    print(quote)
    print('hellp\n')
    print(ObjectId(_id))
    author = db.author.find_one({'_id': ObjectId(id2)})
    print(author['fullname'])


def author_name():
    pass


if __name__ == '__main__':
    main(id__)
