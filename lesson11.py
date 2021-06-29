#exceptions

""" def divide(devideBy):
    try:
        return 42 / devideBy
    except ZeroDivisionError:
        print('error of zero division')

print(divide(3))
print(divide(0))
print(divide(15))
print(divide(9)) """

print('how many dogs do you have?')
numdog = input()
try:
    if int(numdog) >= 2:
        print('good numbers')
    else:
        print('oh very few')
except ValueError:
    print('enter only integer')