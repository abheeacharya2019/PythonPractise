def f1(x, y):
    try:
        c = (x + y) / (x - y)
    except ZeroDivisionError:
        print("Not possible to divide with Zero")
    else:
        print(c)


f1(8.0, 3.0)
f1(3.0, 3.0)
