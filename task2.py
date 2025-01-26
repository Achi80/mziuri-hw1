def digit_sum(number, target):

    digit_sum = sum(int(digit) for digit in str(number))
    return digit_sum == target

number = 1121
target = 5

if digit_sum(number, target):
    print(f"The sum of the digits in {number} equals {target}.")
else:
    print(f"The sum of the digits in {number} does not equal {target}.")