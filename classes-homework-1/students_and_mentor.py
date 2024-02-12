class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grade = 0

    def __lt__(self, other):
        return self.average_grade < other.average_grade

    def __le__(self, other):
        return self.average_grade <= other.average_grade

    def __eq__(self, other):
        return self.average_grade == other.average_grade

    def __ne__(self, other):
        return self.average_grade != other.average_grade

    def __ge__(self, other):
        return self.average_grade >= other.average_grade

    def __gt__(self, other):
        return self.average_grade > other.average_grade

    def __str__(self):
        if self.finished_courses:
            finished_courses = ",".join(self.finished_courses)
        else:
            finished_courses = 'Еще молодой все еще впереди'
        if self.courses_in_progress:
            courses_in_progress = ",".join(self.courses_in_progress)
        else:
            courses_in_progress = 'Проверьте, прошла ли ваша оплата'

        return (f'Имя: {self.name}' + '\n'
                f'Фамилия: {self.surname}' + '\n'
                f'Средняя оценка за домашние задания: {self.average_grade}'+'\n'
                f'Курсы в процессе изучения: {courses_in_progress}' + '\n'
                f'Завершенные курсы: {finished_courses}' + '\n')
   
    def update_average(self):
        if self.grades:
            self.average_grade = (sum(map(sum, self.grades.values()))/
                    sum(map(len, self.grades.values())))
        return

    def rate_lecturer(self, lecturer, course, rating):
        if (isinstance(lecturer, Lecturer) 
               and course in self.courses_in_progress
               and course in lecturer.courses_attached):
            if course in lecturer.course_rating:
                lecturer.course_rating[course] += [rating]
            else:
                lecturer.course_rating[course] = [rating]
            lecturer.update_average()
        else:
            return 'Ошибка'


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.average_rating = 0
    

class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.course_rating = {}

    def __lt__(self, other):
        return self.average_rating < other.average_rating

    def __le__(self, other):
        return self.average_rating <= other.average_rating

    def __eq__(self, other):
        return self.average_rating == other.average_rating

    def __ne__(self, other):
        return self.average_rating != other.average_rating

    def __ge__(self, other):
        return self.average_rating >= other.average_rating

    def __gt__(self, other):
        return self.average_rating > other.average_rating

    def __str__(self):
        if self.course_rating:
            average_rating = (sum(map(sum, self.course_rating.values()))/
                    sum(map(len, self.course_rating.values())))

        return (f'Имя: {self.name}' + '\n'
                f'Фамилия: {self.surname}' + '\n'
                f'Средняя оценка за лекции: {self.average_rating}' + '\n')

    def update_average(self):
        if self.course_rating:
            self.average_rating = (sum(map(sum, self.course_rating.values()))/
                    sum(map(len, self.course_rating.values())))
        return

class Reviever(Mentor):

    def __str__(self):
        return (f'Имя: {self.name}' + '\n'
                f'Фамилия: {self.surname}' + '\n')

    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and course in self.courses_attached 
                and course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
            student.update_average()
        else:
            return 'Ошибка'

def average_students_grade(students, course):
    return (sum(sum(_.grades[course]) if _.grades[course] else 0 
           for _ in students) / sum(len(_.grades[course]) if _.grades[course] 
           else 0 for _ in students))

def average_lecturers_rating(lecturers, course):
    return (sum(sum(_.course_rating[course]) if _.course_rating[course] else 0 
           for _ in lecturers) / sum(len(_.course_rating[course]) 
           if _.course_rating[course] else 0 for _ in lecturers))

lec1 = Lecturer('Имя первого лектора', 'Фамилия первого лектора')
lec1.courses_attached += ['Git', 'Python']
lec2 = Lecturer('Имя второго лектора', 'Фамилия второго лектора')
lec2.courses_attached += ['Git', 'Python']
st1 = Student('Имя первого студента', 'Фамилия первого студента', 'пол1')
st1.courses_in_progress += ['Git','Python']
st1.rate_lecturer(lec1,'Git',2)
st1.rate_lecturer(lec1,'Python',7)
st1.rate_lecturer(lec2,'Git',4)
st1.rate_lecturer(lec2,'Python',3)
st2 = Student('Имя второго студента', 'Фамилия второго студента', 'пол2')
st2.courses_in_progress += ['Git','Python']
st2.rate_lecturer(lec1,'Git',5)
st2.rate_lecturer(lec1,'Python',9)
st2.rate_lecturer(lec2,'Git',1)
st2.rate_lecturer(lec2,'Python',8)
rev1 = Reviever('Имя первого проверяющего', 'Фамилия первого проверяющего')
rev1.courses_attached += ['Git']
rev1.rate_hw(st1, 'Git', 1)
rev1.rate_hw(st2, 'Git', 4)
rev2 = Reviever('Имя второго проверяющего', 'Фамилия второго проверяющего')
rev2.courses_attached += ['Python']
rev2.rate_hw(st1, 'Python', 7)
rev2.rate_hw(st2, 'Python', 3)

print(lec1 > lec2)
print(rev1,rev2,lec1, lec2, st1, st2)
print(lec1.course_rating['Git'], st1.grades['Git'])
print('average_students_grade:',average_students_grade([st1,st2],'Git'))
print('average_lecturers_rating:',average_lecturers_rating([lec1,lec2],'Git'))
