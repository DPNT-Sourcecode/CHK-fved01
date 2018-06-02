#! -*- coding: utf-8 -*-
from collections import defaultdict

# noinspection PyUnusedLocal
# skus = unicode string

PRICES = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
    'E': 40,
    'F': 10,
    'G': 20,
    'H': 10,
    'I': 35,
    'J': 60,
    'K': 70,
    'L': 90,
    'M': 15,
    'N': 40,
    'O': 10,
    'P': 50,
    'Q': 30,
    'R': 50,
    'S': 20,
    'T': 20,
    'U': 40,
    'V': 50,
    'W': 20,
    'X': 17,
    'Y': 20,
    'Z': 21,
}

SPECIAL_OFFERS = {
    'A': {
        3: 130,
        5: 200,
    },
    'B': {
        2: 45,
    },
    'H': {
        5: 45,
        10: 80,
    },
    'K': {
        2: 120,
    },
    'P': {
        5: 200,
    },
    'Q': {
        3: 80,
    },
    'V': {
        2: 90,
        3: 130,
    },
    'S': {
        3: 45,
    },
}

IDENTICAL_SPECIAL_OFFERS = [
    'STXYZ',
]

FREE_OFFERS = {
    'E': {
        2: {
            'B': {
                'quantity': 1,
            },
        },
    },
    'F': {
        2: {
            'F': {
                'quantity': 1,
                'limit': 3,
            },
        },
    },
    'N': {
        3: {
            'M': {
                'quantity': 1,
            },
        },
    },
    'R': {
        3: {
            'Q': {
                'quantity': 1,
            },
        },
    },
    'U': {
        3: {
            'U': {
                'quantity': 1,
                'limit': 4,
            }
        }
    }
}


def _check_special_offers(product, freq, offer_list, offer=None):
    offer = offer or 0
    sum = 0
    offer_quantity = offer_list[offer]
    remaining = freq % offer_quantity

    if remaining < offer_list[-1]:
        sum += remaining * PRICES[product]
    elif offer + 1 < len(offer_list):
        sum += _check_special_offers(product, remaining, offer_list, offer + 1)

    sum += (
        (freq / offer_quantity) * SPECIAL_OFFERS[product][offer_quantity]
    )

    return sum


def checkout(skus):
    if not isinstance(skus, str) and not isinstance(skus, unicode):
        return -1

    sum = 0
    frequencies = defaultdict(int)
    identical_frequencies = defaultdict(list)

    # Count frequencies of the products on the basket
    for product in skus:
        if product not in PRICES:
            return -1

        identical_offer_found = False
        for identical_offer in IDENTICAL_SPECIAL_OFFERS:
            if product in identical_offer:
                identical_offer_found = True
                identical_frequencies[identical_offer].append(product)

        if identical_offer_found:
            continue

        frequencies[product] += 1

    import pdb; pdb.set_trace()

    # Apply free offers
    for product in frequencies.keys():
        if product not in FREE_OFFERS.keys():
            continue

        for offer in FREE_OFFERS[product].keys():
            changes = frequencies[product] / offer
            if not changes:
                continue

            for changable in FREE_OFFERS[product][offer].keys():
                if 'limit' in FREE_OFFERS[product][offer][changable]:
                    remaining = (
                        changes % FREE_OFFERS[product][offer][changable]['limit'])

                    if remaining > 0:
                        changes = (
                            frequencies[product] / FREE_OFFERS[product][offer][changable]['limit'])
                    elif remaining == 0:
                        changes -= 1

                frequencies[changable] -= (
                    changes * FREE_OFFERS[product][offer][changable]['quantity'])

                if frequencies[changable] < 0:
                    frequencies[changable] = 0

    for product, freq in frequencies.items():
        if product in SPECIAL_OFFERS:
            offer_list = sorted(SPECIAL_OFFERS[product].keys(), reverse=True)
            sum += _check_special_offers(product, freq, offer_list)
            continue

        sum += freq * PRICES[product]

    return sum
