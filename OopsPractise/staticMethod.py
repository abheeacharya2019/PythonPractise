class Math:
    @staticmethod
    def add(x, y):
        print("The sum is : ", x + y)

    @staticmethod
    def product(x, y):
        print("The product is :", x * y)

    @staticmethod
    def average(x, y):
        print("The average is :", (x+y) / 2)


Math.add(10, 20)
Math.product(10, 20)
Math.average(10, 20)
