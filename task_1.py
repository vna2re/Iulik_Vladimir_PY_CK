# TODO Напишите функцию для поиска индекса товара

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']


def find_item_func(name):
    k = 0
    for item in items_list:
        if item == name:
           return k
        k += 1


for find_item in ['банан', 'груша', 'персик']:
    index_item = find_item_func(find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
