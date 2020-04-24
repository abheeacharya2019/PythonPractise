class Student:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    def display(self):
        print("Name is : ", self.name)
        print("Mark is : ", self.mark)

    def grade(self):
        if self.mark >= 60:
            print("You are first grade..")
        elif self.mark >= 50:
            print("You are second grade..")
        elif self.mark >= 35:
            print("You are third grade..")
        else:
            print("You are failed..")


number = int(input("Please number of student : "))
for i in range(number):
    name = input("Please enter name : ")
    mark = int(input("Please enter the mark : "))
    s = Student(name, mark)
    s.display()
    s.grade()
    print()
