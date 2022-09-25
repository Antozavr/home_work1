class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_course(self, course_name):
        self.finished_courses.append(course_name)

    def rate(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and \
                course in lecturer.courses_attached:
            if course in lecturer.course_grades:
                lecturer.course_grades[course] += [grade]
            else:
                lecturer.course_grades[course] = [grade]
        else:
            return 'Ошибка'

    def count_grades(self):
        middle_grades_py = sum(self.grades['Python']) / len(self.grades['Python'])
        middle_grades_git = sum(self.grades['Python']) / len(self.grades['Python'])
        ratio_py_git = (middle_grades_git + middle_grades_py) / len(self.grades)
        return round(ratio_py_git, 1)

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Студентом не является')
            return
        return best_student.count_grades() > bad_student.count_grades()

    def __str__(self):
        self.some_student = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашнее задание: ' \
                            f'{self.count_grades()}\n' \
                            f'Курсы в процессе изучения: {",".join(self.courses_in_progress)}\nЗавершенные курсы: ' \
                            f'{" ".join(self.finished_courses)}'
        return self.some_student


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.course_grades = {}

    def __calculation_grades(self):
        middle_grades_py = sum(self.course_grades['Python']) / len(self.course_grades['Python'])
        middle_grades_git = sum(self.course_grades['Python']) / len(self.course_grades['Python'])
        ratio_py_git = (middle_grades_git + middle_grades_py) / len(self.course_grades)
        return round(ratio_py_git, 1)

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Не является лектором')
            return
        return cool_lecturer.__calculation_grades() < bad_lecturer.__calculation_grades()

    def __str__(self):
        self.some_lecturer = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: ' \
                             f'{self.__calculation_grades()}'
        return self.some_lecturer


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        self.some_reviewer = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        return self.some_reviewer


best_student = Student('Arkady', 'Parovozov', 'male')
best_student.finished_courses += ['Git']
best_student.courses_in_progress += ['Python']
best_student.grades['Git'] = [10, 9, 10, 10]
best_student.grades['Python'] = [9, 10]
bad_student = Student('Alexander', 'Petrov', 'male')
bad_student.finished_courses += []
bad_student.courses_in_progress += ['Python', 'Git']
bad_student.grades['Git'] = [2, 3, 4, 1]
bad_student.grades['Python'] = [2, 3]
cool_lecturer = Lecturer('Irina', 'Vetrova')
cool_lecturer.courses_attached = ['Git', 'Python']
bad_lecturer = Lecturer('Nikolai', 'Melnikov')
bad_lecturer.courses_attached = ['Git', 'Python']
best_student.rate(bad_lecturer, 'Git', 4)
best_student.rate(cool_lecturer, 'Git', 9)
best_student.rate(bad_lecturer, 'Python', 2)
best_student.rate(cool_lecturer, 'Python', 10)
best_student.rate(bad_lecturer, 'Git', 1)
best_student.rate(cool_lecturer, 'Git', 10)
best_student.rate(bad_lecturer, 'Python', 3)
best_student.rate(cool_lecturer, 'Python', 9)
bad_student.rate(bad_lecturer, 'Git', 4)
bad_student.rate(cool_lecturer, 'Git', 9)
bad_student.rate(bad_lecturer, 'Python', 2)
bad_student.rate(cool_lecturer, 'Python', 10)
bad_student.rate(bad_lecturer, 'Git', 1)
bad_student.rate(cool_lecturer, 'Git', 10)
bad_student.rate(bad_lecturer, 'Python', 3)
bad_student.rate(cool_lecturer, 'Python', 9)
first_reviewer = Reviewer('Mark', 'Lipatov')
first_reviewer.courses_attached += ['Python', 'Git']
second_reviewer = Reviewer('Alena', 'Morozova')
second_reviewer.courses_attached += ['Python', 'Git']
first_reviewer.rate_hw(best_student, 'Python', 9)
second_reviewer.rate_hw(best_student, 'Python', 10)
first_reviewer.rate_hw(best_student, 'Python', 8)
second_reviewer.rate_hw(best_student, 'Python', 9)
first_reviewer.rate_hw(best_student, 'Python', 10)
second_reviewer.rate_hw(best_student, 'Python', 9)
first_reviewer.rate_hw(best_student, 'Git', 7)
second_reviewer.rate_hw(best_student, 'Git', 9)
first_reviewer.rate_hw(best_student, 'Git', 8)
second_reviewer.rate_hw(best_student, 'Git', 9)
first_reviewer.rate_hw(best_student, 'Git', 10)
second_reviewer.rate_hw(best_student, 'Git', 8)
first_reviewer.rate_hw(bad_student, 'Python', 3)
second_reviewer.rate_hw(bad_student, 'Python', 2)
first_reviewer.rate_hw(bad_student, 'Python', 1)
second_reviewer.rate_hw(bad_student, 'Python', 4)
first_reviewer.rate_hw(bad_student, 'Python', 1)
second_reviewer.rate_hw(bad_student, 'Python', 3)
first_reviewer.rate_hw(bad_student, 'Git', 1)
second_reviewer.rate_hw(bad_student, 'Git', 2)
first_reviewer.rate_hw(bad_student, 'Git', 1)
second_reviewer.rate_hw(bad_student, 'Git', 3)
first_reviewer.rate_hw(bad_student, 'Git', 2)
second_reviewer.rate_hw(bad_student, 'Git', 1)

all_student = [best_student, bad_student]
all_lecturer = [cool_lecturer, bad_lecturer]


def average_grades_std(student, course):
    grade_list = []
    for student in all_student:
        if course in student.grades:
            grade_list += student.grades[course]
        else:
            return 'Ошибка'
        total_grades_std = sum(grade_list) / len(grade_list)
    return round(total_grades_std, 1)


def average_grades_lcr(lecturer, course):
    list_grade = []
    for lecturer in all_lecturer:
        if course in lecturer.course_grades:
            list_grade += lecturer.course_grades[course]
        else:
            return 'Ошибка'
        total_grades_lcr = sum(list_grade) / len(list_grade)
    return round(total_grades_lcr, 1)


print('Студенты:')
print(best_student.__str__())
print(bad_student.__str__())
print('Лекторы')
print(cool_lecturer.__str__())
print(bad_lecturer.__str__())
print('Ревьюеры:')
print(first_reviewer.__str__())
print(second_reviewer.__str__())
print(f'Средняя оценка у Arkady Parovozova больше чем у Alexandra Petrova?\n{best_student.__lt__(bad_student)}')
print(f'Средняя оценка у лектора Nikolay Melnikov меньше чем у Irina Vetrova?\n{cool_lecturer.__lt__(bad_lecturer)}')
print(f'Средний бал по курсу Python среди студентов:{average_grades_std(all_student,"Python")}')
print(f'Средний бал по курсу Git среди студентов:{average_grades_std(all_student,"Git")}')
print(f'Средний бал по курсу Python среди лекторов:{average_grades_lcr(all_lecturer,"Python")}')
print(f'Средний бал по курсу Git среди лекторов:{average_grades_lcr(all_lecturer,"Git")}')