# 6. Создайте класс Student с атрибутами name и grades (список оценок).
# Добавьте метод average_grade, который возвращает среднюю оценку

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def set_grade(self, grades):
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

pupil = Student("Pupil")
for i in range(1, 7):
    pupil.add_grade(i)
print(pupil.average_grade())

ken = Student("Ken")
ken.set_grade([4, 8, 6, 5, 2])
print(ken.average_grade())