#! -*- coding: utf-8 -*-
from collections import defaultdict

# noinspection PyUnusedLocal
# skus = unicode string

PRICES = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
}

SPECIAL_OFFERS = {
    'A': {
        3: 130,
        5: 200,
    },
    'B': {
        2: 45,
    }
}


def checkout(skus):
    if not isinstance(skus, str) and not isinstance(skus, unicode):
        return -1

    sum = 0
    frequences = defaultdict(int)

    for product in skus:
        if product not in PRICES:
            return -1
        frequences[product] += 1

    for product, freq in frequences.items():
        if product in SPECIAL_OFFERS:
            offer_list = sorted(SPECIAL_OFFERS[product].keys(), reverse=True)
            remaining = freq % SPECIAL_OFFERS[product]['quantity']
            sum += remaining * PRICES[product]
            sum += (
                (freq / SPECIAL_OFFERS[product]['quantity']) *
                SPECIAL_OFFERS[product]['offer']
            )
            continue

        sum += freq * PRICES[product]

    return sum


