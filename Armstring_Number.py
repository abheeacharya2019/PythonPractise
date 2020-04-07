def power(x, y):
    if y == 0:
        return 1
    else:
        return x ** y


def order(x):
    n = 0
    while x != 0:
        n = n + 1
        x = x // 10
    return n


def isArmstrong(x):
    n = order(x)
    temp = x
    sum1 = 0
    while temp != 0:
        r = temp % 10
        sum1 = sum1 + power(r, n)
        temp = temp // 10

    return sum1 == x


armstrong = eval(input("Please enter a number : "))
if isArmstrong(armstrong):
    print("{0} is a armstrong number".format(armstrong))
else:
    print("{0} is a not a armstrong1 number".format(armstrong))
