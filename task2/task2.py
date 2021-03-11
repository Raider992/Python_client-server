import json


def write_order_to_json(item, quantity, price, buyer, date):
    data = {
        'item': item,
        'price': price,
        'quantity': quantity,
        'buyer': buyer,
        'date': date
    }
    with open('orders.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)


write_order_to_json('keyboard', 1, 3000, 'Uasya', '01.02.2021')
