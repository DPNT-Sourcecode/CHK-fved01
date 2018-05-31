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
    'K': 80,
    'L': 90,
    'M': 15,
    'N': 40,
    'O': 10,
    'P': 50,
    'Q': 30,
    'R': 50,
    'S': 30,
    'T': 20,
    'U': 40,
    'V': 50,
    'W': 20,
    'X': 90,
    'Y': 10,
    'Z': 50,
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
        2: 150,
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
    }
}

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


def _check_special_offers(product, freq, offer, offer_list):
    sum = 0
    remaining = freq % offer_list[offer]

    if remaining < offer_list[-1]:
        sum += remaining * PRICES[product]
    elif offer + 1 < len(offer_list):
        sum += _check_special_offers(product, remaining, offer + 1, offer_list)

    sum += (
        (freq / offer_list[offer]) * SPECIAL_OFFERS[product][offer_list[offer]]
    )

    return sum


# TODO: Still not unittestable
def _check_free_offers(frequencies, product):
    if product in FREE_OFFERS.keys():
        for offer in FREE_OFFERS[product].keys():
            changes = frequencies[product] / offer
            if changes:
                for changeble in FREE_OFFERS[product][offer].keys():
                    if 'limit' in FREE_OFFERS[product][offer][changeble]:
                        remaining = (
                            changes % FREE_OFFERS[product][offer][changeble]['limit'])
                        if remaining > 0:
                            changes = (
                                frequencies[product] / FREE_OFFERS[product][offer][changeble]['limit'])
                        elif remaining == 0:
                            changes -= 1

                    frequencies[changeble] -= (
                        changes * FREE_OFFERS[product][offer][changeble]['quantity'])
                    if frequencies[changeble] < 0:
                        frequencies[changeble] = 0


def checkout(skus):
    if not isinstance(skus, str) and not isinstance(skus, unicode):
        return -1

    sum = 0
    frequencies = defaultdict(int)

    # Count frequencies of the products on the basket
    for product in skus:
        if product not in PRICES:
            return -1
        frequencies[product] += 1

    for product in frequencies.keys():
        _check_free_offers(frequencies, product)

    for product, freq in frequencies.items():
        if product in SPECIAL_OFFERS:
            offer_list = sorted(SPECIAL_OFFERS[product].keys(), reverse=True)
            sum += _check_special_offers(product, freq, 0, offer_list)
            continue

        sum += freq * PRICES[product]

    return sum


