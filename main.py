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
        try:
            if choice == '1':
                print('Если какая-то фильтрация вам не нужна, нажмите Enter')
                print(*get_data(
                    ge_price=int(input('Отфильтруйте выше определенной цены: ')),
                    le_price=int(input('Отфильтруйте ниже определенной цены: ')),
                    stat=input('Выберите статус active/inactive: ').lower(),
                    page=int(input('Выберите страницу: ')),
                    date=input('Отфильтруйте по дате (2022-10-4 xx:xx:xx): ')), sep='\n')
            elif choice == '2':
                id_ = int(input('Введите id продукта: '))
                print(get_one_product(id_))
            elif choice == '3':
                print(post_product())
            elif choice == '4':
                id_ = int(input('Введите id продукта, который хотите обновить: '))
                print(update_product(id_))
            elif choice == '5':
                id_ = int(input('Введите id продукта, который хотите удалить: '))
                print(del_product(id_))
            elif choice.lower() == 'exit':
                break
            else:
                print('нет такого варианта!')
        except ValueError:
            print('Введите число!')


if __name__ == '__main__':
    main()
