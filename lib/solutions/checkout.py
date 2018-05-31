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
    freq = defaultdict(int)

    for product in skus:
        if product in freq:
            freq[product] += 1

    for sku in freq:
        sum += PRICES[product]

    return sum


