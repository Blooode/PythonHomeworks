# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

print("Make two numbers.")
first_number = 1
second_number = 1
numbers_sum = int(input("Enter the sum of two numbers: "))
numbers_product = int(input("Enter the product of two numbers: "))
while ((first_number + second_number != numbers_sum or first_number * second_number != numbers_product) and
       first_number < 1000):
    first_number += 1
    second_number = 1
    while ((first_number + second_number != numbers_sum or first_number * second_number != numbers_product) and
       first_number < 1000 and second_number < 1000):
        second_number += 1
        print(f"{first_number} + {second_number} = {first_number + second_number}")
        print(f"{first_number} * {second_number} = {first_number * second_number}", end = "\n\n")
if first_number > 1000 or second_number > 1000:
    print("There are no true numbers")
else:
    print(f"Hidden numbers are {first_number} and {second_number}")