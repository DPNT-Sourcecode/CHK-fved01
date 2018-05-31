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


def _check_offers(product, freq, offer, offer_list, sum):
    remaining = freq % SPECIAL_OFFERS[product][offer_list[offer]]

    if remaining < offer_list[-1]:
        import pdb; pdb.set_trace()
        sum += remaining * PRICES[product]
    else:
        sum += _check_offers(product, freq, offer_list[offer + 1], offer_list)

    sum += (
        (freq / offer_list[offer]) * SPECIAL_OFFERS[product][offer_list[offer]]
    )

    return sum


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
            sum += _check_offers(product, freq, 0, offer_list, sum)
            continue

        sum += freq * PRICES[product]

    return sum


