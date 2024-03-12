student_list = []
student_dict = {}

# Add list
def add_student():
    name = input("Enter student's name: ")
    age = int(input("Enter student's age: "))
    grade = int(input("Enter student's grade: "))

    student_list.append(name)
    student_dict[name] = {'age': age, 'grade': grade}

    print(f"Student information added successfully!")
    print(student_dict)

def search_student():
    name = input("Enter the name of the student to search or simply enter to skip: ")
    if name in student_dict:
        print(f"Student found!\nName: {name}\nAge: {student_dict[name]['age']}\nGrade: {student_dict[name]['grade']}")
    else:
        print(f"Student not found!")

def remove_student():
    name = input("Enter the name of the student to remove or simply enter to skip: ")
    if name in student_dict:
        student_list.remove(name)
        del student_dict[name]
        print(f"Student removed successfully!")
        print(student_dict)
    else:
        print(f"Student not found!")

# Test the system
add_student()
search_student()
remove_student()
