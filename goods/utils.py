from django.db.models import Q

from goods.models import Categories, Products

def q_search(query):
    if query.isdigit():
        return Products.objects.filter(id=int(query))

    keywords =  [i for i in query.split() if len(i) > 2]

    q_obj = Q()


    for i in keywords:
        q_obj |= Q(name__contains=i) | Q(description__contains=i)

        print(q_obj)

    return Products.objects.filter(q_obj)