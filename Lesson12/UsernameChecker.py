# 17. Создайте класс UsernameChecker с методом is_valid(username), который
# проверяет, состоит ли имя пользователя только из букв и цифр


class UsernameChecker:

    def __init__(self, name):
        self.name = name

    def is_valid(self, username):
        self.username = username
        return username == isdigit(username) and isalpha(username)

obj = UsernameChecker ("ghkwfb444")
print(obj.is_valid())