import random


def generate_numbers(amount, min_value=0, max_value=0):
    result = []
    for i in range(0, amount):
        result.append(random.randint(min_value, max_value))
    return result
