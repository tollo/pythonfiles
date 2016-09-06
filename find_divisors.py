# Find common divisors of two numbers
# Introduction to Compututation and Programming uising Python

d = {}
for x in 'ab':
    # Error handling for data types other than 'int'
    while True:
        try:
            input_value = int(input('Integer_' + str(x) + ': '))
            break
        except ValueError:
            print('Please enter only integers')
    d['Integer_{0}'.format(x)] = input_value


def findDivisors(n1, n2):
    """Assumes that n1 and n2 are positive integers
       Returns a tuple containing all common divisors of n1 and n2"""
    divisors = ()  # the empty tuple
    for i in range(1, min(n1, n2) + 1):
        if n1 % i == 0 and n2 % 1 == 0:
            divisors = divisors + (i,)
    return divisors

divisors = findDivisors(d['Integer_a'], d['Integer_b'])
print(divisors)
total = 0
for d in divisors:
    total += d
print(total)


# def findDivisors(n1, n2):
#    """Assumes that n1 and n2 are positive integers
#       Returns a tuple containing all common divisors of n1 and n2"""
#    divisors = ()  # the empty tuple
#    for i in range(1, min(n1, n2) + 1):
#        if n1 % i == 0 and n2 % 1 == 0:
#            divisors = divisors + (i,)
#    return divisors
#
# divisors = findDivisors(20, 100)
# print(divisors)
# total = 0
# for d in divisors:
#    total += d
# print(total)