# TODO Найдите количество книг, которое можно разместить на дискете
inf_value = int (1.44 * 1024 * 1024)
pages = 100
strok = 50
symbols = 25
one_symbol = 4
print("Количество книг, помещающихся на дискету:", inf_value // (pages * strok * symbols * one_symbol))