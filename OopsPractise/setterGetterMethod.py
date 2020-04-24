class Student:
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setMark(self, mark):
        self.mark = mark

    def getMark(self):
        return self.mark


number = int(input("Please enter the number of student : "))
for i in range(number):
    name = input("Please enter the name : ")
    mark = int(input("Please enter the mark : "))
    s = Student()
    s.setName(name)
    s.setMark(mark)

    print("Hi..", s.getName())
    print("Your mark is is ", s.getMark())
    print()
