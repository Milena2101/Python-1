'''Определить индексы элементов массива (списка), 
значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума)'''

list_1 = [2, -5, 3, -4, 0, 12, 7, -2, 6, 4, 13]
min_number = int(input( ))
max_number = int(input( ))
for i in range(len(list_1)):
    if min_number <= list_1[i] <= max_number:
        print(i, end=' ')

