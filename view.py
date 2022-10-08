import json
from datetime import datetime

FILE_JSON = 'data.json'


def get_data(ge_price=None, le_price=None, stat=None, page=None, date=None):
    with open(FILE_JSON) as file:
        products = json.load(file)
    if page:
        products = products[page * 3 - 3:page * 3]
    if ge_price:
        products = [i for i in products if i['price'] >= ge_price]
    if le_price:
        products = [i for i in products if i['price'] <= le_price]
    if stat == 'active' or stat == 'inactive':
        products = [i for i in products if i['status'] == stat]
    if date:
        products = [i for i in products if date in i['date of creation']]
    return products


def get_one_product(id_=None):
    products = get_data()
    product = [i for i in products if i['id'] == id_]
    if product:
        return product[0]
    return 'Нет такого продукта!'


def post_product():
    products = get_data()
    new_id = max(i['id'] for i in products) + 1
    products.append({
        'id': new_id,
        'name': input('Введите название продукта: '),
        'price': int(input('Введите цену нового продукта: ')),
        'date of creation': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'date of update': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'description': input('Введите описание: '),
        'status': 'active'
    })
    json.dump(products, open(FILE_JSON, 'w'))
    return 'created'


def update_product(id_=None):
    products = get_data()
    product = [i for i in products if i['id'] == id_]
    if product:
        ind_of_product = products.index(product[0])
        choice = input('Введите через запятую что хотите изменить:\n1-цену\n2-описание\n3-статус\n')
        if '1' in choice:
            products[ind_of_product]['price'] = int(input('Введите новую цену: '))
        if '2' in choice:
            products[ind_of_product]['description'] = input('Измените описание: ')
        if '3' in choice:
            status = input('Выберите статус: active/inactive: ')
            if status.lower() == 'active' or status.lower() == 'inactive':
                products[ind_of_product]['status'] = status
            else:
                return 'нет такого статуса!'
        products[ind_of_product]['date of update'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        json.dump(products, open(FILE_JSON, 'w'))
        return 'updated'
    return 'Нет такого продукта!'


def del_product(id_=None):
    products = get_data()
    del_prod = [i for i in products if i['id'] == id_]
    if del_prod:
        products.remove(del_prod[0])
        json.dump(products, open(FILE_JSON, 'w'))
        return 'deleted'
    return 'Нет такого продукта!'
