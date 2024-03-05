# Task - 9
from abc import ABC, abstractmethod
from colorama import Fore, Style, init

init()


class StudentRepository(ABC):
    @abstractmethod
    def add_student(self, student) -> None:
        pass

    @abstractmethod
    def get_student(self, student_id: int):
        pass

    @abstractmethod
    def remove_student(self, student_id: int) -> None:
        pass


class Course(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_students(self):
        pass


class Student(ABC):
    @abstractmethod
    def get_id(self) -> int:
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_surname(self) -> str:
        pass

    @abstractmethod
    def get_courses(self) -> list:
        pass

    @abstractmethod
    def add_course(self, course) -> None:
        pass

    @abstractmethod
    def remove_course(self, course) -> None:
        pass

    @abstractmethod
    def add_grade(self, course, grade: int) -> None:
        pass

    @abstractmethod
    def get_grade(self, course):
        pass


class InMemoryStudentRepository(StudentRepository):
    def __init__(self) -> None:
        self._students = {}

    def add_student(self, student: Student) -> None:
        self._students[student.get_id()] = student

    def get_student(self, student_id: int) -> Student:
        return self._students.get(student_id)

    def remove_student(self, student_id: int) -> None:
        if student_id in self._students:
            student = self._students.pop(student_id)
            for course in student.get_courses():
                course.remove_student(student)


class SimpleCourse(Course):
    def __init__(self, name: str) -> None:
        self._name = name
        self._students = set()

    def get_name(self) -> str:
        return self._name

    def get_students(self) -> set:
        return self._students

    def add_student(self, student: Student) -> None:
        self._students.add(student)

    def remove_student(self, student: Student) -> None:
        self._students.remove(student)


class SimpleStudent(Student):
    def __init__(self, student_id: int, name: str, surname: str) -> None:
        self._id = student_id
        self._name = name
        self._surname = surname
        self._courses = []
        self._grades = {}

    def get_id(self) -> int:
        return self._id

    def get_name(self) -> str:
        return self._name

    def get_surname(self) -> str:
        return self._surname

    def get_courses(self) -> list[Course]:
        return self._courses

    def add_course(self, course) -> None:
        self._courses.append(course)
        course.add_student(self)

    def remove_course(self, course) -> None:
        self._courses.remove(course)
        course.remove_student(self)

    def add_grade(self, course, grade: int) -> None:
        self._grades[course.get_name()] = grade

    def get_grade(self, course):
        return self._grades.get(course, None)


def print_menu() -> None:
    print(Fore.BLUE, Style.BRIGHT + "1. Додати студента")
    print(Fore.BLUE, Style.BRIGHT + "2. Видалити студента")
    print(Fore.BLUE, Style.BRIGHT + "3. Відобразити інформацію про студента")
    print(Fore.BLUE, Style.BRIGHT + "4. Додати курс для студента")
    print(Fore.BLUE, Style.BRIGHT + "5. Видалити курс у студента")
    print(Fore.BLUE, Style.BRIGHT + "6. Відобразити список студентів на курсі")
    print(Fore.BLUE, Style.BRIGHT + "7. Відобразити список курсів для студента")
    print(Fore.BLUE, Style.BRIGHT + "8. Додати оцінку студенту")
    print(Fore.BLUE, Style.BRIGHT + "9. Відобразити інформацію про всіх студентів")
    print(Fore.BLUE, Style.BRIGHT + "0. Вийти" + Style.RESET_ALL)


def execute_choice(choice: str) -> None:
    try:
        if choice == "1":
            student_id = int(input("Введіть номер студента: "))
            name = input("Введіть ім'я студента: ")
            surname = input("Введіть прізвище студента: ")
            new_student = SimpleStudent(student_id, name, surname)
            student_repository.add_student(new_student)
            print(Fore.GREEN + "Студент доданий." + Style.RESET_ALL)
        elif choice == "2":
            student_id = int(input("Введіть номер студента, якого ви хочете видалити: "))
            student_repository.remove_student(student_id)
            print(Fore.GREEN + "Студент видалений." + Style.RESET_ALL)
        elif choice == "3":
            student_id = int(input("Введіть номер студента: "))
            student = student_repository.get_student(student_id)
            if student:
                print(
                    Fore.YELLOW + f"Інформація про студента:\nНомер: {student.get_id()}\nІм'я: {student.get_name()} {student.get_surname()}")
                print("Курси:")
                for course in student.get_courses():
                    print(f"- {course.get_name()}")
                    grade = student.get_grade(course.get_name())
                    print(f"  Grade: {grade}" if grade is not None else "  Grade: N/A" + Style.RESET_ALL)
            else:
                print(Fore.GREEN + "Студент не знайдений." + Style.RESET_ALL)
        elif choice == "4":
            student_id = int(input("Введіть номер студента: "))
            student = student_repository.get_student(student_id)
            if student:
                course_name = input("Введіть назву курсу: ")
                course = SimpleCourse(course_name)
                student.add_course(course)
                print(Fore.GREEN + f"Курс {course_name} доданий для студента." + Style.RESET_ALL)
            else:
                print("Студент не знайдений.")
        elif choice == "5":
            student_id = int(input("Введіть номер студента: "))
            student = student_repository.get_student(student_id)
            if student:
                course_name = input("Введіть назву курсу: ")
                for course in student.get_courses():
                    if course.get_name() == course_name:
                        student.remove_course(course)
                        print(f"Курс {course_name} видалений для студента.")
                        break
                else:
                    print("Курс не знайдений для цього студента.")
            else:
                print("Студент не знайдений.")
        elif choice == "6":
            course_name = input("Введіть назву курсу: ")
            for student in student_repository._students.values():
                for course in student.get_courses():
                    if course.get_name() == course_name:
                        print(Fore.CYAN + f"- {student.get_name()} {student.get_surname()}" + Style.RESET_ALL)
                        break
                    else:
                        print("Курс не знайдений або на ньому немає студентів.")
        elif choice == "7":
            student_id = int(input("Введіть номер студента: "))
            student = student_repository.get_student(student_id)
            if student:
                print(Fore.CYAN + f"Курси для студента {student.get_name()} {student.get_surname()}:")
                for course in student.get_courses():
                    print(f"- {course.get_name()}" + Style.RESET_ALL)
            else:
                print("Студент не знайдений.")
        elif choice == "8":
            student_id = int(input("Введіть номер студента: "))
            student = student_repository.get_student(student_id)
            if student:
                course_name = input("Введіть назву курсу: ")

                for existing_course in student.get_courses():
                    if existing_course.get_name() == course_name:
                        course = existing_course
                        break
                else:
                    print("Course not found for this student.")
                    return

                grade = int(input("Введіть оцінку: "))
                student.add_grade(course, grade)
                print(f"Оцінка {grade} додана для студента на курсі {course_name}.")
            else:
                print("Студент не знайдений.")
        elif choice == "9":
            for student_id, student in student_repository._students.items():
                print(Fore.YELLOW + f"Student ID: {student_id}")
                print(f"Name: {student.get_name()} {student.get_surname()}")
                print("Courses:")
                for course in student.get_courses():
                    print(f"- {course.get_name()}")
                    grade = student.get_grade(course.get_name())
                    print(f"  Grade: {grade}" if grade is not None else "  Grade: N/A" + Style.RESET_ALL)
                print("\n")
        elif choice == "0":
            exit()
        else:
            print("Невірний вибір. Спробуйте ще раз.")
    except Exception as e:
        print(Fore.BLACK + f"Error: {e}" + Style.RESET_ALL)


student_repository = InMemoryStudentRepository()

while True:
    print_menu()
    user_choice = input(Fore.LIGHTRED_EX + "Введіть номер опції: ")
    execute_choice(user_choice)
