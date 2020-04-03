class TooYoungException(Exception):
    def __init__(self, arg):
        self.msg = arg


class TooOldException(Exception):
    def __init__(self, arg):
        self.msg = arg


age = int(input("Please enter your age for marriage :"))
if age < 18:
    raise TooYoungException("You are too young to marry")
elif age > 60:
    raise TooOldException("You are too old to marry")
else:
    print("You are eligible for marriage")
