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
    },
    'B': {
        2: 45,
    }
}


def checkout(skus):
    sum = 0
    frequences = defaultdict(int)

    for product in skus:
        if product in frequences:
            frequences[product] += 1

    for sku, freq in frequences.items():
        sum += PRICES[sku] * freq

    return sum


