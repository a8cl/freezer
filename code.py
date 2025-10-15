import datetime
from decimal import Decimal

goods = {}

def add(items, title, amount, expiration_date=None):
    if expiration_date:
        year, month, day = expiration_date.split('-')
        date_object = datetime.date(int(year), int(month), int(day))
    else:
        date_object = None
    if title in items:
        temp_list = items[title]
        temp_list.append({'amount': Decimal(str(amount)), 'expiration_date': date_object})
        items[title] = temp_list
    else:
        items[title] = [{'amount': Decimal(str(amount)), 'expiration_date': date_object}]

def add_by_note(items, note):
    data = note.split()
    title = ''
    expiration_date = None
    amount = 0
    for k in data:
        if k[0] not in '0123456789':
            if title:
                title = title + ' ' + k
            else:
                title = k
        else:
            if amount > 0:
                expiration_date = k
            else:
                amount = Decimal(k)
    add(items, title, amount, expiration_date)

def find(items, needle):
    return_list = []
    for title in items:
        if str.lower(needle) in str.lower(title):
            return_list.append(title)
    return return_list

def amount(items, needle):
    list_of_items = find(items, needle)
    counter = Decimal('0')
    for i in list_of_items:
        for k in range(len(items[i])):
            counter += items[i][k]['amount']
    return counter
