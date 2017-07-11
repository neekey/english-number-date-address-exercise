import random


def generate_phone_numbers(amount):
    result = []
    for i in range(0, amount):
        result.append('0' + str(random.randint(100000000, 999999999)))
    return result
