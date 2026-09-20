class Student:

    college = "ABC College"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("College:", Student.college)
        print()


student1 = Student("Harini", 20)
student2 = Student("Anu", 21)

print("Student 1:")
student1.display()

print("Student 2:")
student2.display()
