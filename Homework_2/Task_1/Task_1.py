# �� ����� ����� n �������. ��������� �� ��� ����� ����� ������, � ��������� � ������.
# ���������� ����������� ����� �������, ������� ����� �����������, ����� ��� ������� ����
# ��������� ����� ����� � ��� �� ��������. �������� ����������� ���������� �����, ������� ����� �����������
# heads = 0, tails = 1

import random

coins_amount = int(input("Enter the amount of coins: "))
heads_amount = 0
tails_amount = 0
for i in range(coins_amount):
    if random.randint(0, 1) == 0:
        heads_amount += 1
    else:
        tails_amount += 1
if heads_amount > tails_amount:
    print(f"It's need to turn over {tails_amount} coins")
else:
    print(f"It's need to turn over {heads_amount} coins")