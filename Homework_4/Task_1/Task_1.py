# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания
# все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

list1_count = int(input("Enter the number of elements of the first list: "))
list2_count = int(input("Enter the number of elements of the second list: "))
list1 = list()
list2 = list()

for i in range(list1_count):
    list1.append(input(f"Number {i} in list1: "))
for i in range(list2_count):
    list2.append(input(f"Number {i} in list2: "))
global_set = set()
set1 = set()
set2 = set()
for num in list1:
    set1.add(num)
for num in list2:
    set2.add(num)
print(set1, set2)
for num in set1:
    if num in set2: global_set.add(num)
print(sorted(global_set))
