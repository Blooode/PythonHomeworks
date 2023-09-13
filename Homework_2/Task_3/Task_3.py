# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

max_number = int(input("Enter the maximal value: "))
i = 2
while i <= max_number:
    print(i)
    i *= 2