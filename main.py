from view import *


def main():
    while True:
        choice = input(
            'Выберите действие: 1-показать список продуктов\n\
            2-показать продукт по id\n\
            3-добавить продукт\n\
            4-обновить продукт\n\
            5-удалить продукт\n\
            exit чтобы выйти\n\
            Ваш выбор: '
        )
        if choice == '1':
            page1 = int(input('Выберите страницу (в одной странице будет 3 товара): '))
            filt = input(
                'Выберите способ фильтрации через запятую:\n\
                1-выше определенной цены\n\
                2-ниже определенной цены\n\
                3-фильтрация по дате\n\
                Ваш выбор: '
            )
            if '1' in filt:
                print(get_data(ge_price=int(input('Отфильтруйте выше определенной цены: ')), page=page1))
            if '2' in filt:
                print(get_data(le_price=int(input('Отфильтруйте ниже определенной цены: ')), page=page1))
            if '3' in filt:
                print(get_data(date=input('Отфильтруйте по дате (2022-10-4): '), page=page1))
            print(get_data(page=page1))
        elif choice == '2':
            print(get_one_product())
        elif choice == '3':
            print(post_product())
        elif choice == '4':
            print(update_product())
        elif choice == '5':
            print(del_product())
        elif choice.lower() == 'exit':
            break
        else:
            print('нет такого варианта!')


if __name__ == '__main__':
    main()
