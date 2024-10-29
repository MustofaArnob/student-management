
import json

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def display_person_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Address: {self.address}")


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
        print(f"Student Information:\nName: {self.name}\nID: {self.student_id}\nAge: {self.age}\nAddress: {self.address}")
        print(f"Enrolled Courses: {', '.join(self.courses)}")
        print(f"Grades: {self.grades}")


class Course:
    def __init__(self, course_name, course_code, instructor):
        self.course_name = course_name
        self.course_code = course_code
        self.instructor = instructor
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_course_info(self):
        print(f"Course Information:\nCourse Name: {self.course_name}\nCode: {self.course_code}\nInstructor: {self.instructor}")
        print(f"Enrolled Students: {', '.join([student.name for student in self.students])}")
class StudentManagementSystem:
    def __init__(self):
        self.students = {}
        self.courses = {}

    def add_student(self, name, age, address, student_id):
        student = Student(name, age, address, student_id)
        self.students[student_id] = student
        print(f"Student {name} (ID: {student_id}) added successfully.")

    def add_course(self, course_name, course_code, instructor):
        course = Course(course_name, course_code, instructor)
        self.courses[course_code] = course
        print(f"Course {course_name} (Code: {course_code}) created with instructor {instructor}.")

    def enroll_student_in_course(self, student_id, course_code):
        if student_id in self.students and course_code in self.courses:
            student = self.students[student_id]
            course = self.courses[course_code]
            student.enroll_course(course.course_name)
            course.add_student(student)
            print(f"Student {student.name} (ID: {student_id}) enrolled in {course.course_name} (Code: {course_code}).")
        else:
            print("Error: Invalid student ID or course code.")

    def add_grade(self, student_id, course_code, grade):
        if student_id in self.students and course_code in self.courses:
            student = self.students[student_id]
            if course_code in student.courses:
                student.add_grade(course_code, grade)
                print(f"Grade {grade} added for {student.name} in {course_code}.")
            else:
                print("Error: Student is not enrolled in this course.")
        else:
            print("Error: Invalid student ID or course code.")

    def display_student_details(self, student_id):
        if student_id in self.students:
            self.students[student_id].display_student_info()
        else:
            print("Error: Student ID not found.")

    def display_course_details(self, course_code):
        if course_code in self.courses:
            self.courses[course_code].display_course_info()
        else:
            print("Error: Course code not found.")

def main():
    sms = StudentManagementSystem()

    while True:
        print("\n==== Student Management System ====")
        print("1. Add New Student")
        print("2. Add New Course")
        print("3. Enroll Student in Course")
        print("4. Add Grade for Student")
        print("5. Display Student Details")
        print("6. Display Course Details")
        print("0. Exit")

        choice = input("Select Option: ")

        if choice == "1":
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            address = input("Enter Address: ")
            student_id = input("Enter Student ID: ")
            sms.add_student(name, age, address, student_id)

        elif choice == "2":
            course_name = input("Enter Course Name: ")
            course_code = input("Enter Course Code: ")
            instructor = input("Enter Instructor Name: ")
            sms.add_course(course_name, course_code, instructor)

        elif choice == "3":
            student_id = input("Enter Student ID: ")
            course_code = input("Enter Course Code: ")
            sms.enroll_student_in_course(student_id, course_code)

        elif choice == "4":
            student_id = input("Enter Student ID: ")
            course_code = input("Enter Course Code: ")
            grade = input("Enter Grade: ")
            sms.add_grade(student_id, course_code, grade)

        elif choice == "5":
            student_id = input("Enter Student ID: ")
            sms.display_student_details(student_id)

        elif choice == "6":
            course_code = input("Enter Course Code: ")
            sms.display_course_details(course_code)

        
        elif choice == "0":
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
