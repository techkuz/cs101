# Given a variable, x, that stores the 
# value of any decimal number, write Python 
# code that prints out the nearest whole 
# number to x.
# If x is exactly half way between two 
# whole numbers, round up, so
# 3.5 rounds to 4 and 2.5 rounds to 3.
# You may assume x is not negative.

# Hint: The str function can convert any number into a string.
# eg str(89) converts the number 89 to the string '89'

# Along with the str function, this problem can be solved 
# using just the information introduced in unit 1.

# x = 3.14159 
# >>> 3 (not 3.0)
# x = 27.63 
# >>> 28 (not 28.0)
# x = 3.5 
# >>> 4 (not 4.0)

x = 999.67

#ENTER CODE BELOW HERE

y = str(x)
middle_value = y.find('.')
final_y = y[:middle_value]
#print final_y
#print middle_value
test_string = y[middle_value + 1: middle_value + 2]
#print test_string
test_value5 = test_string.find('5')
test_value6 = test_string.find('6')
test_value7 = test_string.find('7')
test_value8 = test_string.find('8')
test_value9 = test_string.find('9')
final = y
print int(final_y) + 5 + int(test_value5) + int(test_value6) + int(test_value7) + int(test_value8) + int(test_value9)
x = y












