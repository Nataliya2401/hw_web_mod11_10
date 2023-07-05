import json
from bson.objectid import ObjectId
from django import template


from ..utils import get_mongodb

# коли цитати йшли з Монго - замість автора- відображаллось id. Ф-цыя для заміни відобріження id - fullname
id__ = '64903894d07dbbe295e79f93'
id2 = '64903894d07dbbe295e79f93'

register = template.Library()


def author_name(_id):
    db = get_mongodb()
    # quote = db.quotes.find_one({'_id': ObjectId(id__)})
    # print(quote)
    # print('hellp\n')
    # print(ObjectId(_id))
    author = db.authors.find_one({'_id': ObjectId(id__)})
    return author['fullname']


register.filter('author', author_name)



# if __name__ == '__main__':
#     author_name(id__)









