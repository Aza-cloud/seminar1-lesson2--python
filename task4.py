# * 4. Напишите программу, которая принимает на вход 2 числа.
# Получите значение N, для пустого списка, заполните числами в диапзоне [-N, N].
# Найдите произведение элементов на указанных позициях(не индексах).
# Enter the value of N: 5
# Position one: 1
# Position two: 2
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 20
# _______________________________________________________________________________
numbers_list = []
n = int(input("Enter the value of N: "))
a = int(input("Position one: "))
b = int(input("Position two: "))
for i in range(-n, n + 1):
    numbers_list.append(i)
print(numbers_list)
res = numbers_list[a-1] * numbers_list[b-1]
print(res)