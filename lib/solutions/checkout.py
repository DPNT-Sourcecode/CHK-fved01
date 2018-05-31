#! -*- coding: utf-8 -*-
from collections import defaultdict

# noinspection PyUnusedLocal
# skus = unicode string

PRICES = {
    u'A': 50,
    u'B': 30,
    u'C': 20,
    u'D': 15,
}

SPECIAL_OFFERS = {
    u'A': {
        u'quantity': 3,
        u'offer': 130,
    },
    u'B': {
        u'quantity': 2,
        u'offer': 45,
    }
}


def checkout(skus):
    print type(skus)
    if not isinstance(skus, str) and not isinstance(skus, unicode):
        return -1

    skus = skus.upper()
    sum = 0
    frequences = defaultdict(int)

    for product in skus:
        if product not in PRICES:
            return -1
        frequences[product] += 1

    for product, freq in frequences.items():
        if product in SPECIAL_OFFERS:
            remaining = freq % SPECIAL_OFFERS[product][u'quantity']
            sum += remaining * PRICES[product]
            sum += (
                (freq / SPECIAL_OFFERS[product][u'quantity']) *
                SPECIAL_OFFERS[product][u'offer']
            )
            continue

        sum += freq * PRICES[product]

    return sum


