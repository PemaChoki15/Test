class Person:
    def __init__(self, name, age, cid_number):
        self.name = name
        self.age = age
        self.cid_number = cid_number

    def walk(self):
        print(f"{self.name} is walking.")

    def talk(self):
        print(f"{self.name} is talking.")

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

class Student(Person):
    def __init__(self, name, age, cid_number, student_id, course, year, gpa):
        super().__init__(name, age, cid_number)
        self.student_id = student_id
        self.course = course
        self.year = year
        self.gpa = gpa

    def study(self):
        print(f"{self.name} is studying {self.course}.")

    def attend_class(self):
        print(f"{self.name} is attending a class in {self.course}.")

    def write_exam(self):
        print(f"{self.name} is writing an exam in {self.course}.")

class Teacher(Person):
    def __init__(self, name, age, cid_number, subject, salary, department, designation):
        super().__init__(name, age, cid_number)
        self.subject = subject
        self.salary = salary
        self.department = department
        self.designation = designation

    def teach(self):
        print(f"{self.name} is teaching {self.subject}.")

    def grade_students(self):
        print(f"{self.name} is grading students.")

    def attend_meeting(self):
        print(f"{self.name} is attending a meeting in the {self.department} department.")

student1 = Student("Pema", 20, "S12345", "STU123", "Computer Science", 2, 3.8)
teacher1 = Teacher("Mr.Dorji", 45, "T67890", "Mathematics", 70000,"Mathematics", "Professor")

student1.walk()
student1.talk()
student1.eat()
student1.sleep()

teacher1.walk()
teacher1.talk()
teacher1.eat()
teacher1.sleep()

student1.study()
student1.attend_class()
student1.write_exam()

teacher1.teach()
teacher1.grade_students()
teacher1.attend_meeting()

        
