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
        'quantity': 3,
        'offer': 130,
    },
    'B': {
        'quantity': 2,
        'offer': 45,
    }
}


def checkout(skus):
    if not isinstance(skus, str):
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
            remaining = freq % SPECIAL_OFFERS[product]['quantity']
            sum += remaining * PRICES[product]
            sum += (
                (freq / SPECIAL_OFFERS[product]['quantity']) *
                SPECIAL_OFFERS[product]['offer']
            )
            continue

        sum += freq * PRICES[product]

    return sum


