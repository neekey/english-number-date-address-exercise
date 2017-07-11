from lib.address_generator import request_search, transform_place_results
from lib.number_generator import generate_numbers
from lib.phone_number_generator import generate_phone_numbers
from lib.date_generator import generate_dates
from config import GOOGLE_API_KEY, ADDRESS_FILE_NAME, NUMBERS_FILE_NAME, PHONE_NUMBERS_FILE_NAME, DATE_FILE_NAME
import re
import json
from lib.polly import text_to_voice

# ====== generate address ======
australia_cities = [
    'melbourne',
    'sydney',
    'Brisbane',
    'Adelaide',
    'Perth',
    'Canberra',
]


def get_address_in_australia():
    result = []
    for city in australia_cities:
        address = request_search(GOOGLE_API_KEY, 'bank', city, 'australia')
        result += address
    result = transform_place_results(result)
    return [re.sub(r'\s\w+\s\d+,\sAustralia$', '', address) for address in result]

addresses = get_address_in_australia()

address_file = open('data/' + ADDRESS_FILE_NAME, 'w')
address_file.write(json.dumps(addresses))
address_file.close()

# ====== generate numbers ======
numbers = generate_numbers(50, 10, 99)
numbers += generate_numbers(50, 100, 999)
numbers += generate_numbers(50, 1000, 9999)
numbers += generate_numbers(50, 10000, 99999)
numbers += generate_numbers(50, 100000, 999999)
numbers += generate_numbers(50, 10000000, 99999999)
numbers_file = open('data/' + NUMBERS_FILE_NAME, 'w')
numbers_file.write(json.dumps(numbers))
numbers_file.close()


# ====== generate phone numbers ======
phone_numbers = generate_phone_numbers(100)
phone_numbers_file = open('data/' + PHONE_NUMBERS_FILE_NAME, 'w')
phone_numbers_file.write(json.dumps(numbers))
phone_numbers_file.close()

# ====== generate date ======
dates = generate_dates(100)
dates_file = open('data/' + DATE_FILE_NAME, 'w')
dates_file.write(json.dumps(numbers))
dates_file.close()


# ====== text to voice ======

def save_voice(text, data):
    f = open('data/' + text + '.mp3', 'wb')
    f.write(data)
    f.close()

for number in numbers:
    response = text_to_voice(str(number))
    save_voice('number_' + str(number), response.get('AudioStream').read())

for address in addresses:
    address = address.replace('/', ' ')
    response = text_to_voice(address)
    save_voice('address_' + address, response.get('AudioStream').read())

for phone in phone_numbers:
    response = text_to_voice(str(phone))
    save_voice('phone_' + str(phone), response.get('AudioStream').read())

for date in dates:
    response = text_to_voice(date)
    save_voice('date_' + date, response.get('AudioStream').read())

