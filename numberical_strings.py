import math


new_string = "Hello world!"
fizz = new_string[0:5]
print(fizz)
print(new_string)
telephone_num = "041 123 1234"
print(telephone_num)
capital_amount = 12000
interest_rate = 6
duration = 60
month = 12
print(capital_amount * interest_rate * duration/month)

num1 = 12
num2 = 99.99
print(float(num1))
# Converting floats to ints, as below, causes data loss. int() removes values
# after the decimal point, returning only a whole number.
print(int(num2))
sum = 2 + 4
print(sum)
# prints out 6
cents = 0.25 + 4.33
print(cents)
# prints out 4.58
number = 66.6564544
print(round(number, 2))
# prints 66.66
numbers_list = [6, 4, 66, 35, 1]
print(min(numbers_list))
# print out 1
numbers_list = [6, 4, 66, 35, 1]
print(max(numbers_list))
# output 66
print(math.floor(30.3333))
# outputs 30.0
print(math.ceil(30.3333))
# output 31.0
print(math.trunc(30.33333))
# output 30
