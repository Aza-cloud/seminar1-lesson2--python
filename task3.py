# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
# in
# 6
# out
# [2.0, 2.25, 2.37, 2.441, 2.488, 2.522]
# 14.071

numbers_list = []
a = int(input("Введите длину списка: "))
for n in range(1, a + 1):
    numbers_list.append(round((1 + 1 / n) ** n, 3))
print(numbers_list)
res = sum(numbers_list)
print(res)
