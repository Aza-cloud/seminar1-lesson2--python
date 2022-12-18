# ** 5. Реализуйте алгоритм перемешивания списка.
# Без функции shuffle из модуля random.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]
# ______________________________________________
import random

original_list = []
n = int(input("Enter the value of N: "))
for i in range(0, n):
    original_list.append(i)
print(original_list)
# Создаем копию, поскольку мы не должны изменять оригинал
list = original_list[:]
# Цикл от 0 до длины списка -1
list_length = len(list)
for i in range(list_length):
    # Получение случайного индекса
    index_aleatory = random.randint(0, list_length - 1)
    # Замена
    temp = list[i]
    list[i] = list[index_aleatory]
    list[index_aleatory] = temp
print(list)