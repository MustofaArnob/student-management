
import json

# Class 1: Person
class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def display_person_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Address: {self.address}")

# Class 2: Student (inherits from Person)
class Student(Person):
    def __init__(self, name, age, address, student_id):
        super().__init__(name, age, address)
        self.student_id = student_id
        self.grades = {}
        self.courses = []

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def enroll_course(self, course):
        self.courses.append(course)

    def display_student_info(self):
        super().display_person_info()
        print(f"Student ID: {self.student_id}, Courses: {self.courses}, Grades: {self.grades}")

# Class 3: Course
class Course:
    def __init__(self, course_name, course_code, instructor):
        self.course_name = course_name
        self.course_code = course_code
        self.instructor = instructor
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_course_info(self):
        print(f"Course Name: {self.course_name}, Code: {self.course_code}, Instructor: {self.instructor}")
        print("Enrolled Students: ", [student.name for student in self.students])

# Data storage
students = []
courses = []

# System functionalities
def add_student(name, age, address, student_id):
    student = Student(name, age, address, student_id)
    students.append(student)
    print(f"Student {name} (ID: {student_id}) added successfully.")

def add_course(course_name, course_code, instructor):
    course = Course(course_name, course_code, instructor)
    courses.append(course)
    print(f"Course {course_name} (Code: {course_code}) created with instructor {instructor}.")

def enroll_student_in_course(student_id, course_code):
    student = next((s for s in students if s.student_id == student_id), None)
    course = next((c for c in courses if c.course_code == course_code), None)
    if student and course:
        student.enroll_course(course.course_name)
        course.add_student(student)
        print(f"Student {student.name} (ID: {student_id}) enrolled in {course.course_name} (Code: {course_code}).")
    else:
        print("Invalid student ID or course code.")

def add_grade_for_student(student_id, course_code, grade):
    student = next((s for s in students if s.student_id == student_id), None)
    if student and course_code in [course.course_code for course in courses if course.course_name in student.courses]:
        student.add_grade(course_code, grade)
        print(f"Grade {grade} added for {student.name} in {course_code}.")
    else:
        print("Invalid student ID or course code.")

def display_student_details(student_id):
    student = next((s for s in students if s.student_id == student_id), None)
    if student:
        student.display_student_info()
    else:
        print("Student not found.")

def display_course_details(course_code):
    course = next((c for c in courses if c.course_code == course_code), None)
    if course:
        course.display_course_info()
    else:
        print("Course not found.")

def save_data():
    data = {
        "students": [
            {
                "name": s.name,
                "age": s.age,
                "address": s.address,
                "student_id": s.student_id,
                "grades": s.grades,
                "courses": s.courses
            }
            for s in students
        ],
        "courses": [
            {
                "course_name": c.course_name,
                "course_code": c.course_code,
                "instructor": c.instructor,
                "students": [s.student_id for s in c.students]
            }
            for c in courses
        ]
    }
    with open("data.json", "w") as f:
        json.dump(data, f)
    print("All student and course data saved successfully.")

def load_data():
    global students, courses
    try:
        with open("data.json", "r") as f:
            data = json.load(f)
            students = [Student(**s) for s in data["students"]]
            courses = [Course(**c) for c in data["courses"]]
            for course in courses:
                for student_id in course.students:
                    student = next((s for s in students if s.student_id == student_id), None)
                    if student:
                        course.students.append(student)
                        student.enroll_course(course.course_name)
        print("Data loaded successfully.")
    except FileNotFoundError:
        print("No saved data found.")

# CLI Menu
def main():
    while True:
        print("\n==== Student Management System ====")
        print("1. Add New Student")
        print("2. Add New Course")
        print("3. Enroll Student in Course")
        print("4. Add Grade for Student")
        print("5. Display Student Details")
        print("6. Display Course Details")
        print("7. Save Data to File")
        print("8. Load Data from File")
        print("0. Exit")
        option = input("Select Option: ")

        if option == "1":
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            address = input("Enter Address: ")
            student_id = input("Enter Student ID: ")
            add_student(name, age, address, student_id)
        elif option == "2":
            course_name = input("Enter Course Name: ")
            course_code = input("Enter Course Code: ")
            instructor = input("Enter Instructor Name: ")
            add_course(course_name, course_code, instructor)
        elif option == "3":
            student_id = input("Enter Student ID: ")
            course_code = input("Enter Course Code: ")
            enroll_student_in_course(student_id, course_code)
        elif option == "4":
            student_id = input("Enter Student ID: ")
            course_code = input("Enter Course Code: ")
            grade = input("Enter Grade: ")
            add_grade_for_student(student_id, course_code, grade)
        elif option == "5":
            student_id = input("Enter Student ID: ")
            display_student_details(student_id)
        elif option == "6":
            course_code = input("Enter Course Code: ")
            display_course_details(course_code)
        elif option == "7":
            save_data()
        elif option == "8":
            load_data()
        elif option == "0":
            print("Exiting Student Management System. Goodbye!")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()

