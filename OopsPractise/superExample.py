class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("The name is : ", self.name)
        print("The age is : ", self.age)


class Student(Person):
    def __init__(self, name, age, rollno, marks):
        super().__init__(name, age)
        self.rollno = rollno
        self.marks = marks

    def display(self):
        super(Student, self).display()
        print("Rollno is : ", self.rollno)
        print("Mark is : ", self.marks)


s1 = Student("Abhishek", 24, 100, 89)
s1.display()
